def computepay(horas, rate):
    print("in computepay ", horas, rate)
    if fh > 40:
        print("Overitime")
        reg = rate * horas
        overtime = (horas - 40.0) * 0.5
        print(reg, overtime)
        pay = reg + overtime
    else:
        print("Regular")
        pay = rate * horas
    print("Pay: ", pay)

horas = input("Enter hours: ")
rate = input("Enter rate: ")
fr = float(rate)
fh = float(horas)

xp = computepay(fh, fr)

