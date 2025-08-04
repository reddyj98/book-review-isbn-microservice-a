# Book-Review ISBN Microservice A

## Overview
This microservice is to be implemented alongside the Book Review main program to retrieve book details from the
books API using an ISBN number inputted by the user via the Main Program.

## What can Microservice A do?
- Validate the user ISBN (10 or 13 digits, with the ability to ignore hypens and spaces)
- Fetch title, authors, publisher, published date, description all from Google Books
- Return data as JSON

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
