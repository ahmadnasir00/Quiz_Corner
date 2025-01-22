from app import create_app
from app.models import User, db

app = create_app()

def create_admin():
    with app.app_context():
        # Check if admin already exists
        admin = User.query.filter_by(username='admin').first()
        if admin:
            print("Admin user already exists")
            return
        
        # Create admin user
        admin = User(
            username='admin',
            email='admin@quizcorner.com',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully")

if __name__ == '__main__':
    create_admin()