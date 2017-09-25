import aqi_api

from flask import Flask, make_response, Response, request, render_template
import requests
from twilio.rest import Client

app = Flask(__name__)

# TODO build the web app so it responds via text with info from aqi_api
# TODO Build Procfile and Requirements.txt
# TODO Deploy to Heroku