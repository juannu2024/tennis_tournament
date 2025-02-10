# Gestión de Torneos de Tenis

Una aplicación web desarrollada con Flask para gestionar torneos de tenis, incluyendo inscripciones de jugadores y gestión administrativa.

## Características

- Página pública con formulario de inscripción para torneos activos
- Panel de administración para gestionar torneos y jugadores
- Exportación de jugadores a Excel
- Sistema de autenticación para administradores
- Diseño responsive y moderno

## Requisitos

- Python 3.8 o superior
- MySQL 5.7 o superior

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd tennis_tournament
```

2. Crear un entorno virtual e instalar dependencias:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar la base de datos MySQL:
- Crear una base de datos llamada `tennis_tournament`:
```sql
CREATE DATABASE tennis_tournament;
```
- La aplicación está configurada para usar el usuario `root` sin contraseña
- Si deseas usar credenciales diferentes, puedes configurarlas en un archivo `.env`:
```bash
echo DATABASE_URL=mysql://usuario:contraseña@localhost/tennis_tournament > .env
echo SECRET_KEY=tu-clave-secreta >> .env
```

4. Inicializar la base de datos:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Uso

1. Ejecutar la aplicación:
```bash
python run.py
```

2. Acceder a la aplicación:
- Frontend público: http://localhost:5000
- Panel de administración: http://localhost:5000/auth/login
  - Usuario por defecto: admin
  - Contraseña por defecto: admin123 (¡cambiar en producción!)

## Estructura del Proyecto

```
tennis_tournament/
├── app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── admin/
│   │   ├── auth/
│   │   └── base.html
│   ├── models/
│   ├── routes/
│   └── __init__.py
├── migrations/
├── config.py
├── requirements.txt
├── README.md
└── run.py
```

## Seguridad

- Cambiar la contraseña del administrador por defecto
- Configurar un SECRET_KEY seguro en producción
- Usar HTTPS en producción
- Configurar las credenciales de la base de datos de forma segura

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request
