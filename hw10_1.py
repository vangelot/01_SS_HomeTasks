

class OutOfRangeError(Exception):
    """Number of month is not in range 1..12"""
    def __init__(self, number_of_month):
        print("number ", number_of_month, " is not in range 1-12")


def month_name(month_number):
    # month = 0
    dict_month = {1: "January", 2: "February", 3: "March", 4: "April",
                  5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}
    try:
        month = int(month_number)
        if month not in range(1, 12):
            raise OutOfRangeError(month)
        return dict_month[month]
    except ValueError:
        print('input mistake, inputted value is not integer')
        return "ERROR !!!"
    except OutOfRangeError:
        print("OutOfRangeError")
        return "ERROR !!!"
    except Exception:
        print("some else error")
        return "ERROR !!!"


a = input("Enter month number: ")
print(month_name(a))
