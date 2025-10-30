#Write a Python program to display employee names living in a specific location.

rec = [{
    "e1": {
        "name": "abhi",
        "age": 19,
        "addr": "khmgh",
        "sal": 12
    },
    "e2": {
        "name": "xyz",
        "age": 21,
        "addr": "aaa",
        "sal": 14
    }
}]

ekeys = len(list(rec[0].keys()))
loc = input("Enter specific location: ").strip()

print("Employees living at the specific location:")
flag = 0

for i in range(ekeys):
    eno = f"e{i+1}"
    if rec[0][eno]["addr"] == loc:
        print(f"Employee {eno} - {rec[0][eno]['name']}")
        flag = 1

if flag == 0:
    print("NONE")
