'''
1. Tuple Mastery in Python
Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
The function should format and return a string that lists each itinerary. 
For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`,
 the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"

'''

# Define a function to format itineraries
def format_itineraries(traveler_name, origin, destination):
    # Create a string to store the formatted itinerary
    print(f"Itinerary: {traveler_name} - From {origin} to {destination}")
# Define a list of itineraries
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
# Print out each itinerary
for i, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
    print(f"Itinerary {i}:")
    print(format_itineraries(traveler_name, origin, destination))