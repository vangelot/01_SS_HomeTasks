username = ''


def choose_username():
    global username
    username = input("Enter login: ")
    if len(username) > 5:
        print("login saved")
    else:
        print("try another one (more than 5 letters)")
        choose_username()


def print_username():
    print(username)


def main():
    choose_username()
    print_username()


if __name__ == '__main__':
    main()

