options = [
    ["1", "one"],
    ["2", "two"],
    ["3", "three"],
]

print(sum(options, []))

user = "2"

if user in sum(options, []):
    print("is in")