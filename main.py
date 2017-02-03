__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Development"
__version__ = 0.24
# This was a file for question functions; now is main file due to changed method.


def deviceOS():
    ans = str.lower(str(input("What OS does your phone use?")))
    if ans == "ios" or "apple" or "iphone":
        return "steve"
    elif ans == "samsung" or "android" or "htc" or "lg":
        return "andy"
    elif ans == "nokia" or "windows" or "lumia":
        return "bill"
    else:
        print("I did not understand your input, please try again.")
        deviceOS()


def warrantyInsure():  # Is the device insured or under warranty?
    ans = str.lower(str(input("Are you under Warranty or Insured with this device?")))
    if ans == "yes" or "y":
        return true
    elif ans == "no" or "n":
        return false
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure()


def problemQue():  # Does this device actually have problems?
    ans = str.lower(str(input("Does your device have any problems?")))
    if ans == "yes" or "y":
        print("Sorry, this program is primitive;"),
        print("we will now loop you back to the beginning and hope we can solve this.")
        # CALL MAIN FUNCTION
    elif ans == "no" or "n":
        print("Thanks for using this program; see you around!")
    else:
        print("I did not understand your input, please try again.")
        problemQue()


def backUp(x):  # In main.py, x = deviceOS()
    ans = str.lower(str(input("Have you backed up your device recently?")))
    if ans == "yes" or "y":
        print("We suggest you fully reset your device;")
        if x == "steve":
            print("Plug your Device into your Computer, open itunes and reset it from there.")
        elif x == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select Factory Data Reset and follow the prompts.")
        elif x == "bill":
            print("See https://support.microsoft.com/en-us/help/10666/windows-phone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow the prompts.")
        print("Thanks for using this program; see you around!")
    elif ans == "no" or "n":
        print("We recommend you see a phone repair shop, especially a virus specialist.")
        print("Thanks for using this program; see you around!")
    else:
        print("I did not understand your input, please try again.")
        backup()


def infection():  # Is the device infected?
    ans = str.lower(str(input("Is your device infected?")))
    if ans == "yes" or "y":
        return true
    elif ans == "no" or "n":
        return false
    else:
        print("I did not understand your input, please try again.")
        infection()


def screenBroke():  # Is the screen broken?
    ans == str.lower(str(input("Is the screen/screen glass broken?")))
    if ans == "yes" or "y":
        return true
    elif ans == "no" or "n":
        return false
    else:
        print("I did not understand your input, please try again.")
        screenBroke()


char = false
def isScreenOn():  # Is the screen on?
    ans == str.lower(str(input("Is the screen on?")))
    if (ans == "no" or "n") and char == false: 
        print("Try charging your device with a different charger.")
        char = true
        isScreenOn()
    elif (ans == "no" or "n") and char == true:
        return false
    elif ans == "yes" or "y":
        return true
    else:
        print("I did not understand your input, please try again.")
        isScreenOn()


# Test Script
var0 = deviceOS()
print(var0)
var1 = str(warrantyInsure())
print(var1)
var2 = str(problemQue())
print(var2)
var3 = backUp(var0)
var4 = str(infection())
print(var4)
var5 = str(screenBroke())
print(var5)
var6 = str(isScreenOn())
print(var6)
