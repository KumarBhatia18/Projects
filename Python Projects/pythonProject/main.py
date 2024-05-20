# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date
import calendar
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Welcome to Python ' +name)  # Press Ctrl+F8 to toggle the breakpoint.
    print("Today's date is " + str(date.today()))
    print("Today day is" +str(date.today().day))
    print(calendar.day_name[date.today().weekday()])

    if(int(date.today().day) > 8):
        print("Yes")

# Press the green button in the gutter to run the script.
print_hi('Takshika')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
