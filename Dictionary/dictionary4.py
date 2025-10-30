# Q4. 
# Write a Python code to add records of 5 employees, 
# then delete the records of those employees who are not having complete information 
# (i.e., any missing detail like name, address, contact number, or salary).

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
    number = input("Enter contact number: ")
    salary = input("Enter salary: ")

    rec[0][new_key] = {
        "name": name,
        "addr": addr,
        "number": number,
        "salary": salary
    }

    print(f"\n{new_key} added successfully!")

print("\nList of employees with incomplete data to be deleted:")
flag = 0
to_delete = []

for k in list(rec[0].keys()):
    emp = rec[0][k]
    if not emp.get("name") or not emp.get("addr") or not emp.get("number") or not emp.get("salary"):
        to_delete.append(k)
        flag = 1

for k in to_delete:
    del rec[0][k]
    print(f"Employee {k}")

if flag == 0:
    print("None")
else:
    print("\nGiven employees have been deleted from the records successfully!")

print("\nThe new modified records of employees:")
for k, emp in rec[0].items():
    print(f"Employee {k}:")
    print(f"  Name: {emp['name']}")
    print(f"  Address: {emp['addr']}")
    print(f"  Phone number: {emp.get('number', 'N/A')}")
    print(f"  Salary: {emp['salary']}\n")
