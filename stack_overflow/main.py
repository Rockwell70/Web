#!/usr/bin/env python3

import requests

response = requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=python&site=stackoverflow")

question = response.json()['items'][0]

title = question['title']
iser_id = question['owner']['user_id']
display_name = question['owner']['display_name']

response = requests.get(f'https://api.stackexchange.com/2.2/users/{iser_id}?order=desc&sort=reputation&site'
                        '=stackoverflow')

creation_date = response.json()['items'][0]['creation_date']
print(f'{display_name} created on {creation_date} asked "{title}"')