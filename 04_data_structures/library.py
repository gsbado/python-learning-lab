# Part 1: List and tuple:

books = [
    ("Harry Potter and the Philosopher's Stone", 1997),
    ("The Shining", 1977),
    ("The Lord of the Rings: The Fellowship of the Ring", 1954),
    ("The Little Prince", 1943),
    ("The Midnight Library", 2020)
]

print("\n*** LIBRARY SERVICE STARTED ***\n")
print("====== BOOK LIST ======\n")

for title, year in books:
    print(f"- Book title: {title} | Publication year: {year}")

oldest_book = books[0]

for book in books:
    if book[1] < oldest_book[1]:
        oldest_book = book

print(f"\nThe oldest book in the list is {oldest_book[0]}, published in {oldest_book[1]}.\n")

# Part 2: Return stack:

book_stack = []

for book in books:
    book_stack.append(book)

print("====== RETURN STACK ======\n")

for _ in range(3):
    processed_book = book_stack.pop()
    print(f"- The book '{processed_book[0]}' has been returned to the library.")

remaining_books = len(book_stack)

print(f"\nThere are still {remaining_books} books left in the return stack.\n")

# Part 3: Service queue:

from collections import deque

service_queue = deque()
service_queue.append("Gabriela")
service_queue.append("Jean")
service_queue.append("Maria Joana")

print("====== SERVICE QUEUE ======\n")

customer = service_queue.popleft()
print(
    f"The customer currently being served is {customer}. "
    f"This customer is first in line because they arrived first."
)

service_queue.append("Ronaldinho Gaúcho")
print(f"A new customer has joined the queue! Look, it's {service_queue[-1]}!")
print("Current service queue:", " -> ".join(service_queue))

while service_queue:
    customer = service_queue.popleft()
    print(f"\nThe next customer being served is {customer}")

    if service_queue:
        print("Current service queue:", " -> ".join(service_queue))
    else:
        print("There are no more customers waiting in line. Let's wait for the next customer to arrive!")
        break

print("\n*** END OF LIBRARY SERVICE ***\n")