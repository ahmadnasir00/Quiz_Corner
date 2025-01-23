# Quiz App Documentation

## CHAPTER ONE: INTRODUCTION

### 1.1 Project Background
The Quiz App is a web-based application designed to provide an interactive platform for creating, taking, and managing quizzes. With the increasing demand for online learning and assessment tools, this application aims to fill the gap by offering a simple yet powerful solution for both educators and learners.

### 1.2 Problem Statement
Traditional paper-based quizzes are time-consuming to create, distribute, and grade. There is a need for a digital solution that:
- Allows easy creation and management of quizzes
- Provides instant feedback to users
- Tracks user progress and performance
- Offers a user-friendly interface for both quiz creators and takers

### 1.3 Project Aim and Objectives
**Aim:**
To develop a web-based quiz application that provides an efficient and user-friendly platform for creating, taking, and managing quizzes.

**Objectives:**
1. Develop a secure user authentication system
2. Implement quiz creation and editing features
3. Create a responsive user interface for taking quizzes
4. Develop a scoring and leaderboard system
5. Implement admin features for managing quizzes and users

### 1.4 Project Motivation
The motivation behind this project stems from:
- The growing need for digital learning tools
- The desire to create a more engaging assessment experience
- The opportunity to provide instant feedback to learners
- The need for a centralized platform for quiz management

### 1.5 Project Scope
The Quiz App will include:
- User registration and authentication
- Quiz creation and editing tools
- Interactive quiz-taking interface
- Real-time scoring and feedback
- Leaderboard and user progress tracking
- Admin dashboard for managing content

### 1.6 Tools and Technologies Used
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Flask
- **Database:** SQLite (development), PostgreSQL (production)
- **Authentication:** Flask-Login, OAuth (Google)
- **Version Control:** Git
- **Deployment:** Docker, Nginx

### 1.7 Project Limitations and Delimitations
**Limitations:**
- Initial version supports only multiple-choice questions
- Limited to text-based questions and answers
- No support for multimedia content in quizzes

**Delimitations:**
- Focus on web platform only (no mobile app)
- Support for English language only
- Limited to individual user accounts (no organizational accounts)

### 1.8 Project Plan and Schedule
The project was developed over 3 months following this schedule:
1. Requirements gathering and analysis (2 weeks)
2. System design and architecture (2 weeks)
3. Core feature development (4 weeks)
4. Testing and quality assurance (2 weeks)
5. Deployment and documentation (2 weeks)

### 1.9 Outline of the Project
This documentation is organized into six chapters:
1. Introduction
2. Existing and Proposed Systems
3. System Analysis and Design
4. System Implementation
5. System Evaluation and Testing
6. Conclusions and Future Work

## CHAPTER TWO: EXISTING AND PROPOSED SYSTEMS

### 2.1 Introduction
This chapter examines the current landscape of quiz applications and presents the proposed solution. It compares existing systems with our proposed system and evaluates its feasibility.

### 2.2 Existing Systems
Several quiz applications currently exist in the market:
1. **Kahoot!**
   - Popular game-based learning platform
   - Focuses on live, multiplayer quizzes
   - Limited customization options
   
2. **Quizlet**
   - Flashcard-based learning system
   - Includes quiz features
   - Primarily focused on memorization

3. **Google Forms**
   - General-purpose form builder
   - Basic quiz functionality
   - Lacks specialized quiz features

4. **Moodle Quizzes**
   - Part of comprehensive LMS
   - Complex setup and configuration
   - Geared towards institutional use

### 2.3 Proposed System
Our proposed Quiz App aims to combine the best features of existing systems while addressing their limitations.

#### 2.3.1 Product Perspective
The Quiz App is a standalone web application that:
- Provides a simple interface for quiz creation
- Offers flexible quiz-taking options
- Includes progress tracking and analytics
- Supports both individual and competitive use

#### 2.3.2 Product Functions
Key functions include:
- User registration and authentication
- Quiz creation and editing
- Real-time quiz taking
- Instant scoring and feedback
- Leaderboard and progress tracking
- Admin dashboard for management

#### 2.3.3 User Characteristics
The system serves three main user groups:
1. **Quiz Creators**
   - Educators
   - Content creators
   - Business trainers

2. **Quiz Takers**
   - Students
   - Employees
   - General learners

3. **Administrators**
   - System maintainers
   - Content moderators

#### 2.3.4 Constraints
- Must support at least 100 concurrent users
- Should handle up to 1000 quizzes
- Must maintain 99.9% uptime
- Should comply with data protection regulations

#### 2.3.5 Assumptions and Dependencies
- Users have basic computer literacy
- Internet connectivity is available
- Modern web browsers are used
- Google authentication service is available

### 2.4 Feasibility Study for the Proposed System

