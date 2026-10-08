age = int(input("Enter the age :"))

if age < 18:
    print("Minor")
elif age == 18:
    print("Exactly 18")
else:
    print("Adult")