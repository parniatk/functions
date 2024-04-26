#(The condition of being a triangle and printing its area)

# Returns true if the sum of both sides is greater than the third side

def is_Valid(num1, num2, num3):
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1 :
        return True
    else :
        return False
# Returns the area of the triangle

def triangle_area (num1 , num2 , num3):
    s = (num1 + num2 + num3) / 2
    area = (s * (s - num1) * (s - num2) * (s - num3)) ** 0.5
    return area

def main():
    num1 = eval(input("Enter the first nume: "))
    num2 = eval(input("Enter the second num: "))
    num3 = eval(input("Enter the third num: "))

    if is_Valid(num1,num2 , num3) :
        area = triangle_area(num1 , num2 , num3)
        print(f"The area of the triangle is: {area:.2f}")
    else:
        print("Invalid input. The sides do not form a valid triangle.")

main()