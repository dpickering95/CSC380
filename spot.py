from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
playlist1 = pl1.pl1()
playlist2 = pl2.pl2()
playlist3 = pl3.pl3()
playlist4 = pl4.pl4()
playlist5 = pl5.pl5()
playlist6 = pl6.pl6()
playlist7 = pl7.pl7()
playlist8 = pl8.pl8()
playlist9 = pl9.pl9()



class GenreForm(FlaskForm):
    
    pl1 = SubmitField('"Throwing Stones" -- Grateful Dead')
    pl2 = SubmitField('"Head Like a Hole" -- Nine Inch Nails')
    pl3 = SubmitField('"Season 2 Episode 3" -- Glass Animals')
    pl4 = SubmitField('"Lord Willin\'" -- Logic')
    pl5 = SubmitField('"Life Itself" -- Glass Animals')
    pl6 = SubmitField('"Sense" -- King Gizzard & The Lizard Wizard')
    pl7 = SubmitField('"Daddy Issues" -- The Neighbourhood')
    pl8 = SubmitField('"IV. Sweatpants" -- Childish Gambino')
    pl9 = SubmitField('"Jude Law and a Semester Abroad" -- Brand New')


class PlayerForm(FlaskForm):

    simFinish = SubmitField('Simulate Finish Track')
    thumbsUp = SubmitField('Like Track')
    thumbsDown = SubmitField('Dislike Track')
    skip = SubmitField('Skip Track')
    
class FisherForm(FlaskForm):

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
        if form.pl1.data:
            genre = 'playlist1'
        elif form.pl2.data:
            genre = 'playlist2'
        elif form.pl3.data:
            genre = 'playlist3'
        elif form.pl4.data:
            genre = 'playlist4'
        elif form.pl5.data:
            genre = 'playlist5'
        elif form.pl6.data:
            genre = 'playlist6'
        elif form.pl7.data:
            genre = 'playlist7'
        elif form.pl8.data:
            genre = 'playlist8'
        elif form.pl9.data:
            genre = 'playlist9'

        return redirect(url_for('playlist', genre=genre))
    return render_template('index.html', form=form)

