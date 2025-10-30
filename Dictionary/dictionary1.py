#Write a Python program to store and manage employee records.

rec = [{
    "e1": {
        "name": "abhi",
        "age": 19,
        "addr": "khmgh",
        "sal": 12
    },
    "e2": {
        "name": "debu",
        "age": 21,
        "addr": "tribeni",
        "sal": 14
    }
}]

while True:
    choice = input("Do you want to add a new employee? (y/n): ").lower()
    if choice != "y":
        break

    existing_keys = list(rec[0].keys())
    next_num = len(existing_keys) + 1
    new_key = f"e{next_num}"

    print(f"\nEntering data for {new_key}:")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    addr = input("Enter address: ")
    sal = int(input("Enter salary: "))

    rec[0][new_key] = {
        "name": name,
        "age": age,
        "addr": addr,
        "sal": sal
    }

    print(f"\n{new_key} added successfully!")

print("\n-- Employee Records --")
for key, value in rec[0].items():
    print(f"{key}: {value}")

print("\n--- Queries ---")
print(f"Employee e1 salary: {rec[0]['e1']['sal']}")
print(f"Employee e2 age: {rec[0]['e2']['age']}")
