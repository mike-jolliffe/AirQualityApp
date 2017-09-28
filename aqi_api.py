import os
import requests


AQI_TOKEN = os.environ['AQI_TOKEN']
LATLONG = os.environ['LATLONG']

class AirQualityReport:
    def __init__(self):
        self.category = { 50: 'Good',
                          100: 'Moderate',
                          150: 'Unhealthy for Sensitive Groups',
                          200: 'Unhealthy',
                          300: 'Very Unhealthy',
                          500: 'Hazardous'
                        }

        self.currentAQI = None
        self.currentCat = None

    def get_aq_data(self):
        '''Sends a get request to aqicn API'''
        params = {
                    'token': AQI_TOKEN,
                    'latlong': LATLONG
        }

        request_url = f'http://api.waqi.info/feed/geo:{LATLONG}/?token={params["token"]}'
        resp = requests.get(request_url)

        return resp.json()

    def build_aq_report(self, json_response):
        '''Grabs the relevant info and leaves the rest. Builds a short report for texting to user.'''
        self.currentAQI = json_response['data']['aqi']
        for key in self.category:
            if self.currentAQI < key:
                self.currentCat = self.category[key]
                break
        return f'Current Air Quality: {self.currentAQI}, {self.currentCat}'

if __name__ == '__main__':
    report = AirQualityReport()
    print(report.build_aq_report(report.get_aq_data()))

    #'feed/:city/?token=:token'
    #http://api.waqi.info/feed/shanghai/?token=demo