@app.route('/playlist/<genre>', methods=['GET','POST'])
def playlist(genre):
    form = PlayerForm()
    if genre == 'playlist1':
        track = playlist1.get_current_track()
    elif genre == 'playlist2':
        track = playlist2.get_current_track()
    elif genre == 'playlist3':
        track = playlist3.get_current_track()
    elif genre == 'playlist4':
        track = playlist4.get_current_track()
    elif genre == 'playlist5':
        track = playlist5.get_current_track()
    elif genre == 'playlist6':
        track = playlist6.get_current_track()
    elif genre == 'playlist7':
        track = playlist7.get_current_track()
    elif genre == 'playlist8':
        track = playlist8.get_current_track()
    elif genre == 'playlist9':
        track = playlist9.get_current_track()
    if form.validate_on_submit():
        if form.simFinish.data:
            if genre == 'playlist1':
                playlist1.next_track('finish')
                track = playlist1.get_current_track()
                f = open('playlist1.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist2':
                playlist2.next_track('finish')
                track = playlist2.get_current_track()
                f = open('playlist2.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist3':
                playlist3.next_track('finish')
                track = playlist3.get_current_track()
                f = open('playlist3.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist4':
                playlist4.next_track('finish')
                track = playlist4.get_current_track()
                f = open('playlist4.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist5':
                playlist5.next_track('finish')
                track = playlist5.get_current_track()
                f = open('playlist5.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist6':
                playlist6.next_track('finish')
                track = playlist6.get_current_track()
                f = open('playlist6.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist7':
                playlist7.next_track('finish')
                track = playlist7.get_current_track()
                f = open('playlist7.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist8':
                playlist8.next_track('finish')
                track = playlist8.get_current_track()
                f = open('playlist8.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist9':
                playlist9.next_track('finish')
                track = playlist9.get_current_track()
                f = open('playlist9.csv', 'a')
                f.write('{}, simFinish, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)

        elif form.thumbsUp.data:
            if genre == 'playlist1':
                playlist1.next_track('like')
                track = playlist1.get_current_track()
                f = open('playlist1.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist2':
                playlist2.next_track('like')
                track = playlist2.get_current_track()
                f = open('playlist2.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist3':
                playlist3.next_track('like')
                track = playlist3.get_current_track()
                f = open('playlist3.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist4':
                playlist4.next_track('like')
                track = playlist4.get_current_track()
                f = open('playlist4.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist5':
                playlist5.next_track('like')
                track = playlist5.get_current_track()
                f = open('playlist5.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist6':
                playlist6.next_track('like')
                track = playlist6.get_current_track()
                f = open('playlist6.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist7':
                playlist7.next_track('like')
                track = playlist7.get_current_track()
                f = open('playlist7.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist8':
                playlist8.next_track('like')
                track = playlist8.get_current_track()
                f = open('playlist8.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist9':
                playlist9.next_track('like')
                track = playlist9.get_current_track()
                f = open('playlist9.csv', 'a')
                f.write('{}, like, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)

        elif form.thumbsDown.data:
            if genre == 'playlist1':
                playlist1.next_track('dislike')
                track = playlist1.get_current_track()
                f = open('playlist1.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist2':
                playlist2.next_track('dislike')
                track = playlist2.get_current_track()
                f = open('playlist2.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist3':
                playlist3.next_track('dislike')
                track = playlist3.get_current_track()
                f = open('playlist3.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist4':
                playlist4.next_track('dislike')
                track = playlist4.get_current_track()
                f = open('playlist4.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist5':
                playlist5.next_track('dislike')
                track = playlist5.get_current_track()
                f = open('playlist5.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist6':
                playlist6.next_track('dislike')
                track = playlist6.get_current_track()
                f = open('playlist6.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist7':
                playlist7.next_track('dislike')
                track = playlist7.get_current_track()
                f = open('playlist7.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist8':
                playlist8.next_track('dislike')
                track = playlist8.get_current_track()
                f = open('playlist8.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist9':
                playlist9.next_track('dislike')
                track = playlist9.get_current_track()
                f = open('playlist9.csv', 'a')
                f.write('{}, dislike, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)

        elif form.skip.data:
            if genre == 'playlist1':
                playlist1.next_track('skip')
                track = playlist1.get_current_track()
                f = open('playlist1.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist2':
                playlist2.next_track('skip')
                track = playlist2.get_current_track()
                f = open('playlist2.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist3':
                playlist3.next_track('skip')
                track = playlist3.get_current_track()
                f = open('playlist3.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist4':
                playlist4.next_track('skip')
                track = playlist4.get_current_track()
                f = open('playlist4.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist5':
                playlist5.next_track('skip')
                track = playlist5.get_current_track()
                f = open('playlist5.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist6':
                playlist6.next_track('skip')
                track = playlist6.get_current_track()
                f = open('playlist6.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist7':
                playlist7.next_track('skip')
                track = playlist7.get_current_track()
                f = open('playlist7.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist8':
                playlist8.next_track('skip')
                track = playlist8.get_current_track()
                f = open('playlist8.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
            elif genre == 'playlist9':
                playlist9.next_track('skip')
                track = playlist9.get_current_track()
                f = open('playlist9.csv', 'a')
                f.write('{}, skip, {}, {}\n'.format(str(os.getpid()), str(track), datetime.now().strftime('%m/%d/%Y - %H:%M:%S')))
                f.close()
                return render_template('playlist.html', form=form, genre=genre, track=track)
        return redirect(url_for('playlist'))
    return render_template('playlist.html', form=form, genre=genre, track=track)

if __name__ == '__main__':
    manager.run()
