import requests
import time
base_url = 'http://127.0.0.1:8000/api/book/'


while True:
    isbn = input("Enter ISBN:").strip()
    isbn_url = f"{base_url}{isbn}"

    print(f"Getting book details for ISBN: {isbn}")
    count = 0
    while count < 3:
        time.sleep(1)
        count += 1
        print(".")

    print(f"Sending GET request to {isbn_url}")
    count = 0
    while count < 3:
        time.sleep(1)
        count += 1
        print(".")


    try:
        response = requests.get(isbn_url)
        print(f"Received HTTP Status: {response.status_code}")

        if response.status_code == 200:
            count = 0
            while count < 3:
                time.sleep(1)
                count += 1
                print(".")
            print("Book details retrieved!:")
            print(response.json())
        else:
            try:
                error_details = response.json()
            except ValueError:
                error_details = {"error": response.text}
            print("Error from microservice:", error_details)

    except requests.exceptions.RequestException as e:
        print(f"Exception while getting book details: {e}")

    print("")
    again = input("Would you like to try again? (y/n): ").strip().lower()
    if again != 'y':
        print("Bye! Exiting...")
        break