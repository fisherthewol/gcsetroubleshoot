__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Development"
__version__ = 1.45

# Imports

import sys,time

# Variables

global charged
global operSys
global dried
global userProb
global aindex
charged = False
operSys = " "
dried = False
userProb = " "
aindex = 0


def outPutter(x):  # outputs to file
    t = time.time()
    ti = time.strftime("%H:%M")
    da = time.strftime("%Y%m%d")
    with open("userprob/{}.txt".format(t),"w+") as f:
        f.write("LocalTime: {} {}\nOperSys: {}\nUserProblem: {}\n"
        "IndexReached: {}\nFunctionReached: {}".format(da,ti,operSys,userProb,
        aindex,x))


def warrantyInsure():  # Is the device insured or under warranty?
    global operSys
    ans = str.lower(str(input("Are you under Warranty or Insured with this "
    "device?\n>")))
    if (ans == "yes" or ans == "y") and operSys == "steve":
        print("Return your device to Apple or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or ans == "y") and operSys == "andy":
        print("Return your device to your manufacturer or contact your"
        " insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "yes" or ans == "y") and operSys == "gates":
        print("Return your device to Nokia or contact your insurer.")
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif (ans == "no" or ans == "n") and operSys == "steve":
        print("As your manufacturer will likely not support you, please")
        print("visit some iphone forums, EG:\n")
        forums = open("forums.txt", "r")
        f = forums.readlines()
        print(f[1] + f[2] + f[3])
        forums.close()
        print("And try searching/asking about your issue there.")
    elif (ans == "no" or ans == "n") and operSys == "andy":
        print("As your manufacturer will likely not support you, please")
        print("visit some android forums, EG:\n")
        forums = open("forums.txt", "r")
        f = forums.readlines()
        print(f[5] + f[6] + f[7])
        forums.close()
        print("And try searching/asking about your issue there.")
    elif (ans == "no" or ans == "n") and operSys == "gates":
        print("As your manufacturer will likely not support you, please")
        print("visit some windows phone forums, EG:\n")
        forums = open("forums.txt", "r")
        f = forums.readlines()
        print(f[9] + f[10] + f[11])
        forums.close()
        print("And try searching/asking about your issue there.")
    else:
        print("I did not understand your input, please try again.")
        warrantyInsure()
    print("Thanks for using this program; see you around!")
    sys.exit()


def backUp():  # is the device backed up?
    global operSys
    ans = str.lower(str(input("Have you backed up your device recently?\n>")))
    if ans == "yes" or ans == "y":
        print("We suggest you fully reset your device;"),
        if operSys == "steve":
            print("Plug your Device into your Computer, open itunes and reset i"
            "t from there.")
        elif operSys == "andy":
            print("Go to settings, scroll and enter Backup and Settings, select"
            " Factory Data Reset and follow the prompts.")
        elif operSys == "gates":
            print("See https://support.microsoft.com/en-us/help/10666/windows-p"
            "hone-reset-my-phone"),
            print("Go to Settings, About Phone, select reset phone, and follow"
            " the prompts.")
        else:
            print("Error; somehow deviceOS wasn't called!")
            print("We will now loop this program.")
            main()
        print("Thanks for using this program; see you around!")
        sys.exit()
    elif ans == "no" or ans == "n":
        print("We recommend you see a phone repair shop, especially a virus"
        " specialist."),
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        backup()


def problemQue():  # Does this device actually have problems?
    ans = str.lower(str(input("Does your device have any (further)"
    " issues?\n>")))
    if ans == "yes" or ans == "y":
        print("Sorry, this program is primitive;"),
        print("we will now loop you back to the beginning and hope we can solve"
        " this.")
        main()
    elif ans == "no" or ans == "n":
        print("Thanks for using this program; see you around!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        problemQue()


def infection():  # Is the device infected?
    ans = str.lower(str(input("Do you think your device is infected with a "
    "virus?\n>")))
    if ans == "yes" or ans == "y":
        backUp()
    elif ans == "no" or ans == "n":
        print("Your issue is currently not interperatable or solvable.")
        try:
            outPutter("infection")
            print("Your issue was written to file a file in the userprob"
            " folder.")
            print("Please send that file to the developers when you get a "
            "chance.")
        except:
            print("Error was encountered while trying to write file.")
            print("Your issue may have been written to a file, or it may have "
            "not.")
        print("Thank you for using this program.\nGoodbye now!")
        sys.exit
    else:
        print("I did not understand your input, please try again.")
        infection()


def screenBroke():  # Is the screen broken?
    ans = str.lower(str(input("Is the screen/screen glass broken?\n>")))
    if ans == "yes" or ans == "y":
        warrantyInsure()
    elif ans =="no" or ans == "n":
        problemQue()
    else:
        print("I did not understand your input, please try again.")
        screenBroke()


def isScreenOn():  # Is the screen on?
    global charged
    ans = str.lower(str(input("Is the screen on?\n>")))
    if (ans == "no" or ans == "n") and (charged == False) and (dried == False):
        print("This presumes your device has been dried or has not come into"
        " contact with water.")
        print("If the above is not true, PLEASE dry your device first.")
        print("Try charging your device with a different charger.")
        charged = True
        isScreenOn()
    elif (ans == "no" or ans == "n") and (charged == True) and (dried == False):
        warrantyInsure()
    elif (ans == "yes") or (ans == "y") and (dried == True):
        problemQue()
    elif (ans == "yes") or (ans == "y") and (dried == False):
        print("Your issue is currently not interperatable or solvable.")
        try:
            outPutter("isScreenOn")
            print("Your issue was written to file a file in the userprob"
            " folder.")
            print("Please send that file to the developers when you get a "
            "chance.")
        except:
            print("Error was encountered while trying to write file.")
            print("Your issue may have been written to a file, or it may have "
            "not.")
        print("Thank you for using this program.\nGoodbye now!")
        sys.exit()
    else:
        print("I did not understand your input, please try again.")
        isScreenOn()


def deviceWater():  # Is the problem due to water?
    ans = str.lower(str(input("Does your issue involve water?\n>")))
    if ans == "yes" or ans == "y":
        print("Dry your device!"),
        print("Take it apart as far as you can"),
        print("(remove back cover and battery if possible),"),
        print("gently towel dry the outer of the phone, then"),
        print("place in rice or (preferably) silica gel for a time."),
        print("Then, remove from the rice and replace the battery"),
        print("and try to turn the device on.")
        global dried
        dried = True
        isScreenOn()
    elif ans == "no" or ans == "n":
        print("Your issue is currently not interperatable or solvable.")
        try:
            outPutter("deviceWater")
            print("Your issue was written to file a file in the userprob"
            " folder.")
            print("Please send that file to the developers when you get a "
            "chance.")
        except:
            print("Error was encountered while trying to write file.")
            print("Your issue may have been written to a file, or it may have "
            "not.")
        print("Thank you for using this program.\nGoodbye now!")
        sys.exit
    else:
        print("I did not understand your input, please try again.")
        deviceWater()


def deviceOS():  # What OS does the device use/what manufacturer?
    global operSys
    operSys = " "
    ans = str.lower(str(input("What type/maker of phone do you have?\n>")))
    if ans == "ios" or ans == "apple" or ans == "iphone":
        operSys = "steve"
    elif ans == "samsung" or ans == "android" or ans == "htc" or ans == "lg":
        operSys = "andy"
    elif ans == "nokia" or ans == "windows" or ans == "lumia":
        operSys = "gates"
    else:
        print("I did not understand your input, please try again.")
        deviceOS()


def connect():  # Connectivity issues?
    ans = str.lower(str(input("Is your 4g/wifi working?\n>")))
    if (ans == "no" or ans == "n"):
        print("Try turning your device off and on again.")
        ans = str.lower(str(input("Did this fix it?\n>")))
        if (ans == "no" or ans == "n"):
            warrantyInsure()
        elif (ans == "yes" or ans == "y"):
            print("Thanks for using this program; see you around!")
            sys.exit()
        else:
            print("Sorry, I did not understand your input.")
            print("Unfortunately, We will have to restart this whole question.")
            connect()
    elif (ans == "yes" or ans == "y"):
        print("Your issue is currently not interperatable or solvable.")
        try:
            outPutter("main")
            print("Your issue was written to file a file in the userprob"
            " folder.")
            print("Please send that file to the developers when you get a "
            "chance.")
        except:
            print("Error was encountered while trying to write file.")
            print("Your issue may have been written to a file, or it may have "
            "not.")
        print("Thank you for using this program.\nGoodbye now!")
        sys.exit
    else:
        print("Sorry, I did not understand your input.")
        connect()


def main():  # main function
    global operSys
    global userProb
    global aindex
    deviceOS()
    keywords = ("infection","virus","malware","infected","broken","shattered",
    "smashed","cracked","black","off","charge","dead","isn't on","wifi","4g",
    "internet","water","wet","toilet","end")
    userProb = str.lower(str(input("Please describe your issue\n>")))
    aindex = 0
    while keywords[aindex] not in userProb and aindex < 19:
        aindex += 1
    if aindex < 4:
        print("Problem detected: Infection.")
        infection()
    elif aindex >= 4 and aindex < 8:
        print("Problem detected: Broken Screen.")
        screenBroke()
    elif aindex >= 8 and aindex < 13:
        print("Problem detected: Battery/charge issues.")
        isScreenOn()
    elif aindex >= 13 and aindex < 16:
        print("Problem detected: Connectivity.")
        connect()
    elif aindex >= 16 and aindex < 19:
        print("Problem detected: Water.")
        deviceWater()
    elif aindex == 19:
        print("Your issue is currently not interperatable or solvable.")
        outPutter("main")
        print("Your issue was written to file a file in the userprob"
        " folder.")
        print("Please send that file to the developers when you get a "
        "chance.")
        # print("Error was encountered while trying to write file.")
        # print("Your issue may have been written to a file, or it may have "
        # "not.")
        print("Thank you for using this program.\nGoodbye now!")
        sys.exit
    else:
        print("I did not understand your input, please try again.")
        main()


print("DISCLAIMER: The developer(s) of this program accept no responsibility "
"for")
print("damage caused to your device due to instructions given.")
print("All advice given SHOULD be helpful and all attempts have been taken to "
"reduce")
print("likelyhood of damage, but we still take no responsibility.")


main()
