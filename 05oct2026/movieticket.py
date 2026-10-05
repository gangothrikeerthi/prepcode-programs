age=int(input("enter age:"))
price=200
if age < 12:
    price=price-(price*50/100)
elif age >=60:
    price=price-(price*30/100)
print("ticket price=",price)