""" Main application for twitoff """

# Imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User, Tweet

def create_app():
    """ Creates and configures an instance of a flask app """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route("/")

    def root():
        DB
        DB.drop_all()
        DB.create_all()

        name1 = 'elonmusk'
        user1 = User(name=name1)
        DB.session.add(user1)
        DB.session.commit()

        name2 = 'austen'
        user2 = User(name=name2)
        DB.session.add(user2)
        DB.session.commit()

        for i in range(1, 6):
            text1 = 'sample tweet number' + str(i)
            tweet = Tweet(text=text1)
            DB.session.add(tweet)
            DB.session.commit()

        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    return app
