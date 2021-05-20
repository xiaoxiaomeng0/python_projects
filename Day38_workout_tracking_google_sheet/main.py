import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
# print(APP_ID, API_KEY)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

# exercise_input = input("What did you exercise today? ")

request_body = {
    "query": "I ran 4000 feet and jumped 500 meters",
    "gender": "female",
    "weight_kg": "72.5",
    "height_cm": "167.64",
    "age": "30",
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
exercise_response = requests.post(url=exercise_endpoint, json=request_body, headers=headers)

# data = [new_item for item in response.text["exercises"].]
data_list = exercise_response.json()["exercises"]
# print(exercise_response.json())
# print(data_list)
# if len(data_list) == 0:
#     pass
# else:
#     foo = {}
#     for key in data_list[0].keys():
#         foo[key] = [item[key] for item in data_list]
#     print(foo)

# keys = ['tag_id', 'duration_min', 'user_input']
# data_list_filtered = [{key: item[key] for key in keys} for item in data_list]
# print(data_list_filtered)
    # print({key: [item[key] for item in data_list]})

# exercise_list = []

sheety_url = "https://api.sheety.co/42249d81205f4e5645dfcd92aee2ca5b/workoutTracking/workouts"
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": os.environ.get("SHEETY_AUTH")
}

for data in data_list:
    body = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data["user_input"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheety_url, json=body, headers=sheety_headers)
    print(sheet_response.text)
