from flask import Flask, render_template, request, redirect, flash
import security_info
import json
import randomtweets
import random


app = Flask(__name__)
app.secret_key = security_info.APP_SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    error = ""
    username = ""
    tweet_mimic = ""
    if request.method == "POST":
        username = request.form["username"]
        if username == "":
            error = "Please search for a @username first" 
        else:
            my_tweets = randomtweets.search_tweets(username)
            mimic_dict = randomtweets.mimic_tweets(my_tweets)
            word = random.choice(my_tweets).split()[0]
            tweet_mimic = randomtweets.print_mimic(mimic_dict, word) 
    return render_template('index.html', username=username, tweet=tweet_mimic, error=error)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)