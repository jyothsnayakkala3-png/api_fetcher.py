import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def display_users(users):
    if not users:
        print("No users found.")
        return

    print("\nUser Details")
    print("-" * 50)
    for user in users:
        print(f"ID      : {user['id']}")
        print(f"Name    : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email   : {user['email']}")
        print(f"City    : {user['address']['city']}")
        print("-" * 50)

def search_users(users, keyword):
    keyword = keyword.lower()
    return [
        user for user in users
        if keyword in user["name"].lower()
        or keyword in user["username"].lower()
        or keyword in user["email"].lower()
    ]

def main():
    users = fetch_data()

    if not users:
        return

    display_users(users)

    while True:
        keyword = input("\nEnter name, username, or email to search (or 'exit'): ")

        if keyword.lower() == "exit":
            print("Goodbye!")
            break

        results = search_users(users, keyword)
        display_users(results)

if __name__ == "__main__":
    main()
