class WrongTypeError(Exception):
    """We should not use Bool"""


def is_all_unique(list_of_numbers):
    try:
        for num in list_of_numbers:
            int(num)
            if type(num) == bool:
                raise WrongTypeError
        if len(list_of_numbers) == 0:
            raise Exception
        set_from_list = set(list_of_numbers)
        if len(set_from_list) == len(list_of_numbers):
            return "List is Unique"
        else:
            return "List is not Unique"
    except ValueError:
        print("List include NOT a number")
        return "ERROR"
    except WrongTypeError:
        print('List should not include BOOL type')
        return "ERROR"
    except Exception:
        print("List is empty")
        return "ERROR"


print(is_all_unique([1, 2, 3]), '\n')

print(is_all_unique([]), '\n')

print(is_all_unique('a'), '\n')

print(is_all_unique([1, 2, False]), '\n')

print(is_all_unique([1, 2, 3, 3, 10.5]))
