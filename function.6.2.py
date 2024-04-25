#(Sum the digits in an integer)
def sum_digit(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10 
    return s

def main():
    num = eval(input( "Enter the int number : "))
    if num < 0 :
        print(f"entered number {num} is negative ")
    else :
        sum_of_gidits = sum_digit(num)
        print(f"sum of number {num} = {sum_of_gidits}")
        
main()