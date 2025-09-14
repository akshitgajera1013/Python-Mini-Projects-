import requests

query=input("What type of news are you intrested in today :")
api="2fe48e9618c241358dab23820901d0c9"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-08-14&sortBy=publishedAt&apiKey={api}"
r=requests.get(url)

data=r.json()
articles=data["articles"]

for index,i in enumerate(articles):
    print(index+1,i["title"],i["url"])
    print("\n*********************************************************\n")