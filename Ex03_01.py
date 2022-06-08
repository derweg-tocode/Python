horas = input("Enter hours: ")
rate = input("Enter rate: ")
fr = float(rate)
fh = float(horas)
if fh > 40:
    print("Overitime")
    reg = fr * fh
    overtime = (fh - 40.0) * 0.5
    print(reg,overtime)
    pay = reg + overtime
else:
    print("Regular")
    pay = fr * fh
print("Pay: ", pay)