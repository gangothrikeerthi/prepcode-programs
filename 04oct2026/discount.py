datas=input()
data=datas.split()
price=int(data[0])
dis=int(data[1])*price/100
final_price=price-dis
print(final_price)