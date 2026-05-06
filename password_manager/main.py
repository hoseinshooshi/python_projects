# store your password encrypted, then decrypt with a master password
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: 
        key_file.write(key)
write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

pwd = input("what is the master password? ")
key = load_key() + pwd.encode()
fer = Fernet(key)

def view():
    what_to_read = input("if there is an specific website that you wanna see your account and password for, enter the website name, if you wanna see all the passwords, type all.(all/website) ").lower()
    with open('passwords.txt', 'r') as f:
        if what_to_read == "all":
            for line in f.readlines():
                data = line.rstrip()
                site, user, passw = data.split("|")
                print("website:", site,"username: ", user, "password: ", fer.decrypt(passw.encode()).decode() )
        # check if an specified line, contains the website and return the password
        else: 
            # open the file in reading mode
            with open('passwords.txt', 'r') as f:
                # read lines
                lines = f.readlines()
                does_exists = False
                # loop lines
                for line in lines:
                    if line.find(what_to_read) != -1:
                        data = line.rstrip()
                        site, user, passw = data.split("|")
                        print("details: ","username=", user, "password=", fer.decrypt(passw.encode()).decode())
                        does_exists = True
                    else:
                        pass

def add():
    website = input("add the website address or name that you have the account on: ").lower()
    username = input("add your account username: ")
    password = input("add your account password: ")
    # now open a file or create one if doesnt exist than add the password
    # the second parameter in open("first_para", "second_para") is the mode, if written 'w' then it would write and create a new file if the file doesnt exist but everytime that is executed, it will clear the file with 'r' you only read the file and 'a' wich you add to file and create if doesnt exist
    with open('passwords.txt', 'a') as f:
        f.write(website + " | " + username + " | " + fer.encrypt(password.encode()).decode() + "\n")
while True: 
    mode = input("do you wanna add a new password or view existing ones?(view/add) type 'q' to quit. ").lower()

    if mode == "view": 
        view()
    elif mode == "add": 
        add()
    elif mode == "q": 
        break
    else: 
        print("not a valid input, try again")
        continue
    