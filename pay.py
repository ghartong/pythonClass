hrInput = input("Enter hours:")
rInput = input("Enter rate:")
errors = False

try:
    hours = float(hrInput)
except:
    print("Hours must be numeric")
    errors = True

try:
    rate = float(rInput)
except:
    print("Rate must be numeric")
    errors = True

if errors != True:
    pay = hours * rate
    print(pay)