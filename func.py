data = {
    "eden":"password123",
    "edward":"pass123",
}
from getpass import getpass
from webbrowser import get
def start():
    print("Welcome to the portal\nTo proceed please sign in")
    welcome = input("Alredy have an account? ").capitalize()
    if welcome == "Yes":
        print("\n")
        log_in()
    elif welcome == "No":
        print("\n")
        signup()
def log_in():
    global data
    username = input("Enter your user name: ")
    password = getpass("Enter your password:")
    for u,p in data.items():
        if (username == u) and (password == p):
            print("Welcome!!")
            main()
            quit()
        elif (username == u) and (password != p):
            print("Invalid password or username")
            print("\n")
            log_in()
            quit()
    print("Name not found")
    print("\n")
    signup()
    quit()
def signup():
    t_a = input("Do you want to Sign up? ").capitalize()
    if t_a == "Yes":
        print("That's very good")
        print("\n")
        re_sign_up()
        print("/n")
        main()
    else:
        print("Have a nice day!!")
        quit()

def re_sign_up():
    name = input('Enter your First name: ')
    name = input('Enter your Last name: ')
    user_name = input("Enter the username you intend on using: ")
    password = getpass("Enter your password: ")
    confirm_password = getpass("Confirm password: ")
    if password == confirm_password:
        data[user_name] = password
        print(f"{user_name} Your account has been created")
        print("You can now login into your account\n")
        log_in()
    else:
        print("The password you entered does not match\nPlease resign up")
        print("\n")
        re_sign_up()
def main():
    global fhand
    set = input("Enter the year you graduated from Olivet: ")
    if set == "2022":
        set = "mbox.txt"
    fhand = open("mbox.txt")
    print("This prompt you to check up a classmate's info: ")
    name = input("Enter your classmate's name: ").capitalize()
    for line in fhand:
        line = line.rstrip()
        if name in line:
            print(line)
            t_a = input("Do you want to run the program again?\n(Enter (y) for y and (n) for No) ")
            if t_a == "y":
                main()
            else:
                print("Have a nice day!!")
                quit()
    print("Name of student not found")
