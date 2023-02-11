score = input("Enter Scores:")
try:
    sf = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if sf > 1.0:
    print("Out of range")
elif sf >= 0.9:
    print('A')
elif sf >= 0.8:
    print('B')
elif sf >= 0.7:
    print('C')
elif sf >= 0.6:
    print('D')
elif sf < 0.6:
    print('F')
elif sf < 0.0:
    print("Error, out of range")
print("Score Grade:", sf)