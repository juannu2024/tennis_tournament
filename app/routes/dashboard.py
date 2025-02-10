from flask import Blueprint, render_template
from app.models.models import Tournament, Player
from app import db
from sqlalchemy import func
from collections import defaultdict
from flask_login import login_required

bp = Blueprint('dashboard', __name__)

@bp.route('/dashboard')
@login_required
def show_dashboard():
    # Estadísticas generales
    total_tournaments = Tournament.query.count()
    total_players = Player.query.count()
    
    # Inscripciones por torneo
    tournament_stats = db.session.query(
        Tournament.name,
        Tournament.status,
        func.count(Player.id).label('player_count')
    ).outerjoin(Player).group_by(Tournament.id).all()
    
    # Distribución por categorías
    category_stats = db.session.query(
        Player.category,
        func.count(Player.id).label('count')
    ).group_by(Player.category).all()
    
    # Estadísticas por estado del torneo
    status_stats = db.session.query(
        Tournament.status,
        func.count(Tournament.id).label('count')
    ).group_by(Tournament.status).all()
    
    # Promedio de jugadores por torneo
    avg_players = total_players / total_tournaments if total_tournaments > 0 else 0
    
    # Torneos con más inscripciones
    top_tournaments = db.session.query(
        Tournament.name,
        func.count(Player.id).label('player_count')
    ).outerjoin(Player).group_by(Tournament.id)\
    .order_by(func.count(Player.id).desc()).limit(3).all()
    
    # Categorías más populares por torneo
    popular_categories = defaultdict(list)
    tournaments = Tournament.query.all()
    for tournament in tournaments:
        cat_counts = db.session.query(
            Player.category,
            func.count(Player.id).label('count')
        ).filter(Player.tournament_id == tournament.id)\
        .group_by(Player.category)\
        .order_by(func.count(Player.id).desc())\
        .first()
        if cat_counts:
            popular_categories[tournament.name] = {
                'category': cat_counts[0],
                'count': cat_counts[1]
            }

    return render_template('dashboard.html',
                         total_tournaments=total_tournaments,
                         total_players=total_players,
                         tournament_stats=tournament_stats,
                         category_stats=category_stats,
                         status_stats=status_stats,
                         avg_players=round(avg_players, 2),
                         top_tournaments=top_tournaments,
                         popular_categories=dict(popular_categories))
