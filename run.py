from flask.cli import FlaskGroup, AppGroup
import click

from application import create_app
from application.local_settings import FLASK_PUBLIC_PORT


app = create_app()
cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
