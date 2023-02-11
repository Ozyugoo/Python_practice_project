h = input("Enter Hours:")
r = input("Enter Rate:")
fh = float(h)
fr = float(r)
if  fh > 40:
    reg = fr * fh
    otpay = (fh - 40.0) * (fr * 0.5)
    pay = reg + otpay
    print("Pay:", pay)
else:
    pay = fr * fh
    print("Pay:", pay)