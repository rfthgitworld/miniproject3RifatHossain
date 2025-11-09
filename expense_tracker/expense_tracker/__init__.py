from flask import Flask, redirect, url_for
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'expense_tracker.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import and initialize DB
    from . import db
    db.init_app(app)

    # Register Blueprints
    from .auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .expenses.routes import bp as expenses_bp
    app.register_blueprint(expenses_bp)

    @app.route('/')
    def index():
        return redirect(url_for('expenses.dashboard'))

    return app
