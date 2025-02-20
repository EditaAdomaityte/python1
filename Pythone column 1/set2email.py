# Initialize empty sets
subscribers = set()
unsubscribers = set()

# Function to add an email
def add_email(email, set_name):
    if set_name==subscribers:
        subscribers.add(email)
    else:
        unsubscribers.add(email)
    print(f"Email '{email}' added to {'subscribers' if set_name == subscribers else 'unsubscribers'}.")

# Function to remove an email
def remove_email(email, set_name):
    if email in set_name:
        set_name.remove(email)
        print(f"Email {email} was removed from {set_name}")
    else:
        print(f"Email {email} was not found")


# Function to display emails
def display_emails(set_name):
    print(f"{'subscribers' if set_name == subscribers else 'unsubscribers'}:")
    for _ in set_name:
        print(f"{_}")

# Function to find active subscribers. Return the set.
def find_active_subscribers(set1,set2):
    active=set1.difference(set2)
    print("Active subscribers are:")
    for email in active:
        print(email)
    

# Adding emails to subscribers (notice that some people subscribe more than once)
add_email("user1@example.com", subscribers)
add_email("user3@example.com", subscribers)
add_email("user4@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user6@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user5@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user8@example.com", subscribers)
add_email("user9@example.com", subscribers)
add_email("user2@example.com", subscribers)
add_email("user11@example.com", subscribers)
add_email("user7@example.com", subscribers)
add_email("user10@example.com", subscribers)
add_email("user12@example.com", subscribers)

# Adding emails to unsubscribers
add_email("user6@example.com", unsubscribers)
add_email("user8@example.com", unsubscribers)
add_email("user1@example.com", unsubscribers)
add_email("user10@example.com", unsubscribers)

# Displaying subscribers and unsubscribers
display_emails(subscribers)
display_emails(unsubscribers)

find_active_subscribers(subscribers,unsubscribers)
