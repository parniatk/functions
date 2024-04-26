#(Sort three numbers)
def display_Sorted_Numbers(num1, num2, num3):

#Using the list to sort
    numbers = sorted([num1 , num2 , num3])

    print(numbers)

def main () :
    #Get the number from the user
    num1 = eval(input("Enter the first number :"))
    num2 = eval(input("Enter the second number :"))
    num3 = eval(input("Enter the third number :"))

    display_Sorted_Numbers (num1, num2 , num3 )
main()

