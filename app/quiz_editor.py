from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from app.models import db, Quiz, Question, QuestionChoice
from flask_login import login_required, current_user
import logging

quiz_editor_bp = Blueprint('quiz_editor', __name__)
logger = logging.getLogger(__name__)

@quiz_editor_bp.route('/edit-quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def edit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        try:
            # Debug log form data
            logger.debug(f"Form data received: {request.form}")
            
            # Update quiz details
            new_title = request.form.get('title')
            new_description = request.form.get('description')
            logger.debug(f"Updating quiz {quiz.id}: title={new_title}, description={new_description}")
            
            quiz.title = new_title
            quiz.description = new_description
            db.session.add(quiz)
            
            # Process existing questions
            for question in quiz.questions:
                question_text = request.form.get(f'question-{question.id}-text')
                logger.debug(f"Updating question {question.id}: text={question_text}")
                
                question.text = question_text
                db.session.add(question)
                
                # Process choices
                for choice in question.choices:
                    choice_text = request.form.get(f'question-{question.id}-choice-{choice.id}')
                    correct_choice_id = request.form.get(f'question-{question.id}-correct')
                    is_correct = (str(choice.id) == correct_choice_id)
                    
                    logger.debug(f"Updating choice {choice.id}: text={choice_text}, correct={is_correct}")
                    
                    choice.text = choice_text
                    choice.is_correct = is_correct
                    db.session.add(choice)
                
                # Check if question should be deleted
                if request.form.get(f'delete-question-{question.id}') == 'true':
                    logger.debug(f"Deleting question {question.id}")
                    db.session.delete(question)
            
            # Handle new questions
            new_question_count = int(request.form.get('new-question-count', 0))
            logger.debug(f"Processing {new_question_count} new questions")
            
            for i in range(1, new_question_count + 1):
                question_text = request.form.get(f'new-question-{i}-text')
                if question_text:
                    logger.debug(f"Adding new question {i}: {question_text}")
                    question = Question(
                        text=question_text,
                        quiz_id=quiz.id
                    )
                    db.session.add(question)
                    db.session.flush()
                    
                    # Add choices for new question
                    choice_count = int(request.form.get(f'new-question-{i}-choice-count', 0))
                    for j in range(1, choice_count + 1):
                        choice_text = request.form.get(f'new-question-{i}-choice-{j}-text')
                        if choice_text:
                            logger.debug(f"Adding new choice {j} to question {i}: {choice_text}")
                            choice = QuestionChoice(
                                text=choice_text,
                                question_id=question.id,
                                is_correct=(request.form.get(f'new-question-{i}-correct') == str(j))
                            )
                            db.session.add(choice)
            
            # Commit all changes
            db.session.commit()
            logger.info(f"Quiz {quiz.id} updated successfully by user {current_user.id}")
            flash('Quiz updated successfully!', 'success')
            
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error updating quiz {quiz.id}: {str(e)}")
            logger.error(f"Form data: {request.form}")
            logger.exception(e)
            flash('Failed to update quiz. Please try again.', 'error')
        
        return redirect(url_for('quiz_editor.edit_quiz', quiz_id=quiz.id))
    
    return render_template('edit_quiz.html', quiz=quiz)

# ... rest of the file remains unchanged ...
