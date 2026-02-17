print("hey there what do you want to do ")

e= 1==1
while e:
    a = int(input("enter the first value "))
    b = int(input("enter the second value "))
    c = int(input("which opration do you want to do \n 1.+ \n 2.- \n 3.* \n 4./ \n 5.% \n"))
    d = (a+b)
    if c < 6:
     match c:
        case 1:
            print("your answer is ", a+b)
        case 2:
            print("your answer is ", a-b)
        case 3:
            print("your answer is ", a*b)
        case 4:
            print("your answer is ", a/b)
        case 5:
            print("your answer is ", a%b)
else :
    print("your giving wrong input")

      
