import requests
import os

USERNAME = 'pluszka'

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

user_params = {
    'token': os.environ.get('PIXELA_TOKEN'),
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#..............................CREATING USER..................................
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT =