calc = input("enter v, i, r: ")
volt = 0
ampere = 0
ohms = 0

# def calculate(calc):
try:
    if calc == "v":
        volt = 0
        ampere = float(input("Enter Current: "))
        ohms = float(input("Enter Resistance: "))

        print(ampere * ohms)

    elif calc == "i":
        ampere = 0
        volt = float(input("Enter Voltage "))
        ohms = float(input("Enter Resistance: "))

        print(volt / ohms)

    elif calc == "r":
        ohms = 0
        volt = float(input("Enter Voltage "))
        ampere = float(input("Enter Current: "))
        print(volt / ampere)

except ValueError:
    print("Please enter v i or r")
