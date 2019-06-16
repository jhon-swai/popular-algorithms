# A Python 3 program to implement
# the Tomohiko Sakamoto Algorithm
# function to implement tomohiko
# sakamoto algorithm
def day_of_the_week(y,  m, d) :

    # array with leading number of days values
    t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ]

    # if month is less than 3 reduce year by 1
    if (m < 3) :
        y = y - 1
    #calculating the day
    day = (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7
    #Creating an array list of days
    day_array = ["Sunday","Monday", "Tuesday","wednesday","Thursday","Friday","Saturday"]

    return day_array[day]



# Driver Code
def takeDate():
    global day
    global month
    global year

    try:
        print("Enter the day of the weel")
        day = int(input())
        print("Enter the month")
        month = int(input())
        print("Enter the year")
        year = int(input())
    except:
        print("You have entered invalid data. Please enter again.")
        takeDate()
takeDate()

print(day_of_the_week(year, month, day))
