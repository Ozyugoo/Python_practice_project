h = input("Enter Hours:")
r = input("Enter Rate:")
try:
    fh = float(h)
    fr = float(r)
except:
    print("Error, please enter numeric input")
    quit()

if  fh > 40:
    reg = fr * fh
    otpay = (fh - 40.0) * (fr * 0.5)
    pay = reg + otpay
    print("Pay:", pay)
else:
    pay = fr * fh
    print("Pay:", pay)