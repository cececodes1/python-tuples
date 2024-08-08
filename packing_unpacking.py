'''
Mastering Tuple Packing and Unpacking in Python
Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
'''

def print_orders(orders):
    for order in orders:
        name = order[0]
        product = order[1]
        quantity = order[2]
        print("Order Details:")
        print("Customer: " + name)
        print("Product: " + product)
        print("Quantity: " + str(quantity))
        print()

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "Phone", 3),
    ("David", "Tablet", 1),
]

print_orders(orders)