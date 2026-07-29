#page based 
import requests

page = 1

while True:

    response = requests.get(
        url,
        params={"page": page}
    )

    response.raise_for_status()

    data = response.json()

    users = data["data"]

    if not users:
        break

    for user in users:
        print(user)

    page += 1

#cursor based
cursor = None

while True:

    response = requests.get(
        url,
        params={"cursor": cursor}
    )

    data = response.json()

    for item in data["data"]:
        print(item)

    cursor = data.get("next_cursor")

    if cursor is None:
        break