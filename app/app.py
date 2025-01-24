from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, session
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Quiz, Question, QuestionChoice, QuizResult, db
from authlib.integrations.flask_client import OAuth
import random
import os

# Initialize OAuth
oauth = OAuth()

def init_oauth(app):
    oauth.init_app(app)
    google = oauth.register(
        name='google',
        client_id="501602680733-kll08lan2nqp6at4bkcrp1m5c8do5k2l.apps.googleusercontent.com",
        client_secret="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",
        access_token_url='https://accounts.google.com/o/oauth2/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/userinfo/v2/me',
        client_kwargs={'scope': 'openid email profile'},
    )

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/login/google')
def google_login():
    redirect_uri = url_for('main.google_authorize', _external=True).replace('127.0.0.1', 'localhost')
    # Generate and store state parameter in session
    state = os.urandom(16).hex()
    session['oauth_state'] = state
    return oauth.google.authorize_redirect(redirect_uri, state=state)

@main_blueprint.route('/login/google/authorize')
def google_authorize():
    # Verify state parameter matches
    if 'oauth_state' not in session or request.args.get('state') != session.pop('oauth_state'):
        flash('Invalid state parameter. Please try logging in again.', 'error')
        return redirect(url_for('main.login'))
        
    token = oauth.google.authorize_access_token()
    if not token:
        flash('Google login failed. Please try again.', 'error')
        return redirect(url_for('main.login'))
    
    userinfo = oauth.google.parse_id_token(token)
    if not userinfo:
        flash('Failed to get user info from Google.', 'error')
        return redirect(url_for('main.login'))
    
    google_id = userinfo['sub']
    email = userinfo['email']
    name = userinfo.get('name', email.split('@')[0])
    
    # Check if user exists by Google ID
    user = User.get_by_google_id(google_id)
    if not user:
        # Check if user exists by email
        user = User.query.filter_by(email=email).first()
        if user:
            # Update existing user with Google ID
            user.google_id = google_id
            db.session.commit()
        else:
            # Create new user
            user = User.create_from_google(google_id, email, name)
    
    login_user(user)
    flash('Logged in successfully with Google!', 'success')
    return redirect(url_for('main.home'))


@main_blueprint.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        
        new_quiz = Quiz(
            title=title, 
            description=description, 
            user_id=current_user.id,
            is_system_quiz=False,
            status='pending'
        )
        db.session.add(new_quiz)
        db.session.commit()

        # Process questions
        questions = request.form.getlist('question')
        for i, question_text in enumerate(questions):
            # Create question
            question = Question(quiz_id=new_quiz.id, text=question_text)
            db.session.add(question)
            db.session.commit()

            # Process choices for this question
            choices = request.form.getlist(f'choices_{i}')
            correct_choice = request.form.get(f'correct_choice_{i}')

            for j, choice_text in enumerate(choices):
                if choice_text.strip():  # Only add non-empty choices
                    is_correct = (str(j) == correct_choice)
                    choice = QuestionChoice(
                        question_id=question.id, 
                        text=choice_text, 
                        is_correct=is_correct
                    )
                    db.session.add(choice)
        
        db.session.commit()
        flash('Quiz created successfully!')
        return redirect(url_for('main.home'))
    
    return render_template('create_quiz.html')

@main_blueprint.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    # Check if user has already taken this quiz
    existing_result = QuizResult.query.filter_by(
        user_id=current_user.id, 
        quiz_id=quiz_id
    ).first()
    
    if request.method == 'POST':
        # Process quiz submission
        total_questions = quiz.questions.count()
        correct_answers = 0
        
        for question in quiz.questions:
            selected_choice_id = request.form.get(f'question_{question.id}')
            if selected_choice_id:
                choice = QuestionChoice.query.get(selected_choice_id)
                if choice and choice.is_correct:
                    correct_answers += 1
        
        # Calculate score percentage
        score_percentage = (correct_answers / total_questions) * 100
        
        # Save quiz result
        result = QuizResult(
            user_id=current_user.id, 
            quiz_id=quiz.id, 
            score=correct_answers, 
            total_questions=total_questions
        )
        db.session.add(result)
        
        
        
        # Award points only if: User hasn't taken this quiz before n user got at least 50% correct
        if not existing_result and score_percentage >= 50:
            current_user.score += 1
        
        db.session.commit()
        
        return render_template('quiz_result.html', 
                               quiz=quiz, 
                               score=correct_answers, 
                               total_questions=total_questions,
                               score_percentage=score_percentage)
    
    # Randomize question order
    questions = list(quiz.questions)
    random.shuffle(questions)
    
    return render_template('quiz.html', 
                           quiz=quiz, 
                           questions=questions, 
                           already_taken=existing_result is not None)

@main_blueprint.route('/quiz/edit/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def edit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    # Ensure only the quiz creator can edit
    if quiz.user_id != current_user.id:
        flash('You are not authorized to edit this quiz.')
        return redirect(url_for('main.home'))
    
    if request.method == 'POST':
        # Update quiz logic
        quiz.title = request.form['title']
        quiz.description = request.form['description']
        db.session.commit()
        flash('Quiz updated successfully!')
        return redirect(url_for('main.home'))
    
    return render_template('edit_quiz.html', quiz=quiz)

@main_blueprint.route('/quiz/delete/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def delete_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    # Ensure only the quiz creator can delete
    if quiz.user_id != current_user.id:
        flash('You are not authorized to delete this quiz.')
        return redirect(url_for('main.home'))
    
    try:
        # First, delete all related quiz results
        QuizResult.query.filter_by(quiz_id=quiz_id).delete()
        
        # Then, delete all choices for questions in this quiz
        for question in quiz.questions:
            QuestionChoice.query.filter_by(question_id=question.id).delete()
        
        # Delete all questions in this quiz
        Question.query.filter_by(quiz_id=quiz_id).delete()
        
        # Finally, delete the quiz itself
        db.session.delete(quiz)
        db.session.commit()
        
        flash('Quiz deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash(f'An error occurred while deleting the quiz: {str(e)}')
    
    return redirect(url_for('main.home'))


@main_blueprint.route('/leaderboard')
def leaderboard():
    # Get users sorted by their score in descending order
    top_users = User.query.filter_by(is_admin=False).order_by(User.score.desc()).limit(10).all()
    
    return render_template('leaderboard.html', top_users=top_users)

@main_blueprint.route('/')
def home():
    # Get system quizzes
    system_quizzes = Quiz.query.filter_by(is_system_quiz=True).all()
    
    # Get user's approved quizzes
    user_quizzes = []
    if current_user.is_authenticated:
        user_quizzes = Quiz.query.filter_by(
            user_id=current_user.id,
            status='approved'
        ).all()
    
    # Get all approved quizzes from all users
    all_quizzes = Quiz.query.filter_by(
        status='approved',
        is_system_quiz=False
    ).all()
    
    return render_template('home.html',
                         system_quizzes=system_quizzes,
                         user_quizzes=user_quizzes,
                         all_quizzes=all_quizzes,
                         Quiz=Quiz)

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if username exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('main.register'))
            
        # Check if email exists
        if User.query.filter_by(email=email).first():
            flash('Email address already registered')
            return redirect(url_for('main.register'))
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.home'))
        
        flash('Invalid username or password')
    
    return render_template('login.html')

@main_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))