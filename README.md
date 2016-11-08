# CSC380

In order to run the current version of the app you probably need to install some things.

***WARNING:
I don't know about windows, but on Linux the virtual environment does not play well (or at all) with spaces in the path,
so if the path you want to run it in is like /home/user/group\ project/ it isn't going to work.  It'll fail when you try to run pip to install the modules needed for the app.

SETUP:
python 3.5 has a virtual environment included, so in the directory you want to run the app from just type:

pyvenv venv

That should set up the virtual environment

To activate the virtual environment source /venv/bin/activate will start it, your propmt will now be preceded by a (venv) letting you know it's active.

To deactivate simply enter:

deactivate

While the virtual environment is activated, enter the following to get the app ready:

pip install --upgrade pip

pip install flask, flask-script, flask-bootstrap, flask-moment, flask-wtf, wtf-forms

If I missed something (you might not need flask-moment tbh) the script will complain when you try to run it.  Just pip install whatever the missing module is and it should work after that.

STARTING THE APP:

type:

python3 spot.py runserver --host 0.0.0.0

then in your browser go to http://localhost:5000

There you can see what's done running.  To kill it, Ctrl-C in the terminal.

TODO:
I think we should just add the probability matices and the song lists directly to the spot.py script.  It'll look like shit, but I think it'll prevent scoping weirdness.

Buttons on the playlist file don't do anything yet.  In the python directory is my stub where I was starting work on those.  At the moment it just picks rows of the probabiliy matrix.  I'm planning on working on this more Wednesday evening.

Data:  I kinda just want to dump data to a csv in the running directory, with the file names being the same as the session handling cookies.  We can just appended data to the csv like Mode(fisher yates vs hmm) and the catalog of skips, thumbs up, thumbs down...etc).  But we can do it however you guys want.  

Server environment isn't ready.  I'm also going to work on this Wednesday evening.  I think (hope) we should be able to wrap everything up Thursday during class.

NOTES:


