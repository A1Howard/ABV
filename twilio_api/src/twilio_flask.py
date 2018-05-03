"""This file gives our app the ability to respond to text queries for specific styles of beer."""
import json
from flask import Flask
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
import requests


APP = Flask(__name__)


def get_num_matching_beers(query_results):
    data = query_results
    return len(data)


@APP.route("/", methods=['GET', 'POST'])
def handle_sms():
    """This function provides the response for twilio test message requests."""
    style = request.form['Body']
    query_results = requests.get("http://0.0.0.0:10000/current?style={}".format(style))

    # Handles any situation where an attempt to get a response failed.
    if query_results.status_code != 200:
        response = MessagingResponse()
        response.message("Sorry, I cannot handle your request. Please try again later!")
        return str(response)

    count = get_num_matching_beers(query_results.json())

    response = MessagingResponse()
    if count == 0:
        response.message("Sorry, no results for {}".format(style))
    elif count == 1:
        response.message("There is 1 beer with the style {}".format(style))
    else:
        response.message("There are {} beers with the style {}.".format(count, style))
    return str(response)


if __name__ == "__main__":
    APP.run(debug=True)