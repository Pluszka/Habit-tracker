import requests
import os
import datetime as dt

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

#.............................CREATING GRAPH..........................

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH1_ID = 'comicg1'

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

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

#..........................ADDING NEW PIXEL.....................................

PIXEL_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH1_ID}'

# current_data = dt.datetime(year=2022, month=2, day=12)
current_data = dt.date.today()

new_pixel = {
    'date': current_data.strftime('%Y%m%d'),
    'quantity': input('How many time you spent today?'),
}
# response = requests.post(url=PIXEL_ENDPOINT, json=new_pixel, headers=headers)
# print(response.text)


#.............................UPDATE PIXEL..............................

# day_to_update = current_data.strftime('%Y%m%d')
#
#
# UPDATE_ENDPOINT = f'{PIXEL_ENDPOINT}/{day_to_update}'
#
# update_config = {
#     'quantity': input('How many time you spent today?')
# }
#
# # response = requests.put(url=UPDATE_ENDPOINT, json=update_config, headers=headers)
# # print(response.text)
#
# #........................DELETE PIXEL....................................
#
# day_to_del = dt.datetime(year=2022, month=2, day=12).strftime('%Y%m%d')
#
# DEL_ENDPOINT = f'{PIXEL_ENDPOINT}/{day_to_del}'

# response = requests.delete(url=DEL_ENDPOINT, headers=headers)
# print(response.text)
