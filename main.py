__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Tests"
__version__ = 0.81
# MainFile, includes question funcs - modularity is gone :(
# Imports

import sys

# Variables

global charged
global operSys
charged = False
operSys = " "


def warrantyInsure(): # Is the device insured or under warranty?
    global operSys
    ans = str.lower(str(input("Are you under Warranty or Insured with this device?\n")))
    if (ans == "yes" or ans == "y") and operSys == "steve":
        print("Return your device to Apple or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or ans == "y") and operSys == "andy":
        print("Return your device to your manufacturer or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or ans == "y") and operSys == "gates":
        print("Return your device to Nokia or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "no" or ans == "n") and operSys == "steve":
        print("As your manufacturer will likely not support you, please\n")
        print("visit some iphone forums, EG:"),
        forums = open("forums.txt","r")
        f = forums.readlines()
        print(f[1])
        print(f[2])
        print(f[3])
        forums.close()
    elif (ans == "no" or ans == "n") and operSys == "andy":
        print("As your manufacturer will likely not support you, please\n")
        print("visit some android forums, EG:"),
        forums = open("forums.txt","r")
        f = forums.readlines()
        print(f[5])
        print(f[6])
        print(f[7])
        forums.close()
    elif (ans == "no" or ans == "n") and operSys == "gates":
        print("As your manufacturer will likely not support you, please\n")
        print("visit some windows phone forums, EG:"),
        forums = open("forums.txt","r")
        f = forums.readlines()
        print(f[9])
        print(f[10])
        print(f[11])
        forums.close()
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure()
    print("Thanks for using this program; see you around!")
    sys.exit()


def backUp():  # is the device backed up
    global operSys
    ans = str.lower(str(input("Have you backed up your device recently?\n")))
    if ans == "yes" or ans == "y":
        print("We suggest you fully reset your device;"),
        if operSys == "steve":
            print("Plug your Device into your Computer, open itunes and reset it from there.")
        elif operSys == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select Factory Data Reset and follow the prompts.")
        elif operSys == "bill":
            print("See https://support.microsoft.com/en-us/help/10666/windows-phone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow the prompts.")
        else:
            print("Error; somehow deviceOS wasn't called!")
            deviceOS()
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "no" or ans == "n":
        print("We recommend you see a phone repair shop, especially a virus specialist."),
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        backup()


def problemQue():  # Does this device actually have problems?
    ans = str.lower(str(input("Does your device have any problems?\n")))
    if ans == "yes" or ans == "y":
        print("Sorry, this program is primitive;"),
        print("we will now loop you back to the beginning and hope we can solve this.")
        deviceOS()
    elif ans == "no" or ans == "n":
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        problemQue()


def infection():  # Is the device infected?
    ans = str.lower(str(input("Is your device infected?\n")))
    if ans == "yes" or ans == "y":
        backUp()
    elif ans == "no" or ans == "n":
        problemQue()
    else:
        print("I did not understand your input, please try again.")
        infection()


def screenBroke():  # Is the screen broken?
    ans = str.lower(str(input("Is the screen/screen glass broken?\n")))
    if ans == "yes" or ans == "y":
        warrantyInsure()
    elif ans == "no" or ans == "n":
        infection()
    else:
        print("I did not understand your input, please try again.")
        screenBroke()


def isScreenOn():  # Is the screen on?
    global charged
    ans = str.lower(str(input("Is the screen on?\n")))
    if (ans == "no" or ans == "n") and (charged == False):
        print("Try charging your device with a different charger.")
        charged = True
        isScreenOn()
    elif (ans == "no" or ans == "n") and (charged == True):
        warrantyInsure()
    elif (ans == "yes") or (ans == "y"):
        screenBroke()
    else:
        print("I did not understand your input, please try again.")
        isScreenOn()


def deviceWater():  # Is the problem due to water?
    ans = str.lower(str(input("Does your issue involve water?\n")))
    if ans == "yes" or ans == "y":
        print("Dry your device!"),
        print("Take it apart as far as you can"),
        print("(remove back cover and battery if possible),"),
        print("gently towel dry the outer of the phone, then"),
        print("place in rice or (preferably) silica gel for a time."),
        print("Then, remove from the rice and replace the battery"),
        print("and try to turn the device on.")
        isScreenOn()
    elif ans == "no" or ans == "n":
        isScreenOn()
    else:
        print("I did not understand your input, please try again.")
        deviceWater()


def deviceOS():  # What OS does the device use/what manufacturer?
    global operSys
    operSys = " "
    ans = str.lower(str(input("What OS does your phone use?\n")))
    if ans == "ios" or ans == "apple" or ans == "iphone":
        operSys = "steve"
        deviceWater()
    elif ans == "samsung" or ans == "android" or ans == "htc" or ans == "lg":
        operSys = "andy"
        deviceWater()
    elif ans == "nokia" or ans == "windows" or ans == "lumia":
        operSys = "bill"
        deviceWater()
    else:
        print("I did not understand your input, please try again.")
        deviceOS()


deviceOS()
