__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Tests"
__version__ = 0.63
# MainFile, includes question funcs - modularity is gone :(

import sys

# Variables

charged = False
devicesOS = str


def warrantyInsure(x):  # Is the device insured or under warranty?
    ans = str.lower(str(input("Are you under Warranty or Insured with this device?\n")))
    if ans == "yes" or "y" and x == "steve":
        print("Return your device to Apple or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "yes" or "y" and x == "andy":
        print("Return your device to your manufacturer or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "yes" or "y" and x == "gates":
        print("Return your device to Nokia or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "no" or "n" and x == "steve":
        print("Visit some iphone forums, EG:"),
        forums = open("forums.txt","r")
        print(str(forums.readlines(2))),
        print(str(forums.readlines(3))),
        print(str(forums.readlines(4))),
        forums.close()
    elif (ans == "no" or "n") and x == "andy":
        print("Visit some android forums, EG:"),
        forums = open("forums.txt","r")
        print(str(forums.readlines(6))),
        print(str(forums.readlines(7))),
        print(str(forums.readlines(8))),
        forums.close()
    elif (ans == "no" or "n") and x == "gates":
        print("Visit some windows phone forums, EG:"),
        forums = open("forums.txt","r")
        print(str(forums.readlines(10))),
        print(str(forums.readlines(11))),
        print(str(forums.readlines(12))),
        forums.close()
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure(devicesOS)
    print("Thanks for using this program; see you around!")
    sys.exit()


def backUp(x):  # is the device backed up
    ans = str.lower(str(input("Have you backed up your device recently?\n")))
    if ans == "yes" or "y":
        print("We suggest you fully reset your device;"),
        if x == "steve":
            print("Plug your Device into your Computer, open itunes and reset it from there.")
        elif x == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select Factory Data Reset and follow the prompts.")
        elif x == "bill":
            print("See https://support.microsoft.com/en-us/help/10666/windows-phone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow the prompts.")
        else:
            print("Error; somehow deviceOS wasn't called!")
            deviceOS()
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "no" or "n":
        print("We recommend you see a phone repair shop, especially a virus specialist."),
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        backup()


def problemQue():  # Does this device actually have problems?
    ans = str.lower(str(input("Does your device have any problems?\n")))
    if ans == "yes" or "y":
        print("Sorry, this program is primitive;"),
        print("we will now loop you back to the beginning and hope we can solve this.")
        deviceOS()
    elif ans == "no" or "n":
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        problemQue()


def infection():  # Is the device infected?
    ans = str.lower(str(input("Is your device infected?\n")))
    if ans == "yes" or "y":
        backUp(devicesOS)
    elif ans == "no" or "n":
        problemQue()
    else:
        print("I did not understand your input, please try again.")
        infection()


def screenBroke():  # Is the screen broken?
    ans = str.lower(str(input("Is the screen/screen glass broken?\n")))
    if ans == "yes" or "y":
        warrantyInsure(devicesOS)
    elif ans == "no" or "n":
        infection()
    else:
        print("I did not understand your input, please try again.")
        screenBroke()


def isScreenOn(x):  # Is the screen on?
    ans = str.lower(str(input("Is the screen on?\n")))
    if (ans == "no" or ans == "n") and (x == False):
        print("Try charging your device with a different charger.")
        x = True
        isScreenOn(x)
    elif (ans == "no" or ans == "n") and (x == True):
        warrantyInsure(devicesOS)
    elif (ans == "yes") or (ans == "y"):
        screenBroke()
    else:
        print("I did not understand your input, please try again.")
        isScreenOn(x)


def deviceWater():  # Is the problem due to water?
    ans = str.lower(str(input("Does your issue involve water?\n")))
    if ans == "yes" or "y":
        print("Dry your device!"),
        print("Take it apart as far as you can"),
        print("(remove back cover and battery if possible),"),
        print("gently towel dry the outer, then"),
        print("place in rice or (preferably) silica gel for a time."),
        print("Then, remove from the rice and replace the battery"),
        print("and try to turn the device on.")
        isScreenOn(charged)
    elif ans == "no" or "n":
        isScreenOn(charged)
    else:
        print("I did not understand your input, please try again.")
        deviceWater()


def deviceOS():  # What OS does the device use/what manufacturer?
    ans = str.lower(str(input("What OS does your phone use?\n")))
    if ans == "ios" or "apple" or "iphone":
        devicesOS = "steve"
        deviceWater()
    elif ans == "samsung" or "android" or "htc" or "lg":
        devicesOS = "andy"
        deviceWater()
    elif ans == "nokia" or "windows" or "lumia":
        devicesOS = "gates"
        deviceWater()
    else:
        print("I did not understand your input, please try again.")
        deviceOS()


deviceOS()
