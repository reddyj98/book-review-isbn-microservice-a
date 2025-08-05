# Book-Review ISBN Microservice A

## Overview
This microservice is to be implemented alongside the Book Review main program to retrieve book details from the
books API using an ISBN number inputted by the user via the Main Program.

## What can Microservice A do?
- Validate the user ISBN (10 or 13 digits, with the ability to ignore hypens and spaces)
- Fetch title, authors, publisher, published date, description all from Google Books
- Return data as JSON

## Communication Plan

---

## How to Request Data
The microservice provides a GET endpoint to retrieve the book details
by ISBN.

The endpoint URL will look similar to this:

GET http://127.0.0.1:8000/api/book/<isbn>/

Replace the **isbn** value with a valid ISBN-10 or ISBN-13 (hyphens and spaces are allowed and accounted for).

An example request would be the following:
```
import requests

isbn = "9780439023528"
url = "http://127.0.0.1:8000/api/book/{isbn}/"

response = requests.get(url)

# we are assuming that the ISBN is valid with a 200 status code.
print(response.json())
```
For a separate test_client, please refer to the test_client.py file for guidance on how the Microservice works.

## How to Receive Data
The microservice responds with JSON.

The example code to receive and process the response would be the following:
```
import requests

isbn = "9780439023528"
url = "http://127.0.0.1:8000/api/book/{isbn}/"
response = requests.get(url)

if response.status_code = 200:
    data = response.json()
    ... # parse the data 
else:
    print("error!")
```

An example of successful JSON response would be the following:
```
{
    'title': 'The Hunger Games',
    'authors': ['Suzanne Collins'], 
    'publisher': 'Scholastic Inc.', 
    'publishedDate': '2008', 
    'description': 'By winning the Hunger Games, Katniss...
}
```
For a separate test_client, please refer to the test_client.py file for guidance on how the Microservice works.

## UML
<img width="1388" height="939" alt="Image" src="https://github.com/user-attachments/assets/6cf1667f-f3aa-4a45-9e1f-c9c56a25d852" />

---
## Setup
### 1. Clone the repository
```
git clone https://github.com/reddyj98/book-review-isbn-microservice-a
cd book-review-isbn-microservice-a
```
### 2. Create Environment
```
python 3 -m venv .venv
source .venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Run Migration
```
cd isbn_service
python manage.py migrate
```
### 5. Start Server
```
python manage.py runserver
```
