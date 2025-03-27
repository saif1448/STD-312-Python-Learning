from Task11Module import convert_fer_to_cel, convert_daily_fer_temp

while True:
    output = convert_daily_fer_temp()
    if output == False:
        print("The program has been ended!")
        break
    else:
        continue
