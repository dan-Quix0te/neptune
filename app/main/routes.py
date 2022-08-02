from app.main import main
from flask import render_template
import os
import subprocess




@main.route('/')
def index():
    return render_template('index.html', title='Home')

@main.route('/ingest')
def ingest():
    return render_template('ingest.html', title='ingest')



#@app.route('/schedule')
#def schedule():
#    return render_template('schedule.html', title='schedule')
#
#@app.route('/mixer')
#def mixer():
#    return render_template('mixer.html', title='mixer')
#
#@app.route('/record')
#def record():
#    return render_template('record.html', title='record')
#
#@app.route('/archive')
#def archive():
#    return render_template('archive.html', title='archive')
#
#@app.route('/delivery')
#def delivery():
#    return render_template('delivery.html', title='delivery')
#
#
#
