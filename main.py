import sys
__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Release"
__version__ = 1.04


def main():
    print("DISCLAIMER: The developer(s) of this program accept no "
          "responsibility for")
    print("damage caused to your device due to instructions given.")
    print("All advice given SHOULD be helpful and all attempts have been "
          "taken to reduce")
    print("likelyhood of damage, but we still take no responsibility.")
    ans = str.lower(str(input("Which task do you want to launch?\n>")))
    if ans == "1" or ans == "one":
        try:
            import task1
            print("Task1 loaded.")
        except:
            print("Error occured while loading task1\nWe will now exit.")
            sys.exit
        task1.deviceOS()
    elif ans == "2" or ans == "two":
        try:
            import task2
            print("Task2 loaded.")
        except:
            print("Error occured while loading task2\nWe will now exit.")
            sys.exit
        task2.main()
    elif ans == "3" or ans == "three":
        try:
            import task3
            print("Task3 loaded.")
        except:
            print("Error occured while loading task3\nWe will now exit.")
            sys.exit
        task3.main()
    else:
        print("Sorry, we did not understand your input.")
        main()
    sys.exit


main()
