import csv
from collections import Counter

'''
BooksDataset.csv

https://www.kaggle.com/datasets/elvinrustam/books-dataset

This dataset comprises information scraped from wonderbk.com, a popular online bookstore. T
he dataset contains details of 103,063 books, with key attributes such as 
title, authors, description, category, publisher, starting price, and publish date.

'''

def clean_data():
    # Define the input and output file paths
    input_file_path = 'data/BooksDataset.csv'
    output_file_path = 'data/cleaned_books.csv'

    # Open the input file and write only the Title and Category columns to the output file
    with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        
        # Write the header for the new CSV file
        writer.writerow(['Title', 'Category'])
        
        # Process each row and write only Title and Category
        for row in reader:
            title = row['Title'].strip()
            category = row['Category'].strip()
            if not category:
                category = "General"
            writer.writerow([title, category])

'''
call clean data function:
take the BooksDataset.csv and extract the title and subjects,
stored in new file cleaned_books.csv

clean_data()
'''

def get_subcounts():
    file_path = 'data/cleaned_books.csv'
    subject_counts = Counter()  # Initialize a Counter to track subject frequencies

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Use DictReader for column names
        for row in reader:
            categories = row['Category'].split(',')  # Split categories by commas
            categories = [cat.strip() for cat in categories]  # Clean up whitespace
            subject_counts.update(categories)  # Update counts for each category

    return subject_counts

'''
# call get_subcounts
subject_counts = get_subcounts()

# Print all unique subjects and their counts
for subject, count in subject_counts.items():
    if count > 2000:
        print(f"{subject}: {count}")
'''

# categories then cleaned and reduced
subjects = ["History","Biography & Autobiography", 
            "Business & Economics","Political Science",
            "Romance",
            "Fantasy",
            "Fiction","Science Fiction","Young Adult Fiction", "Juvenile Nonfiction",
            "Classics",
            "Action & Adventure", "Mystery & Detective","Thrillers",
            "Poetry", "Cooking", "Religion",
            "General"]

# create a file for each subject
def seperate_data(subject):
    input_file = 'data/cleaned_books.csv'
    output_file = f'data/subjects/{subject}.csv'
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile, fieldnames=['Title', 'Subjects'])
        writer = csv.writer(outfile)

        # Write the header for the output file
        writer.writerow(['Title', 'Category'])

        # Iterate through each row in the input file
        for row in reader:
            # Extract and clean the subjects
            subjects = [subject.strip() for subject in row['Subjects'].split(',')]
            
            # Check if the target subject is in the subjects list
            if subject in subjects:
                writer.writerow([row['Title'], row['Subjects']])

'''
create seperate csv files for each book subject (genre)

for subject in subjects:
    seperate_data(subject)
'''