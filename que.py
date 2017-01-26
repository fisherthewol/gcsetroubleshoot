__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Development"
__version__  =  0.20
##This is a file for question functions; allows for //modularity//
def warrantyInsure(): ##Is the device insured or under warranty
    ans = input("Are you under Warranty or Insured with this device?")
    if ans == "yes" or "Yes" or "y" or "Y":
        return true
    elif ans == "no" or "No" or "n" or "N":
        return false
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure()

def problemQue(): ##Does this device actually have problems?
    ans = input("Does your device have any problems?")
    if ans == "yes" or "Yes" or "y" or "Y":
        print("Sorry, this program is primitive; we will now loop you back to the beginning and hope we can solve this.")
        ##CALL MAIN FUNCTION
    elif ans == "no" or "No" or "n" or "N":
        print("Thanks for using this program; see you around!")
    else:
        print("I did not understand your input, please try again.")
        problemQue()

def backUp(x):##In main.py, x = deviceOS()
    ans = input("Have you backed up your device recently?")
    if ans == "yes" or "Yes" or "y" or "Y":
        print("We suggest you fully reset your device;")
        if x == "steve":
            print("Plug your Device into your Computer, open itunes and reset it from there.")
        elif x == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select Factory Data Reset and follow the prompts.")
        elif x == "bill":
            print("See https://support.microsoft.com/en-us/help/10666/windows-phone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow the prompts.")
        print("Thanks for using this program; see you around!")
    elif ans == "no" or "No" or "n" or "N":
        print("We recommend you see a phone repair shop, especially a virus specialist.")
        print("Thanks for using this program; see you around!")
    else:
        print("I did not understand your input, please try again.")
        backup()

def infection(): ##Is the device infected?
    ans = input("Is your device infected?")
    if ans == "yes" or "Yes" or "y" or "Y":
        backUp()
    elif ans == "no" or "No" or "n" or "N":
        problemQue()
    else:
        print("I did not understand your input, please try again.")
        infection()
