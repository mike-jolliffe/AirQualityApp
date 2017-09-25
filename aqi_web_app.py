from aqi_api import AirQualityReport
from api_keys import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from flask import Flask, make_response, Response, request, render_template
import requests
from twilio.rest import Client

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)

# TODO build the web app so it responds via text with info from aqi_api
# TODO Build Procfile and Requirements.txt
# TODO Deploy to Heroku

@app.route('/inbound_sms', methods=['POST'])
def inbound_sms():
    # Create a quick response
    response = MessagingResponse()
    response.message(f"Checking {request.form['Body']} now. Just a sec...")

    # Grab phone numbers
    from_num = request.form['From']
    to_num = request.form['To']

    client.messages.create(to=from_num, from_=to_num, url=None)#TODO put webapp URL here)

    return str(response)

@app.route('/outbound_sms', methods=['POST'])
def outbound_sms():
    # Hit Air Quality API and return results
    report = AirQualityReport()
    air_quality = report.build_aq_report(report.get_aq_data())
    response = MessagingResponse()
    return response.message(air_quality)

if __name__ == '__main__':
    app.run(debug=True)