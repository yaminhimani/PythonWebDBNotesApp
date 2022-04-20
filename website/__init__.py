from flask import Flask

#initalize app for creation
#Register route blueprints here 

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'cajipohcapeihfnep'
  
  from .views import views
  from .auth import auth
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/')

  return app 