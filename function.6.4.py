#(Display an integer reversed)
def reverse_number(n) :
    reversed_num = 0

    while n > 0 :
        a = n % 10
        reversed_num = (reversed_num * 10) + a
        n //= 10
    return reversed_num
    
def main():

    number = eval(input( "Enter the integer number :"))
    reversed_number = reverse_number (number)
    print(reversed_number)

main()