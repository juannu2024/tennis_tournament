from app import create_app, db
from app.models.models import Tournament, Player
from datetime import datetime, timedelta
import random

app = create_app()

def create_sample_data():
    with app.app_context():
        # Limpiar datos existentes
        Player.query.delete()
        Tournament.query.delete()
        db.session.commit()

        # Crear torneos
        tournaments = [
            {
                'name': 'Torneo de Primavera 2025',
                'start_date': datetime(2025, 3, 15),
                'end_date': datetime(2025, 3, 20),
                'status': 'upcoming',
                'image': 'tournament1.jpg'
            },
            {
                'name': 'Copa Verano Junior',
                'start_date': datetime(2025, 7, 1),
                'end_date': datetime(2025, 7, 5),
                'status': 'upcoming',
                'image': 'tournament2.jpg'
            },
            {
                'name': 'Torneo Municipal 2025',
                'start_date': datetime.now(),
                'end_date': datetime.now() + timedelta(days=5),
                'status': 'active',
                'image': 'tournament3.jpg'
            },
            {
                'name': 'Campeonato Regional',
                'start_date': datetime.now() - timedelta(days=30),
                'end_date': datetime.now() - timedelta(days=25),
                'status': 'finished',
                'image': 'tournament4.jpg'
            },
            {
                'name': 'Torneo de Invierno',
                'start_date': datetime(2025, 12, 10),
                'end_date': datetime(2025, 12, 15),
                'status': 'upcoming',
                'image': 'tournament5.jpg'
            },
            {
                'name': 'Copa Fin de Año',
                'start_date': datetime(2025, 12, 27),
                'end_date': datetime(2025, 12, 30),
                'status': 'upcoming',
                'image': 'tournament6.jpg'
            }
        ]

        created_tournaments = []
        for t in tournaments:
            tournament = Tournament(**t)
            db.session.add(tournament)
            created_tournaments.append(tournament)
        db.session.commit()

        # Categorías disponibles
        categories = [
            'benjamin_male', 'benjamin_female',
            'alevin_male', 'alevin_female',
            'infantil_male', 'infantil_female',
            'cadete_male', 'cadete_female',
            'absolute_male', 'absolute_female'
        ]

        # Nombres y apellidos para generar jugadores
        first_names = ['Juan', 'Ana', 'Carlos', 'María', 'Pedro', 'Laura', 'Miguel', 'Sofia', 'David', 'Elena']
        last_names = ['García', 'Martínez', 'López', 'González', 'Rodríguez', 'Fernández', 'Pérez', 'Sánchez']

        # Crear 20 jugadores
        for i in range(20):
            # Distribuir jugadores entre los torneos
            tournament = random.choice(created_tournaments)
            
            # Generar datos aleatorios para el jugador
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            category = random.choice(categories)
            
            player = Player(
                first_name=first_name,
                last_name=last_name,
                license_number=f'LIC{2025}{i+1:03d}',
                email=f'{first_name.lower()}.{last_name.lower()}@email.com',
                phone=f'6{random.randint(10000000, 99999999)}',
                category=category,
                notes=f'Jugador inscrito en {tournament.name}',
                tournament_id=tournament.id
            )
            db.session.add(player)

        db.session.commit()
        print("Datos de ejemplo creados exitosamente!")

if __name__ == '__main__':
    create_sample_data()
