__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Development"
__version__ = 0.45
# MainFile, includes question func - modularity is gone :(

import sys

# Variables
charged = False
devicesOS = str


def warrantyInsure(x):  # Is the device insured or under warranty?
    ans = str.lower(str(input("Are you under Warranty or Insured with this device?")))
    if (ans == "yes" or "y") and x == "steve":
        print("Return your device to Apple or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or "y") and x == "andy":
        print("Return your device to your manufacturer or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or "y") and x == "andy":
        print("Return your device to Nokia or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure()


def infection():  # Is the device infected?
    ans = str.lower(str(input("Is your device infected?")))
    if ans == "yes" or "y":
        return True
    elif ans == "no" or "n":
        return False
    else:
        print("I did not understand your input, please try again.")
        infection()


def screenBroke():  # Is the screen broken?
    ans == str.lower(str(input("Is the screen/screen glass broken?")))
    if ans == "yes" or "y":
        warrantyInsure()
    elif ans == "no" or "n":
        infection()
    else:
        print("I did not understand your input, please try again.")
        screenBroke()


def isScreenOn():  # Is the screen on?
    ans = str.lower(str(input("Is the screen on?")))
    if (ans == "no" or "n") and charged == False:
        print("Try charging your device with a different charger.")
        charged = True
        isScreenOn()
    elif (ans == "no" or "n") and charged == True:
        warrantyInsure(devicesOS)
    elif ans == "yes" or "y":
        screenBroke()
    else:
        print("I did not understand your input, please try again.")
        isScreenOn()


def deviceWater():  # Is the problem due to water?
    ans = str.lower(str(input("Does your issue involve water?")))
    if ans == "yes" or "y":
        print("Dry your device!"),
        print("Take it apart as far as you can"),
        print("(remove back cover and battery if possible),"),
        print("gently towel dry the outer, then"),
        print("place in rice or (preferably) silica gel for a time."),
        print("Then, remove from the rice and replace the battery"),
        print("and try to turn the device on.")
        isScreenOn()
    elif ans == "no" or "n":
        isScreenOn()
    else:
        print("I did not understand your input, please try again.")
        deviceWater()


def deviceOS():  # What OS does the device use/what manufacturer?
    ans = str.lower(str(input("What OS does your phone use?")))
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


def problemQue():  # Does this device actually have problems?
    ans = str.lower(str(input("Does your device have any problems?")))
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


def backUp(x):  # parse variable of deviceOS
    ans = str.lower(str(input("Have you backed up your device recently?")))
    if ans == "yes" or "y":
        print("We suggest you fully reset your device;"),
        if x == "steve":
            print("Plug your Device into your Computer, open itunes and reset it from there.")
        elif x == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select Factory Data Reset and follow the prompts.")
        elif x == "bill":
            print("See https://support.microsoft.com/en-us/help/10666/windows-phone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow the prompts.")
        print("Thanks for using this program; see you around!")
    elif ans == "no" or "n":
        print("We recommend you see a phone repair shop, especially a virus specialist."),
        print("Thanks for using this program; see you around!")
    else:
        print("I did not understand your input, please try again.")
        backup()
