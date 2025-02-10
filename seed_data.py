from datetime import datetime, timedelta
from app import create_app, db
from app.models.models import Tournament, Player

def seed_data():
    app = create_app()
    
    with app.app_context():
        # Limpiar datos existentes
        Player.query.delete()
        Tournament.query.delete()
        
        # Crear torneos
        tournaments = [
            Tournament(
                name='Torneo de Primavera 2025',
                start_date=datetime(2025, 3, 15),
                end_date=datetime(2025, 3, 20),
                status='active'
            ),
            Tournament(
                name='Copa Verano 2025',
                start_date=datetime(2025, 7, 1),
                end_date=datetime(2025, 7, 7),
                status='upcoming'
            ),
            Tournament(
                name='Torneo de Invierno 2024',
                start_date=datetime(2024, 12, 10),
                end_date=datetime(2024, 12, 15),
                status='finished'
            ),
            Tournament(
                name='Campeonato Local 2025',
                start_date=datetime(2025, 5, 1),
                end_date=datetime(2025, 5, 5),
                status='upcoming'
            ),
            Tournament(
                name='Torneo de Otoño 2024',
                start_date=datetime(2024, 10, 15),
                end_date=datetime(2024, 10, 20),
                status='finished'
            ),
            Tournament(
                name='Copa Fin de Año 2025',
                start_date=datetime(2025, 12, 27),
                end_date=datetime(2025, 12, 30),
                status='inactive'
            )
        ]
        
        # Añadir torneos a la base de datos
        for tournament in tournaments:
            db.session.add(tournament)
        db.session.commit()
        
        # Crear jugadores
        players = [
            # Jugadores para el Torneo de Primavera (activo)
            Player(
                first_name='Juan',
                last_name='García',
                license_number='LIC001',
                email='juan.garcia@email.com',
                phone='666111222',
                category='benjamin_male',
                notes='Alergia al polen',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='María',
                last_name='López',
                license_number='LIC002',
                email='maria.lopez@email.com',
                phone='666222333',
                category='benjamin_female',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='Carlos',
                last_name='Martínez',
                license_number='LIC003',
                email='carlos.martinez@email.com',
                phone='666333444',
                category='alevin_male',
                tournament_id=tournaments[0].id
            ),
            
            # Jugadores para el Torneo de Invierno (finalizado)
            Player(
                first_name='Ana',
                last_name='Rodríguez',
                license_number='LIC004',
                email='ana.rodriguez@email.com',
                phone='666444555',
                category='infantil_female',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Pablo',
                last_name='Sánchez',
                license_number='LIC005',
                email='pablo.sanchez@email.com',
                phone='666555666',
                category='cadete_male',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Laura',
                last_name='Fernández',
                license_number='LIC006',
                email='laura.fernandez@email.com',
                phone='666666777',
                category='absolute_female',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Miguel',
                last_name='González',
                license_number='LIC007',
                email='miguel.gonzalez@email.com',
                phone='666777888',
                category='absolute_male',
                tournament_id=tournaments[2].id
            ),
            
            # Jugadores para el Torneo de Otoño (finalizado)
            Player(
                first_name='Sara',
                last_name='Pérez',
                license_number='LIC008',
                email='sara.perez@email.com',
                phone='666888999',
                category='infantil_female',
                tournament_id=tournaments[4].id
            ),
            Player(
                first_name='David',
                last_name='Ruiz',
                license_number='LIC009',
                email='david.ruiz@email.com',
                phone='666999000',
                category='cadete_male',
                tournament_id=tournaments[4].id
            ),
            Player(
                first_name='Elena',
                last_name='Moreno',
                license_number='LIC010',
                email='elena.moreno@email.com',
                phone='667000111',
                category='absolute_female',
                tournament_id=tournaments[4].id
            ),
            
            # Más jugadores para el Torneo de Primavera (activo)
            Player(
                first_name='Roberto',
                last_name='Jiménez',
                license_number='LIC011',
                email='roberto.jimenez@email.com',
                phone='667111222',
                category='alevin_male',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='Carmen',
                last_name='Díaz',
                license_number='LIC012',
                email='carmen.diaz@email.com',
                phone='667222333',
                category='alevin_female',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='Jorge',
                last_name='Álvarez',
                license_number='LIC013',
                email='jorge.alvarez@email.com',
                phone='667333444',
                category='infantil_male',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='Lucía',
                last_name='Torres',
                license_number='LIC014',
                email='lucia.torres@email.com',
                phone='667444555',
                category='cadete_female',
                tournament_id=tournaments[0].id
            ),
            Player(
                first_name='Daniel',
                last_name='Romero',
                license_number='LIC015',
                email='daniel.romero@email.com',
                phone='667555666',
                category='absolute_male',
                tournament_id=tournaments[0].id
            ),
            
            # Jugadores adicionales para el Torneo de Invierno (finalizado)
            Player(
                first_name='Marina',
                last_name='Castro',
                license_number='LIC016',
                email='marina.castro@email.com',
                phone='667666777',
                category='benjamin_female',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Alejandro',
                last_name='Ortiz',
                license_number='LIC017',
                email='alejandro.ortiz@email.com',
                phone='667777888',
                category='alevin_male',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Paula',
                last_name='Navarro',
                license_number='LIC018',
                email='paula.navarro@email.com',
                phone='667888999',
                category='infantil_female',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Hugo',
                last_name='Molina',
                license_number='LIC019',
                email='hugo.molina@email.com',
                phone='667999000',
                category='cadete_male',
                tournament_id=tournaments[2].id
            ),
            Player(
                first_name='Alba',
                last_name='Serrano',
                license_number='LIC020',
                email='alba.serrano@email.com',
                phone='668000111',
                category='absolute_female',
                tournament_id=tournaments[2].id
            )
        ]
        
        # Añadir jugadores a la base de datos
        for player in players:
            db.session.add(player)
        db.session.commit()
        
        print("Datos de ejemplo insertados correctamente:")
        print(f"- {len(tournaments)} torneos creados")
        print(f"- {len(players)} jugadores registrados")

if __name__ == '__main__':
    seed_data()
