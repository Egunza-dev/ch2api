import os

from app import create_app

config_name = os.getenv("APP_SETTINGS")

app = create_app(config_name)
from app.api import api as api_v1_blueprint
app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()