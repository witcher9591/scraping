import requests

url = "https://travel-places.p.rapidapi.com/"

payload = { "query": """
        query MyQuery {
            getPlaces(lng: 87, lat: 27) {
                distance
                name
                country
                categories
                lng
                lat
                id
            }
        }
    """}
headers = {
	"x-rapidapi-key": "5734613431msh899da255b1f1548p184441jsna8df727a0eea",
	"x-rapidapi-host": "travel-places.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())