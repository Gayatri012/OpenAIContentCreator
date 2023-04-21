import openai
from flask import session


def create_tweet(prompt_text):
    print("Inside main.py create_tweet()")
    # Use api_key saved in session.
    openai.api_key = session['api_key']
    prompt_text = "Create a tweet for - " + prompt_text

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.5
    )
    print(response)
    return response


def create_tweet_hashtags(prompt_text):
    print("Inside main.py create_tweet_hashtags()")
    openai.api_key = session['api_key']
    prompt_text = "Create hashtags for the tweet - " + prompt_text

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.5
    )
    print(response)
    return response


# Testing the functions
# if __name__ == '__main__':
    # response = create_tweet_hashtags('Beautiful sunset')
    # response = create_tweet('Image with beautiful sunset and a couple holding hands')

