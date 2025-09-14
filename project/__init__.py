from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    from .modules.mod_1_main.routes import main_bp
    from .modules.mod_2_coordenadas.routes import sc_bp
    from .modules.mod_3_retas.routes import retas_bp
    from .modules.mod_4_circunferencia.routes import circ_bp
    from .modules.mod_5_twod.routes import twod_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(sc_bp)
    app.register_blueprint(retas_bp)
    app.register_blueprint(circ_bp)
    app.register_blueprint(twod_bp)

    return app