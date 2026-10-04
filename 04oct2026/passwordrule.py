password=input("enter password:")
if len(password)>=8 and any(not c.isalum() for c in password):
      print("valid password")
else:
      print("invalid password")