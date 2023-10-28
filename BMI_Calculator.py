print("*****Welcome to BMI Calculator****\n")
# name=input("Please Enter Your Name: ")
op=1
while(op):
    weight=float(input("Please Enter Your Weight(In KG's): "))
    height=float(input("Please Enter Your Height(In Meters): "))
    bmi=round(weight/(height**2),2)
    print(bmi)
    if (bmi <18.5):
        print("BMI = {bmi} \n *****Your are Under-Weighted*****")
    elif (bmi >= 18.5 and bmi <= 25):
        print("BMI = {bmi} \n *****Your Weight is Normal*****")
    elif (bmi > 25 and bmi <= 30):
        print("BMI = {bmi} \n *****Your are Over-Weighted*****")
    elif (bmi > 30 and bmi <= 40):
        print("BMI = {bmi} \n *****Your are Obesed*****")
    elif (bmi > 40):
        print("BMI = {bmi} \n *****Your are Heavily-Obesed*****")
    else:
        print("*****Invalid Input*****")
    op=bool(input("Enter 0 to Exit: "))
    if(op==0):
        break
        
