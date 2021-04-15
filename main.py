import requests
from secrets import nutritionix_key, nutritionix_id, headers
import datetime

now = datetime.datetime.now()
today = now.today()

head = {
    'x-app-id': nutritionix_id,
    'x-app-key': nutritionix_key
}
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/80d472412da841101008ec637a12804d/myWorkoutsPython/workouts'

body = {
    'query': input('Tell me which exercises you did: ')
}
response = requests.post(nutritionix_endpoint, json=body, headers=head)

data = response.json()['exercises']

for elem in data:
    sheety_post = {
        'workout': {
            'name': 'Kade Williams',
            'email': 'w0nderm4n11@gmail.com',
            'date': today.strftime('%d/%m/%Y'),
            'time': now.strftime('%X'),
            'exercise': elem['name'].title(),
            'duration': elem['duration_min'],
            'calories': elem['nf_calories']
        }
    }

    response = requests.post(sheety_endpoint, json=sheety_post, headers=headers)
print(response.json())
