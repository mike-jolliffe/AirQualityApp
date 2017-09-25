#TODO build an api get request for the following website: http://aqicn.org/api/

import requests
from api_keys import AQI_TOKEN

def get_aq_data(city):
    '''Sends a get request to aqicn API'''
    params = {
                'token': AQI_TOKEN, #TODO get api token, store in gitignore file
                'city': city
    }

    request_url = f'http://api.waqi.info/feed/{params["city"]}/?token={params["token"]}'
    resp = requests.get(request_url)

    return resp.json()

if __name__ == '__main__':
    print(get_aq_data('portland'))

    #'feed/:city/?token=:token'
    #http://api.waqi.info/feed/shanghai/?token=demo