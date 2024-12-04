from collections import defaultdict
import requests
import json
import csv

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJzaW9uIjoiNiIsImlkIjoyMDEzNiwibG9nZ2VkSW4iOnRydWUsInN1YiI6IjIwMTM2IiwiaWF0IjoxNzI5NDY2NjQ5LCJleHAiOjE3NjA5MTY1NDksImh0dHBzOi8vaGFzdXJhLmlvL2p3dC9jbGFpbXMiOnsieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJ1c2VyIl0sIngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1yb2xlIjoidXNlciIsIlgtaGFzdXJhLXVzZXItaWQiOiIyMDEzNiJ9fQ.45Ahr_RPsNJpq1174_66rFUBnCIoTVCOvzBR4frzBro"
TITLE = "Pride and Prejudice"

def fetch_graphql(operations_doc, operation_name, variables):
    url = "https://api.hardcover.app/v1/graphql"
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
    payload = {
        "query": operations_doc,
        "variables": variables,
        "operationName": operation_name
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

def fetch_my_query(title):
    operations_doc = f"""
    query MyQuery {{
        search(query: "{title}") {{
        results
        }}
    }}
    """
    response = fetch_graphql(
        operations_doc,
        "MyQuery",
        {}
    )
    
    if response is None:
        print(f"Error fetching data for title: {title}")
        return None
    return response


# def extract_moods(title):
#     response = fetch_my_query(title)
#     if response is None or "errors" in response:
#         return None
#     try:
#         moods = response["data"]["search"]["results"]["hits"][0]["document"]["moods"]
#         print(moods)
#         return moods
#     except (KeyError, IndexError):
#         return None

# genres = ["fantasy","fiction","romance","magic","mystery","history","science_fiction"]
# subjects = ["Juvenile fiction", "Children's literature", "Children's fiction", "fairy tales", "politics"]
    
def book_titles():
    titles=[]
    # Open the file
    with open('data/books.csv', mode='r', encoding='utf-8', errors='ignore') as file:
        my_file = csv.reader(file, delimiter=',')

        # skip first line
        next(my_file)

        for row in my_file:
            titles.append(row[0])
    return titles

# Function to parse the subjects from a string
def get_subjects(line, subjects):
    # Split the string by commas and strip whitespace
    all_subjects = [subject.strip().lower() for subject in line.split(",")]
    # Filter for relevant subjects
    return set(subject for subject in all_subjects if subject in map(str.lower, subjects))

def create_book_map(csv_file_path, subjects):
    book_map = defaultdict(list)
    books = {}  # Temporary storage for book subjects
    titles = []

    # Read the CSV file
    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            # Assuming format: Title, Genre, Subjects
            title = line[0].strip()
            titles.append(title)
            relevant_subjects = get_subjects(line[2], subjects)
            books[title] = relevant_subjects

    # Build connections
    for book1, subjects1 in books.items():
        for book2, subjects2 in books.items():
            if book1 != book2 and subjects1 & subjects2:  # Check for shared subjects
                book_map[book1].append(book2)

    return book_map





def main():
    subjects = [
    "Fiction", "Drama", "Historical fiction", "Coming of age", "Crime", "Mystery",
    "Children", "Juvenile fiction", "biography", "fiction", "history", 
    "magic", "mystery", "science_fiction"]

    graph = create_book_map(".csv", subjects)
    print(len(graph))
    
   

    

main()