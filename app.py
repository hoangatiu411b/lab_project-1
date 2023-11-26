from os import path
from init import app, login_manager, db 

def create_app():

    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import Users
    
    login_manager.login_view = 'auth.login'

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")