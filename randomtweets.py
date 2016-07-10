# encoding: utf-8
from security_info import *
import subprocess
import requests 
from requests_oauthlib import OAuth1, OAuth1Session
import os.path
import random

URL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
API_KEY = TWITTER_API_KEY 
API_SECRET = TWITTER_API_SECRET
my_tweets = []
 

def search_tweets(username=None):
    auth = OAuth1(API_KEY, API_SECRET)
    if username is None:
        username = raw_input("Please type the @username that you want to search: ")
    params = {"screen_name": username, "count": 200, "include_rts": False}
    response = requests.get(URL, params=params, auth=auth)
    search_results = response.json()
    my_tweets = []
    for tweet in search_results:
        my_tweets.append(tweet["text"])
    return my_tweets


def mimic_tweets(my_tweets):
    mimic_tweets = {}
    for tweet in my_tweets:
        prev_word = ""
        for word in tweet.split():
            if not prev_word in mimic_tweets:
                mimic_tweets[prev_word] = [word]
            else:
                mimic_tweets[prev_word].append(word)
            prev_word = word 
    return mimic_tweets


def print_mimic(mimic_dict, word):
    tweet = ""

    while len(tweet + " " + word) <= 140:
        tweet = tweet +" " + word
        nexts = mimic_dict.get(word)
        if not nexts:
            nexts = mimic_dict[""] 
        word = random.choice(nexts).lower()

    print len(tweet)
    return tweet 


def main():
    
    my_tweets = search_tweets()
    mimic_dict = mimic_tweets(my_tweets)
    word = random.choice(my_tweets).split()[0]
    print print_mimic(mimic_dict, word)


if __name__ == '__main__':
    main()