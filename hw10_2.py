class WrongTypeError(Exception):
    "We should not use Bool"
def is_all_unique(list):

    try:
        for num in list:
            int(num)
            if type(num) == bool:
                raise WrongTypeError
        if len(list) == 0:
            raise Exception
        set_from_list = set(list)
        if len(set_from_list) == len(list):
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
