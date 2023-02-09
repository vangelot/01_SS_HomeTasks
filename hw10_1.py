import sys
class OutOfRangeError(Exception):
    "Number of month is not in range 1..12"

def month_name(month_number):
    # month = 0
    dict_month = {1: "January", 2: "Febrary", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}
    try:
        month = int(month_number)
        if month not in range(1, 12):
            raise OutOfRangeError
        return dict_month[month]
    except ValueError:
        print('input mistake, inputed value is not integer')
        # sys.exit()
    except OutOfRangeError:
        print("there is no such month")
        # sys.exit()
    except Exception:
        print("some else error")
        # sys.exit()

a = input("Enter month nomber: ")
if month_name(a): #!= None:
    print(month_name(a))