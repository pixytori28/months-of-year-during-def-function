# Name: victoria inahuazo
# Date: 04/12/24
# email: victoria.inahuazo11@myhunter.cuny.edu
# A program that uses functions to print out months.

def monthString(monthNumber):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     monthsofYear = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    # Return the month name directly from the list based on monthNumber
     if 1 <= monthNumber <= 12:
        return monthsofYear[monthNumber]
     else:
        return "Invalid month"  #in case if monthNumber is not in the range 1-12


def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)

#Allow script to be run directly:
if __name__ == "__main__":
     main()