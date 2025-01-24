from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from .models import User, Quiz, db

# Icon upload configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}

def get_upload_folder():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'images')

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
    
    # Get current icon
    current_icon = None
    upload_folder = get_upload_folder()
    if os.path.exists(upload_folder):
        for file in os.listdir(upload_folder):
            if file.startswith('icon.'):
                current_icon = file
                break

    return render_template('admin/dashboard.html',
                         pending_quizzes=pending_quizzes,
                         users=users,
                         current_icon=current_icon)

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

@admin_blueprint.route('/admin/upload_icon', methods=['POST'])
@login_required
def upload_icon():
    if not current_user.is_admin:
        flash('Access denied')
        return redirect(url_for('main.home'))

    if 'icon' not in request.files:
        flash('No file selected')
        return redirect(url_for('admin.admin_dashboard'))

    file = request.files['icon']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('admin.admin_dashboard'))

    if file and allowed_file(file.filename):
        # Delete existing icon
        upload_folder = get_upload_folder()
        if os.path.exists(upload_folder):
            for existing_file in os.listdir(upload_folder):
                if existing_file.startswith('icon.'):
                    os.remove(os.path.join(upload_folder, existing_file))

        # Save new icon
        filename = 'icon.' + file.filename.rsplit('.', 1)[1].lower()
        file.save(os.path.join(upload_folder, filename))
        flash('Icon uploaded successfully')
    else:
        flash('Invalid file type. Allowed types: png, jpg, jpeg, svg')

    return redirect(url_for('admin.admin_dashboard'))