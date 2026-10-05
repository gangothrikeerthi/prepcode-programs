price=float(input("enter product price:"))
quantity=int(input("enter quantity:"))
member=input("are you a member?")
coupon=input("o you have a valid coupon?")
total=price* quantity
if member=="yes":
    total-=total * 10/100
if coupon=="yes":
    total-=total * 5/100
print("final payable amount=",total)