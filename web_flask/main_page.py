import random
import string

from flask import Flask, render_template, request, session
from backend.main import create_tweet, create_tweet_hashtags

my_app = Flask(__name__)
my_app.secret_key = ''.join(random.choices(string.ascii_lowercase, k=6))


@my_app.route('/')
def home_page():
    return render_template('login.html')


@my_app.route('/login_user', methods=['POST'])
def login_user():
    # TODO: Add api_key validation before logging in. Otherwise, redirect to error page
    user_api_key = request.form['api_key']
    session['api_key'] = user_api_key
    return render_template('home_page.html')


@my_app.route('/create_content', methods=['POST', 'GET'])
def create_content_request():
    content_type = request.form['content_type']
    print(content_type)
    user_text = request.form['user_text']
    print(user_text)

    posts = ""
    if content_type == "tweet":
        print("Calling create_tweet()")
        posts = create_tweet(user_text)
    elif content_type == "hashtag":
        print("Calling create_tweet_hashtags()")
        posts = create_tweet_hashtags(user_text)

    print(posts)

    # TODO: Render the response within the same form
    return render_template('home_page_with_response.html', posts=posts, content_type=content_type, user_text=user_text)





