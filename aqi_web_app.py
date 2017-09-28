import aqi_api
from aqi_api import AirQualityReport
from flask import Flask, make_response, Response, request, redirect, url_for
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

AQI_TOKEN = os.environ['AQI_TOKEN']
LATLONG = os.environ['LATLONG']


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)

@app.route('/inbound_sms', methods=['GET', 'POST'])
def inbound_sms():
    # Create a quick response
    response = MessagingResponse()

    # Grab phone numbers
    from_num = request.form['From']
    to_num = request.form['To']

    client.messages.create(to=from_num, from_=to_num,
                           body="Checking air quality for your location now. Just a sec...")

    response_body = redirect(url_for('outbound_sms'))
    response.message(response_body)

    return str(response)

@app.route('/outbound_sms', methods=['GET', 'POST'])
def outbound_sms():
    # Hit Air Quality API and return results
    report = AirQualityReport()
    air_quality = report.build_aq_report(report.get_aq_data())
    response = MessagingResponse()
    return response.message(air_quality)

if __name__ == '__main__':
    app.run(debug=True)