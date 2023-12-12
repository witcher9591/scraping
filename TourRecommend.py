import requests

url = "https://tour-recoomender.p.rapidapi.com/search/tour"

# Replace <REQUIRED> with actual latitude, longitude, and radius values
querystring = {
    "lat": "40.7128",  # Replace with actual latitude
    "lng": "-74.0060",  # Replace with actual longitude
    "radius": "10",  # Replace with actual radius in kilometers
    "interest": "museum,bar"
}

headers = {
    "X-RapidAPI-Key": "5734613431msh899da255b1f1548p184441jsna8df727a0eea",
    "X-RapidAPI-Host": "tour-recoomender.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    # Process the JSON response
    tour_recommendations = response.json()
    print(tour_recommendations)
else:
    print("Request failed:", response.status_code)
