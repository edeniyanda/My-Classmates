from getpass import getpass

data = {
    "eden":"password123",
    "edward":"pass123",
    "quicksilver":"12345"
}

def start():
    print("Welcome to the portal\nTo proceed please sign in\n")
    while True:
        welcome = input("Alredy have an account? ").capitalize()
        if welcome == "Yes":
            print("\n")
            log_in()
        elif welcome == "No":
            print("\n")
            signup()
        else:
            print('Invalid input, please enter with a "Yes" or "No"\n')
            
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
    elif t_a =="No":
        print("Have a nice day!!")
        quit()
    else:
        print("Invalid Input")
        signup()

def re_sign_up():
    fname = input('Enter your First name: ').capitalize()
    lname = input('Enter your Last name: ').capitalize()
    user_name = input("Enter the username you intend on using: ")
    password = getpass("Enter your password: ")
    confirm_password = getpass("Confirm password: ")
    if password == confirm_password:
        data[user_name] = password
        print(f"Congratulations {fname} {lname} Your account has been created")
        print("You now have access to the Portal\n")
        main()
    else:
        print("The password you entered does not match\nPlease resign up")
        print("\n")
        re_sign_up()
        
def main():
    global fhand
    year = input("Enter the year you graduated from Olivet Baptist High School: ")
    if year == "2022":
        year = "mbox.txt"
    else:
        try:
            year = int(year)
            print(year)
            print("Invalid input ")
            main()
        except:
            print('Enter a numeric data!')
            main()
            
    fhand = open(year)
    print("This prompt you to check up a classmate's info: ")
    name = input("Enter your classmate's name: ").capitalize()
    
    for line in fhand:
        line = line.rstrip()
        if name in line:
            print(line)
            t_a = input("Do you want to run the program again?\n(Enter (y) for y and (n) for No) ").lower()
            if t_a == "y":
                main()
            else:
                print("Have a nice day!!")
                quit()
    print("Name of student not found")
