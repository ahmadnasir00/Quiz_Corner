from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, Quiz, db

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))
    
    pending_quizzes = Quiz.query.filter_by(status='pending').all()
    # Get all users
    users = User.query.all()
    
    return render_template('admin/dashboard.html', 
                         pending_quizzes=pending_quizzes,
                         users=users)

@admin_blueprint.route('/admin/approve_quiz/<int:quiz_id>')
@login_required
def approve_quiz(quiz_id):
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))
    
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz.status = 'approved'
    db.session.commit()
    flash('Quiz approved successfully')
    return redirect(url_for('admin.admin_dashboard'))

@admin_blueprint.route('/admin/reject_quiz/<int:quiz_id>')
@login_required
def reject_quiz(quiz_id):
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))
    
    quiz = Quiz.query.get_or_404(quiz_id)
    db.session.delete(quiz)
    db.session.commit()
    flash('Quiz deleted')
    return redirect(url_for('admin.admin_dashboard'))

@admin_blueprint.route('/admin/delete_user/<int:user_id>')
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('admin.admin_dashboard'))

@admin_blueprint.route('/admin/reset_password/<int:user_id>')
@login_required
def reset_password(user_id):
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))
    
    user = User.query.get_or_404(user_id)
    # Set default password
    user.set_password('password123')
    db.session.commit()
    flash(f"Password reset for {user.username} to 'password123'")
    return redirect(url_for('admin.admin_dashboard'))