#### 2.4.1 Competition
The main competitors are:
- Kahoot!
- Quizlet
- Google Forms
- Moodle Quizzes

#### 2.4.2 Intended Market Environment
The target market includes:
- Educational institutions
- Corporate training departments
- Individual educators
- Self-learners

#### 2.4.3 Possible Solutions
Three potential solutions were considered:
1. Custom web application (chosen solution)
2. Moodle plugin
3. Google Forms extension

#### 2.4.4 Evaluation Criteria
Solutions were evaluated based on:
- Customization flexibility
- Development complexity
- Maintenance requirements
- User experience

#### 2.4.5 Identifying the Most Feasible Solution
The custom web application was chosen because:
- Offers complete control over features
- Provides better user experience
- Allows for future expansion
- Enables unique branding

#### 2.4.6 Critical Risk Factors
Main risks include:
- User adoption rate
- Competition from established players
- Data security concerns
- Scalability challenges

#### 2.4.7 Conclusion
The proposed system offers a balanced solution that addresses market needs while being technically feasible and economically viable.

### 2.5 SDLC for the Proposed System
The system follows the Agile development methodology:
1. Requirements gathering
2. Sprint planning
3. Iterative development
4. Continuous testing
5. Regular deployment
6. User feedback incorporation

## CHAPTER THREE: SYSTEM ANALYSIS AND DESIGN

### 3.1 System Analysis

#### 3.1.1 Requirement Elicitation Techniques
The following techniques were used to gather requirements:
1. **Interviews:** Conducted with potential users and stakeholders
2. **Surveys:** Distributed to educators and students
3. **Observation:** Studied existing quiz platforms
4. **Document Analysis:** Reviewed educational standards and guidelines

#### 3.1.2 Specific Requirements

##### 3.1.2.1 External Interfaces
The system interfaces with:
1. **Google Authentication API** for user login
2. **Email Service** for notifications
3. **Web Browsers** for user interaction
4. **Database** for persistent storage

##### 3.1.2.2 Functional Requirements
Key functional requirements include:
1. User authentication and authorization
2. Quiz creation and management
3. Real-time quiz taking
4. Scoring and feedback system
5. Progress tracking and reporting
6. Admin dashboard functionality

##### 3.1.2.3 Design Constraints
The system must:
1. Support multiple concurrent users
2. Maintain data integrity and security
3. Provide responsive design for various devices
4. Ensure accessibility compliance
5. Support internationalization

### 3.2 System Design

#### 3.2.1 ER-Diagram
The Entity-Relationship diagram includes:
- Users
- Quizzes
- Questions
- Choices
- Results
- Leaderboard entries

Relationships:
- One User can create many Quizzes
- One Quiz contains many Questions
- One Question has multiple Choices
- One User can have multiple Results
- Results contribute to Leaderboard entries

#### 3.2.2 Database Schema (Mapping) for ERD
The database schema includes these tables:
1. **users**
   - id (PK)
   - username
   - email
   - password_hash
   - score
   - is_admin

2. **quizzes**
   - id (PK)
   - title
   - description
   - user_id (FK)
   - created_at
   - updated_at

3. **questions**
   - id (PK)
   - quiz_id (FK)
   - text
   - order

4. **choices**
   - id (PK)
   - question_id (FK)
   - text
   - is_correct

5. **results**
   - id (PK)
   - user_id (FK)
   - quiz_id (FK)
   - score
   - total_questions
   - completed_at

6. **leaderboard**
   - id (PK)
   - user_id (FK)
   - score
   - updated_at

#### 3.2.3 Class Diagram
The system's main classes include:
1. **User**
   - Attributes: id, username, email, password
   - Methods: authenticate(), create_quiz()

2. **Quiz**
   - Attributes: id, title, description
   - Methods: add_question(), publish()

3. **Question**
   - Attributes: id, text, order
   - Methods: add_choice(), validate()

4. **Choice**
   - Attributes: id, text, is_correct
   - Methods: mark_correct()

5. **Result**
   - Attributes: id, score, timestamp
   - Methods: calculate_score()

#### 3.2.4 Use Case Diagram
Key use cases:
1. User Registration
2. Quiz Creation
3. Quiz Taking
4. Result Viewing
5. Admin Dashboard Access
6. Leaderboard Viewing

#### 3.2.5 Activity Diagram
Main activities include:
1. User Registration Flow
2. Quiz Creation Process
3. Quiz Taking Sequence
4. Result Calculation
5. Leaderboard Update

#### 3.2.6 Sequence Diagram
Key sequences:
1. User Login Process
2. Quiz Creation Workflow
3. Quiz Taking Interaction
4. Result Calculation Steps
5. Leaderboard Update Sequence

## CHAPTER FOUR: SYSTEM IMPLEMENTATION

