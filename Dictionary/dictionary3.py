# Write a Python code to update the net salary of all employees who are living in
# Kolkata or Delhi or Mumbai or Bangalore by increasing 5% over the existing salary.

rec = [{
    "e1": {
        "name": "abhi",
        "age": 19,
        "addr": "khmgh",
        "salary": 12000
    },
    "e2": {
        "name": "xyz",
        "age": 21,
        "addr": "aaa",
        "salary": 14000
    }
}]

while True:
    choice = input("Do you want to add a new employee? (y/n): ").lower()
    if choice != 'y':
        break

    existing_keys = list(rec[0].keys())
    next_num = len(existing_keys) + 1
    new_key = f"e{next_num}"

    print(f"\nEntering data for {new_key}:")
    name = input("Enter name: ")
    addr = input("Enter address: ")
    number = int(input("Enter contact number: "))
    salary = int(input("Enter salary: "))

    rec[0][new_key] = {
        "name": name,
        "addr": addr,
        "number": number,
        "salary": salary
    }

    print(f"\n{new_key} added successfully!")

print("\nEmployees with salary increment:")
flag = 0

for k in rec[0].keys():
    if rec[0][k]["addr"].lower() in ["kolkata", "delhi", "mumbai", "bangalore"]:
        rec[0][k]["salary"] += 0.05 * rec[0][k]["salary"]
        flag = 1
        print(f"Employee {k} ({rec[0][k]['name']}) — New Salary: Rs. {round(rec[0][k]['salary'], 2)}")

if flag == 0:
    print("None")
