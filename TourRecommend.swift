import requests

url = "https://tour-recoomender.p.rapidapi.com/search/tour"

querystring = {"lat":"<REQUIRED>","lng":"<REQUIRED>","radius":"<REQUIRED>","interest":"museum,bar"}

headers = {
	"X-RapidAPI-Key": "5734613431msh899da255b1f1548p184441jsna8df727a0eea",
	"X-RapidAPI-Host": "tour-recoomender.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())