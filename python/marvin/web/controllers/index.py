from flask import current_app, Blueprint, render_template, session as current_session
from flask.ext.classy import FlaskView, route
from marvin.tools.cube import Cube
from marvin import config, session, datadb
index = Blueprint("index_page", __name__)


class Marvin(FlaskView):
    route_base = '/'

    def index(self):
        index = {}
        index['title'] = 'Marvin'
        index['intro'] = 'Welcome to Marvin'
        config.drpver = 'v1_5_1'
        cube = Cube(mangaid='1-209232')
        index['cube'] = cube
        try:
            spectrum = cube.getSpectrum(x=1, y=2)
        except Exception as e:
            spectrum = 'Could not get spectrum: {0}'.format(e)

        index['spectra'] = spectrum
        return render_template("index.html", **index)

    def quote(self):
        return 'getting quote'

    def get(self, id):
        return 'getting id {0}'.format(id)

    @route('/test/')
    def test(self):
        return 'new test'

    def database(self):
        onecube = session.query(datadb.Cube).first()
        return str(onecube.plate)


Marvin.register(index)
