from flask import Blueprint, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from ..models.models import db, Tournament, Player

bp = Blueprint('main', __name__)

class RegistrationForm(FlaskForm):
    first_name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellidos', validators=[DataRequired()])
    license_number = StringField('Licencia', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Teléfono', validators=[DataRequired()])
    category = SelectField('Categoría', choices=[
        ('benjamin_male', 'Benjamín Masculino'),
        ('benjamin_female', 'Benjamín Femenino'),
        ('alevin_male', 'Alevín Masculino'),
        ('alevin_female', 'Alevín Femenino'),
        ('infantil_male', 'Infantil Masculino'),
        ('infantil_female', 'Infantil Femenino'),
        ('cadete_male', 'Cadete Masculino'),
        ('cadete_female', 'Cadete Femenino'),
        ('absolute_male', 'Absoluto Masculino'),
        ('absolute_female', 'Absoluto Femenino')
    ], validators=[DataRequired()])
    notes = TextAreaField('Incidencias')

@bp.route('/')
def index():
    active_tournament = Tournament.query.filter_by(status='active').first()
    upcoming_tournaments = Tournament.query.filter_by(status='upcoming').order_by(Tournament.start_date).limit(3).all()
    form = RegistrationForm()
    return render_template('index.html', tournament=active_tournament, upcoming_tournaments=upcoming_tournaments, form=form)

@bp.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        active_tournament = Tournament.query.filter_by(status='active').first()
        if not active_tournament:
            flash('No hay torneos activos en este momento.', 'error')
            return redirect(url_for('main.index'))

        player = Player(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            license_number=form.license_number.data,
            email=form.email.data,
            phone=form.phone.data,
            category=form.category.data,
            notes=form.notes.data,
            tournament_id=active_tournament.id
        )
        db.session.add(player)
        db.session.commit()
        flash('¡Inscripción realizada con éxito!', 'success')
        return redirect(url_for('main.index'))

    for field, errors in form.errors.items():
        for error in errors:
            flash(f'{getattr(form, field).label.text}: {error}', 'error')
    return redirect(url_for('main.index'))
