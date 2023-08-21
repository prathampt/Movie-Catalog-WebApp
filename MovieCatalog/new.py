import requests

url = "https://imdb8.p.rapidapi.com/title/find"

querystring = {"q":"pk"}

headers = {
	"X-RapidAPI-Key": "9b38bc633amshb6d25a99648e57fp10e29djsn288b53257477",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

with open("new.json", 'w') as f:
    f.write(str(response.json()))