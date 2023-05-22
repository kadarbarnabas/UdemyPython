for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print("A megadott érték nem emelhető hatványra")

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Egy szám nullával való osztása nem értelmezhető")
finally:
    print("All Done")
    
def ask():
    while True:
        try:
            num = int(input("Input an integer: "))
            print(f"Thank you, your number squared is: {num**2}")
            break
        except TypeError:
            print("Whoops! An error occurd! Please Try again!")
        except ValueError:
            print("Whoops! An error occurd! Please Try again!")
        except UnboundLocalError:
            print("Whoops! An error occurd! Please Try again!")
            
ask()
        
