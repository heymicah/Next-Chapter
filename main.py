import requests

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJzaW9uIjoiNiIsImlkIjoyMDEzNiwibG9nZ2VkSW4iOnRydWUsInN1YiI6IjIwMTM2IiwiaWF0IjoxNzI5NDY2NjQ5LCJleHAiOjE3NjA5MTY1NDksImh0dHBzOi8vaGFzdXJhLmlvL2p3dC9jbGFpbXMiOnsieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJ1c2VyIl0sIngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1yb2xlIjoidXNlciIsIlgtaGFzdXJhLXVzZXItaWQiOiIyMDEzNiJ9fQ.45Ahr_RPsNJpq1174_66rFUBnCIoTVCOvzBR4frzBro"
BASE_URL = "https://api.hardcover.com/search"
ISBN = "9780140449136"  # Replace with the actual ISBN

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

params = {
    "isbn": ISBN
}

response = requests.get(BASE_URL, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    if data.get("results"):
        for book in data["results"]:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genres: {book.get('genres', 'N/A')}")
    else:
        print("No books found for this ISBN.")
else:
    print(f"Error: {response.status_code} - {response.text}")