### 4.1 Programming Languages

#### 4.1.1 Justification for Using Python and Flask
The Quiz App was implemented using Python and Flask for several key reasons:

1. **Python Advantages:**
   - Clean and readable syntax
   - Extensive standard library
   - Rich ecosystem of packages
   - Strong community support
   - Excellent for rapid development

2. **Flask Advantages:**
   - Lightweight and flexible
   - Easy to learn and use
   - Modular design
   - Excellent for small to medium web applications
   - Extensive documentation and community support

3. **Development Speed:**
   - Python's simplicity and Flask's minimalism enabled rapid prototyping
   - Quick iteration cycles during development
   - Easy to implement new features

4. **Scalability:**
   - Flask's modular architecture allows for easy scaling
   - Ability to add extensions as needed
   - Support for WSGI deployment

5. **Integration Capabilities:**
   - Easy integration with databases (SQLAlchemy)
   - Simple API development
   - Good support for authentication (Flask-Login)

6. **Maintainability:**
   - Python's readability makes code easy to maintain
   - Flask's modular structure promotes clean code organization
   - Easy to add new developers to the project

### 4.2 Implementation

#### 4.2.1 Sample of Forms
The application implements several forms using Flask-WTF:

1. **User Registration Form:**
```python
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
```

2. **Quiz Creation Form:**
```python
class QuizForm(FlaskForm):
    title = StringField('Quiz Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    questions = FieldList(FormField(QuestionForm), min_entries=1)
    submit = SubmitField('Create Quiz')
```

3. **Question Form:**
```python
class QuestionForm(FlaskForm):
    text = TextAreaField('Question Text', validators=[DataRequired()])
    choices = FieldList(FormField(ChoiceForm), min_entries=2)
```

4. **Choice Form:**
```python
class ChoiceForm(FlaskForm):
    text = StringField('Choice Text', validators=[DataRequired()])
    is_correct = BooleanField('Correct Answer')
```

#### 4.2.2 Sample of Reports
The system generates several types of reports:

1. **User Progress Report:**
```python
def generate_user_progress_report(user_id):
    user = User.query.get(user_id)
    quizzes_taken = Result.query.filter_by(user_id=user_id).count()
    average_score = db.session.query(func.avg(Result.score)).filter_by(user_id=user_id).scalar()
    
    return {
        'username': user.username,
        'quizzes_taken': quizzes_taken,
        'average_score': round(average_score, 2),
        'last_activity': user.last_login,
        'leaderboard_position': Leaderboard.query.filter_by(user_id=user_id).first().position
    }
```

2. **Quiz Statistics Report:**
```python
def generate_quiz_statistics(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    total_attempts = Result.query.filter_by(quiz_id=quiz_id).count()
    average_score = db.session.query(func.avg(Result.score)).filter_by(quiz_id=quiz_id).scalar()
    
    return {
        'quiz_title': quiz.title,
        'total_attempts': total_attempts,
        'average_score': round(average_score, 2),
        'most_recent_attempt': Result.query.filter_by(quiz_id=quiz_id)
                                         .order_by(Result.completed_at.desc())
                                         .first().completed_at
    }
```

#### 4.2.3 Pseudo Codes
Here are some key algorithms implemented in the system:

1. **Quiz Scoring Algorithm:**
```
function calculate_score(quiz, user_answers):
    total_questions = quiz.questions.count()
    correct_answers = 0
    
    for question in quiz.questions:
        if user_answers[question.id] == question.correct_answer:
            correct_answers += 1
    
    score = (correct_answers / total_questions) * 100
    return score
```

2. **Leaderboard Update Algorithm:**
```
function update_leaderboard(user, score):
    leaderboard_entry = Leaderboard.query.filter_by(user_id=user.id).first()
    
    if leaderboard_entry:
        leaderboard_entry.score += score
    else:
        new_entry = Leaderboard(user_id=user.id, score=score)
        db.session.add(new_entry)
    
    db.session.commit()
    update_positions()
```

3. **Quiz Validation Algorithm:**
```
function validate_quiz(quiz):
    if quiz.questions.count() < 1:
        return False
    
    for question in quiz.questions:
        if question.choices.count() < 2:
            return False
        if question.correct_choices.count() != 1:
            return False
    
    return True
```

4. **User Authentication Flow:**
```
function authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return True
    else:
        return False
```

5. **Quiz Taking Flow:**
```
function take_quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    if not quiz:
        return error('Quiz not found')
    
    if request.method == 'POST':
        user_answers = process_answers(request.form)
        score = calculate_score(quiz, user_answers)
        save_result(user.id, quiz.id, score)
        update_leaderboard(user, score)
        return redirect_to_results()
    
    return render_quiz(quiz)
```