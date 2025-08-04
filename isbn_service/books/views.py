import requests
from django.http import JsonResponse

def get_book_details(request, isbn):
    # Used to make ISBN plain digits for data validation.
    plain_isbn = isbn.replace('-', '').replace('.', '').replace(' ','')

    # Data validation that ISBN is a digit and is either 10 or 13 digits long.
    if not plain_isbn.isdigit() or len(plain_isbn) not in [10,13]:
        return JsonResponse({"error": "Invalid ISBN. Please enter 10 or 13 digits."})

    # Google Books API that is built with the ISBN input.
    url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{plain_isbn}"
    response = requests.get(url)

    # If API response is not successful, return 503 error
    if response.status_code != 200:
        return JsonResponse({"error": "Failed to retrieve book details."}, status=503)

    # Retrieved data parse
    data = response.json()

    # Returns error if a book is not found in the Google Books database
    if data.get("items", 0) == 0:
        return JsonResponse({"error": "Book not found."}, status=404)

    # Returns first item in volumeInfo
    book_details = data["items"][0].get("volumeInfo", {})
    result = {
        'title': book_details.get("title"),
        'authors': book_details.get("authors", []),
        'publisher': book_details.get("publisher"),
        'publishedDate': book_details.get("publishedDate"),
        'description': book_details.get("description")
    }

    # Return books details as JSON format
    return JsonResponse(result)