from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class GenreForm(FlaskForm):
    
    blues = SubmitField('Blues')
    country = SubmitField('Country')
    jazz = SubmitField('Jazz')
    rap = SubmitField('Rap')
    rock = SubmitField('Rock')

class PlayerForm(FlaskForm):

    simFinish = SubmitField('Simulate Finish Track')
    thumbsUp = SubmitField('Like Track')
    thumbsDown = SubmitField('Dislike Track')
    skip = SubmitField('Skip Track')
    

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])	
def index():
    form = GenreForm()
    if form.validate_on_submit():
        if form.blues.data:
            genre = 'blues'
        elif form.country.data:
            genre = 'country'
        elif form.jazz.data:
            genre = 'jazz'
        elif form.rap.data:
            genre = 'rap'
        elif form.rock.data:
            genre = 'rock'

        return redirect(url_for('playlist', genre=genre))
    return render_template('index.html', form=form)

@app.route('/playlist/<genre>', methods=['GET', 'POST'])
def playlist(genre):
    form = PlayerForm()
    if genre == 'blues':
        track = '2xar08Fq5xra2KKZs5Bw9j'
    elif genre == 'country':
        track = '0bsl7pRvv1QAy4QlStDtJC'
    elif genre == 'jazz':
        track = '0vzC63EYz5xG1CH7U9FAqT'
    elif genre  == 'rap':
        track = '2FIUS70tSVIrI6iYDg9rcr'
    elif genre == 'rock':
        track = '31n9wiTDFnCE3WJNcSRqL9'
    if form.validate_on_submit():
        if form.simFinish.data:
            action = "simFinish"
        elif form.thumbsUp.data:
            action = "thumbsUp"
        elif form.thumbsDown.data:
            action = "thumbsDown"
        elif form.skip.data:
            action = "skip"
        return redirect(url_for('playlist'))
    return render_template('playlist.html', form=form, genre=genre, track=track)

if __name__ == '__main__':
    manager.run()
