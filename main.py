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

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'

graph_config = {
    'id': 'comicg1',
    'name': 'Working at my comic book',
    'unit': 'hours',
    'type': 'float',
    'color': 'ichou'

}

headers = {
    'X-USER-TOKEN': os.environ.get('PIXELA_TOKEN')
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
