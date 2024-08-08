'''
Python Data Structure Challenges in Real-World Scenarios
Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
'''

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Define a function to add a new book to the library
def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Added '{title}' by {author}to the library.")
    else:
              print(f"'{title}' by {author} is already in the library.")

# Add some new books
add_book(library,"The Alchemist", "Paulo Coelho")
add_book(library,"1984", "George Orwell")  # Duplicate book
add_book(library,"Hatchet", "Gary Paulsen")

# Print the updated library
print("Updated Library:")
for book in library:
    print(book)
