import os
import getpass

os.system("tput setaf 1")
print("\t\t\tTerminal User Interface")

os.system("tput setaf 7")
print("\t\t\t-----------------------")

passwd = getpass.getpass("Enter the password : ")

actpasswd="redhat"

if actpasswd != passwd:
    print("Incorrect password")
    exit()

print("Destination at which task need to be performed (local/remote) :", end='')
location = input()
print(location)

if location == "remote":
    Ip= input("Enter remote Ip :")
    key = input("Want to add key (y/n) : ")

    if(key == 'y'):
        os.system("ssh-keygen")
        os.system("ssh-copy-id root@{0}".format(Ip))
    elif(key == 'n'):
        pass




os.system("clear")
while True:

    os.system("tput setaf 3")

    print("""
             Press 1: Date
             Press 2: Calendar
             Press 3: Configure web Server
             Press 4: To add new User
             Press 5: Run docker container
             Press 6: Newtork Setup
             Press 7: Exit
             """)

    os.system("tput setaf 7")

# Choice selection of the feature

    ch=input("Enter Your Choice :")
    print("\n")

#Local machine
    if location == "local":
        if int(ch) == 1:
            os.system("date")
        elif int(ch) == 2:
            os.system("cal")
        elif int(ch) == 3:
            os.system("yum install httpd")
        elif int(ch) == 4:
            create_user = input("Enter UserName")
            os.system("useradd {}".format(create_user))
        elif int(ch) == 5:
            os.system("systemctl start docker")
            os.system("systemctl status docker | grep Active")
            input("Press return key to launch container")
            os.system("clear")
            print(" Wait . . . . \n")
            os.system("docker images")
            os.system("tput setaf 3")
            img = input ("Enter the image name with version : ")
            name = input ("Enter the name of the image : ")
            os.system("clear")
            os.system("tput setaf 7")
            os.system("docker run -dit --name {0} {1}".format(name, img))
        elif int(ch) == 6:
            os.system("")
        elif int(ch) == 7:
            os.system("clear")
            exit()
        else:
            print("Enter valid option")

        os.system("tput setaf 1")
        input("Press return key to continue...")
        os.system("clear")
        os.system("tput setaf 7")

#remote machine
    elif location == "remote":

        os.system("clear")

        if int(ch) == 1:
            os.system("ssh {} date".format(Ip))
        elif int(ch) == 2:
            os.system("ssh {} cal".format(Ip))
        elif int(ch) == 3:
            os.system("ssh {} yum install httpd".format(Ip))
        elif int(ch) == 4:
            create_user = input("Enter UserName")
            os.system("ssh {0} useradd {1}".format(Ip, create_user))
        elif int(ch) == 5:
            os.system("ssh {0} systemctl start docker".format(Ip))
            os.system("ssh {0} systemctl status docker | grep Active".format(Ip))
            print("\n")
            input("Press return key to launch container".format(Ip))
            os.system("clear")
            print(" Wait . . . . \n")
            os.system("ssh {0} docker images".format(Ip))
            os.system("tput setaf 3")
            img = input ("ssh {0} Enter the image name with version : ".format(Ip))
            name = input ("ssh {0} Enter the name of the image : ".format(Ip))
            os.system("clear")
            os.system("tput setaf 7")
            os.system("ssh {0} docker run -dit --name {1} {2}".format(Ip, name, img))

        elif int(ch) == 6:
            os.system("")
        elif int(ch) == 7:
            os.system("clear")
            exit()
        else:
            print("Enter a valid option")

        os.system("tput setaf 1")
        input("Press Return key to continue... ")
        os.system("tput setaf 7")
        os.system("clear")

#invalid location
    else:
        print("Invalid Location")
