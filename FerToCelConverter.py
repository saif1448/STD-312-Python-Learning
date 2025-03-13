

while True:

    inp = input("Enter Ferhenheigh value: ")

    if inp == 'end':
        break

    fer = float(inp)

    cel = (fer - 32) * 5 / 9

    print(f"Celcius: {cel}")