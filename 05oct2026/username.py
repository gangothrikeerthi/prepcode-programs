blocked=["admin","root","user"]
username=input("enter username:")
if username not in blocked:
   print("username allowed")
else:
    print("username blocked")
