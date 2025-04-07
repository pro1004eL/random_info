import requests

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    if users[0]['name'] == 'Leanne Graham':
        print(f"The first user is Leanne Graham. \nDetails: {users[0]}")
    else:
        print("The first user is NOT Leanne Graham.")

else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
    