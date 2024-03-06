import requests

api_url = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
    r = requests.get(api_url)
    print(r.status_code)
    print(r.text)

    categories = r.json()
    for category in categories:
        print(category['name'])