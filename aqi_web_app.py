import aqi_api
from aqi_api import AirQualityReport
from flask import Flask, make_response, Response, request, render_template
from twilio.rest import Client

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
app = Flask(__name__)

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

    client.messages.create(to=from_num, from_=to_num, url='https://pdx-air-quality-app.herokuapp.com/outbound_sms')

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