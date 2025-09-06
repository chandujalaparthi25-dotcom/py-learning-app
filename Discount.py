total =int(input("Enter the total bill: "))
if total >= 1000:
   discount = total * 0.10
else:
   discount = total * 0.5
final = total - discount 
print("Discount applied, discount", discount)
print("Amount to pay", final)


   

