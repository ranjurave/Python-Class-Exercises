print("Hours worked calculator")
try:
    GrossPay = int(input("Enter Gross pay : "))
    pay_rate = int(input("Enter hourly pay rate : "))
    hours = GrossPay / pay_rate
    print("Hours worked = ", hours)
except ZeroDivisionError:
    print("ERROR: cannot give zero")
except ValueError:
    print("Error: Value error")
except:
    print("Somethings wrong")

print("end of program")
