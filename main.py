import sys
__author__ = "George Kokinis"
__maintainer__ = "George Kokinis"
__email__ = "george.kokinis@gmail.com, gkokinis@kes.sheffield.sch.uk"
__status__ = "Release"
__version__ = 1.02


def main():
    ans = str.lower(str(input("Which task do you want to launch?\n>")))
    if ans == "1" or ans == "one":
        import task1
        task1.deviceOS()
    elif ans == "2" or ans == "two":
        import task2
        task2.main()
    elif ans == "3" or ans == "three":
        import task3
        task3.main()
    else:
        print("Sorry, we did not understand your input.")
        main()
    sys.exit


main()
