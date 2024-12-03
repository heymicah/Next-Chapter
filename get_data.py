import requests
import pandas as pd
import time

# Function to fetch books by genre
def fetch_books_by_genre(genre, max_books=1000):
    base_url = "https://openlibrary.org/subjects/"
    url = f"{base_url}{genre}.json?limit=100"
    books = []

    while len(books) < max_books:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch data for genre {genre}")
            break

        data = response.json()
        works = data.get('works', [])
        for work in works:
            books.append({
                "Title": work.get("title", "Unknown Title"),
                "Genre": genre.title()
            })
            if len(books) >= max_books:
                break
        
        # Check if there's a next page
        next_offset = data.get('offset', 0) + 100
        if next_offset >= data.get('work_count', 0):
            break

        url = f"{base_url}{genre}.json?limit=100&offset={next_offset}"
        time.sleep(1)  # To avoid overloading the server

    return books

# Genres to query
# genres = biography, fantasy, fiction, history, magic, mystery, romance, science_fiction
genres = [
    "magic"
]

# Collect data
all_books = []
for genre in genres:
    print(f"Fetching books for genre: {genre}")
    books = fetch_books_by_genre(genre, max_books=15000)  # Adjust as needed
    all_books.extend(books)

# Save to CSV
df = pd.DataFrame(all_books)
df.to_csv("real_book_titles_and_genres.csv", index=False)
print("Saved book data to 'real_book_titles_and_genres.csv'")