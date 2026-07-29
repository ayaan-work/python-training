#Networks fail.
# Servers restart.
# Temporary outages happen.
# Instead of failing immediately:
# Try
# ↓
# Fails
# ↓
# Wait
# ↓
# Try again

#simple retry
import time
import requests

for attempt in range(3):

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        break

    except requests.exceptions.RequestException:

        print("Retrying...")

        time.sleep(2)

#exponential backoff (instead of waiting for same time in every attempt)
import time
import requests

for attempt in range(5):

    try:

        response = requests.get(url)

        response.raise_for_status()

        break

    except requests.exceptions.RequestException:

        wait = 2 ** attempt

        print(f"Waiting {wait} seconds")

        time.sleep(wait)