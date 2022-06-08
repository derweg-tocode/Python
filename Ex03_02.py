horas = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    fr = float(rate)
    fh = float(horas)
except:
    print("Error, please enter numeric input")
    quit()


if fh > 40:
    print("Overtime")
    reg = fr * fh
    overtime = (fh - 40.0) * 0.5
    print(reg, overtime)
    pay = reg + overtime
else:
    print("Regular")
    pay = fr * fh

print("Pay: ", pay)
