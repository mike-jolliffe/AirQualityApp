import aqi_api
from aqi_api import AirQualityReport
from flask import Flask, make_response, Response, request
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)

@app.route('/inbound_sms', methods=['GET', 'POST'])
def inbound_sms():

    # Grab phone numbers
    from_num = request.form['From']
    to_num = request.form['To']

    # Send a quick follow-up message so user knows we're working on it
    client.messages.create(to=from_num, from_=to_num,
                           body="Checking air quality for your location. Just a sec...")

    # Hit Air Quality API and return results
    report = AirQualityReport()
    air_quality = report.build_aq_report(report.get_aq_data())

    # Send info on current air quality
    client.messages.create(to=from_num, from_=to_num,
                           body=air_quality)

if __name__ == '__main__':
    app.run(debug=True)