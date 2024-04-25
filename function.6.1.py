#pentagonal numbers

def get_pentagonal_number(n):
    return n * ((3 * n) - 1) // 2

#A new function to display the obtained numbers as 10

def display_pentagonal_number (start , end , in_each_row=10) :
    count = 0
    for n in range( start , end + 1) :
        num = get_pentagonal_number(n)
        count+=1
        print(f'{num}', end =" ")
        if count % in_each_row == 0 :
            print()

display_pentagonal_number(1 , 100)