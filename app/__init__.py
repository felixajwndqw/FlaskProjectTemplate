from flask import Flask
import config
from flask_wtf.csrf import CSRFProtect
from flask_babel import Babel


csrf = CSRFProtect()
babel = Babel()


def create_app(config_class=config.Config):
    app = Flask(__name__)
    app.config.from_object(config.ProductionConfig)

    csrf.init_app(app)
    babel.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
