from flask import Flask, Response
from flask_basicauth import BasicAuth


app = Flask(__name__)
app.config.from_object('config')
app.static_folder = 'static'

basic_auth = BasicAuth(app)



from app import views





