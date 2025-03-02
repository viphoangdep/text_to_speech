from flask import Flask

def create_app():
    app = Flask(__name__)
    
    
    from .controllers.routes import convert_bp
    app.register_blueprint(convert_bp)
    
    return app
