#(Palindrome integer)
#به واژه , جمله، عدد،یا هر چیز دیگری که خواندن آن از چپ به راست یا از راست به چپ کاملاً یکسان باشد پالیندروم میگویند
def isPalindrome(s):
 
    for i in range(0, int(len(s)/2)):
 
        if s[i] != s[len(s)-i-1]:
 
            return False
 
    return True

def main() :

    s = input("Enter the number :")

    if isPalindrome(s):

        print(f"{s} is palindrome ")
        
    else:

        print(f"{s} is not palindrome ")
main()