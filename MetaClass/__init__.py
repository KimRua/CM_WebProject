from . import fileUpload
from . import object
# from . import login

def setUp(app):
    app.register_blueprint(object.app)
    app.register_blueprint(fileUpload.app)
    # app.register_blueprint(login.app)
