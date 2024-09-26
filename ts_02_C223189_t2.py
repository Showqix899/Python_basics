

#input the mark
mark = int(input("Enter your mark: "))

#check if the mark is valid
if mark <= 0 and mark >=100:
    #checking the mark is over 80 or not
    if mark>=80:
        print("Grade: A")

    #checking the mark is greater then 60 or less then 80
    elif mark>=60 and mark < 80:
        print("Grade: B")

    #checking the mark is greater then 60 or less then 80
    elif mark>=40 and mark <60:
        print("Grade: C")
    #checking if the mark is below 40
    else:
        print("Grade: F")
#invalid marks
else:
    print("Invalid mark")