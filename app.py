from app_module import create_app
from routes.message_routes import message_bp

app = create_app()

app.register_blueprint(message_bp, url_prefix = '/messages')

if __name__ == '__main__':
    app.debug = True
    app.run()
