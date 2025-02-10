from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('active', 'inactive', 'upcoming', 'finished'), nullable=False)
    image = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    players = db.relationship('Player', backref='tournament', lazy=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    license_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    category = db.Column(db.Enum(
        'benjamin_male', 'benjamin_female',
        'alevin_male', 'alevin_female',
        'infantil_male', 'infantil_female',
        'cadete_male', 'cadete_female',
        'absolute_male', 'absolute_female'
    ), nullable=False)
    notes = db.Column(db.Text)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def category_order(self):
        category_map = {
            'benjamin': 1,
            'alevin': 2,
            'infantil': 3,
            'cadete': 4,
            'absolute': 5
        }
        base_category = self.category.split('_')[0]
        return category_map.get(base_category, 999)
