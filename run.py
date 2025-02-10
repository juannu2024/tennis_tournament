from app import create_app, db
from app.models.models import User

app = create_app()

# Create admin user if it doesn't exist
def create_admin():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('admin123')  # Change this password in production!
            db.session.add(admin)
            db.session.commit()

if __name__ == '__main__':
    create_admin()
    app.run(debug=True)
