
if 1==1:
    print("this is correct")
else:
    print("this is wrong")

if 1<=2 and 1==1:
    print("this is correct")

else:
    print("this is wrong")



marks = 90
if marks>=90 and marks<=100:
    print("this is distincation")
elif marks>=60 and marks<80: 
    print("first division")
elif marks>=50 and marks<60:
    print("second dvision")
else:
    print("fail or wrong input")

print("__________"*3)
mark = 90
if mark>=90 and mark<=100:
    print("distinsion")
    if mark == 100:
     print("toppper")

    elif mark == 80:
     print("lucky")

data = "male"

data = "male" if data == "male" else "female"
print(data)

print("_________"*8)

mark = int(input("enter mark  "))
attendent = int(input("enter your attendent "))
income = int(input("enter mark  "))

if marks<=85:
    if attendent>=90:
        if income<300000:
            print("full scholarship")
        else:
            print("half scholarship")
    else:
        print("low attendence")
else:
    print("no scholarship")
 
         