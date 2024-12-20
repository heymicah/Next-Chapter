import csv,os
from collections import defaultdict, deque
from clean_data import subjects
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": [
            "Content-Type", 
            "Authorization", 
            "Access-Control-Allow-Origin"
        ],
        "supports_credentials": True
    }
})

def list_subjects(subjects):
    i = 1
    count = 0
    for subject in subjects:
        if count < 4:
            print(i, subject, end="\t")
            count += 1
            i+=1
        else:
            count = 0
            print()
        
# create graph based off of passed in subject
def parse_and_create_connections(file_path, excluded_cat):
    book_categories = defaultdict(set)  # Map each category to the titles in it
    book_connections = defaultdict(list)  # Final dictionary of book connections
    book_data = {}  # Store each book's categories for later use

    if not os.path.exists(file_path):
        # print(f"The file path '{file_path}' is not valid.")
        return

    # Read the CSV file
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Use DictReader for column names
        for row in reader:
            title = row['Title'].strip()
            categories = row['Category'].split(',')  # Split categories by commas
            categories = [cat.strip() for cat in categories if cat.strip() != excluded_cat]

            # Save categories for the book
            book_data[title] = categories

            # Map each category to this title
            for category in categories:
                book_categories[category].add(title)

    # Build connections for each book
    for title, categories in book_data.items():
        connected_books = set()
        for category in categories:
            connected_books.update(book_categories[category])  # Add books in the same category
        connected_books.discard(title)  # Remove the book itself from its connections
        book_connections[title] = list(connected_books)

    return book_connections

'''
G

function 1:
- ask user for book title
- ask user for genre 
    * we need to make a list of options (pick 1)

    return title & genre (store in main)
'''
def get_book_info():
    categories = [
        "History", "Biography & Autobiography", "Business & Economics", "Political Science",
        "Romance", "Fantasy", "Fiction", "Science Fiction", "Young Adult Fiction", "Juvenile Nonfiction",
        "Classics", "Action & Adventure", "Mystery & Detective", "Thrillers", "Poetry", "Cooking",
        "Religion", "General"
    ]

    title = input("Enter the book title: ")
    print("")
    print("Select a genre from the following categories:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        genre_input = input("Enter the number corresponding to the genre: ")
        try:
            genre_index = int(genre_input) - 1
            if 0 <= genre_index < len(categories):
                genre = categories[genre_index]
                break
            else:
                print("The genre you selected is not in the provided categories. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the genre.")

    return title, genre



def create_graph(subject):
    file_path = f'data/subjects/{subject}.csv'
    graph = parse_and_create_connections(file_path,subject)
    print('\n')
    if not graph:
        print("Could not create graph. Check file path.")
    else:
        print(f"The {subject} graph has {len(graph)} connections")
    return graph

'''
M

function 3/4:
DFS v BFS search (each of these should return 5 book titles)
'''
def bfs(graph, start_title, max_connections = 5):
    visited = set()
    q = deque()
    q.append(start_title)
    visited.add(start_title)
    connections = []

    while(len(q) != 0 and len(connections) < max_connections):
        front = q.popleft()
        neighbors = graph.get(front, [])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                connections.append(neighbor)

                if len(connections) >= max_connections:
                    break

    return connections

def dfs(graph, start_title, max_connections=5):
    visited = set()
    stack = []
    stack.append(start_title)
    connections = []

    while stack and len(connections) < max_connections:
        front = stack.pop()  

        if front not in visited:
            visited.add(front)
            if front != start_title:
                connections.append(front)

            neighbors = graph.get(front, [])
            stack.extend(neighbors)

    return connections

'''
G

function 5: main ()
-attributes
    title, genre, graph, books (DFS & BFS)
display what the original book title & genre was
call function 2 create the graph
graph passed into functions 3/4
call functions 3/4 (return books
display books
method 1 books:
method 2 books:
* easily display ??

'''

@app.route('/book-connections', methods=['GET'])
def get_book_connections():
    # Retrieve parameters from query string
    title = request.args.get('title')
    genre = request.args.get('genre')

    # Validate parameters
    if not title or not genre:
        return jsonify({
            'error': 'Both title and genre are required'
        }), 400

    try:
        # Create graph based on genre
        graph = create_graph(genre)

        # Perform searches
        dfs_connections = dfs(graph, title)
        bfs_connections = bfs(graph, title)

        return jsonify({
            'title': title,
            'genre': genre,
            'dfs_connections': dfs_connections,
            'bfs_connections': bfs_connections
        })

    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

