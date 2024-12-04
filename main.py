import csv,os
from collections import defaultdict
from clean_data import subjects

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
def parse_and_create_connections(file_path):
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
            categories = [cat.strip() for cat in categories]  # Clean up whitespace

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


def create_graph(subject):
    file_path = f'data/subjects/{subject}.csv'
    graph = parse_and_create_connections(file_path)
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

'''
G

function 5: main ()

-attributes
    title, genre, graph, books (DFS & BFS)

display what the original book title & genre was

call function 2 create the graph

graph passed into functions 3/4

call functions 3/4 (return books)

display books

method 1 books:

method 2 books:

* easily display ??

'''

# title = "Goat Brothers"
# print(f"{title} is connected to: ")
# for book in list(connections[title])[:5]:
#         print(book)

def main():
    list_subjects(subjects)
    genre = "Young Adult Fiction"
    graph = create_graph(genre)
    
main()