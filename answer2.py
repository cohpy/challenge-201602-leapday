# Bennett Wenger
# bexreal1@gmail.com
# 2/29/2016
# Python Group Challenge

# imports
import calendar

# methods

# main menu
def main_menu():
    print("***** Leap Day Convergence Calculator *****")
    print("\nIt's February 29th, 2016.")
    print("This week's python meet is happening on Leap Day!")
    print("Using Python, we'll calculate when this \namazing occurence will happen next.")
    input("\nPress [Enter] to get to it!")
    
# exit prompt
def exit_prompt():
    input("\nPress [Enter] to exit.")

# calculate
def calculate():
    # Parameters:
    # Python meets happen on the last Monday of each month.
    # Leap Day happens every fourth year.

    # declare containers
    febList = []
    fifthWeek = []

    # other declarations
    controlBool = True
    myYear = 2016

    # loop through time
    while (controlBool):
        myFebruary = calendar.monthcalendar(myYear, 2)
        febList = myFebruary
        listLength = len(febList)

        # specify the search
        if (listLength == 5):
            fifthWeek = febList[4]
            myMonday = fifthWeek[0]
            
            # test for a convergence
            if ((myYear > 2016) and (myMonday == 29)):
                break

        # increment year            
        myYear += 1

    print("\nThe next Leap Day Python Meet \nwill occur on February 29, " + str(myYear))

# main logic
main_menu()
calculate()
exit_prompt()

# end of program
