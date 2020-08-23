"""App entry point."""
from flask_sqlalchemy_tutorial import create_app

app = create_app()  # all tables will be created inside our DB

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
