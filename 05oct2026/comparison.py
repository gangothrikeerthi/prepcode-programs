p1=float(input("enter price of first product:"))
p2=float(input("enter price of second product:"))
if p1<p2:
    print("first product is cheaper")
elif p1>p2:
    print("first product is expensive")
else:
    print("both prices are same")
    