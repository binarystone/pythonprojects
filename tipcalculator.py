# tip calculator

amount = int(input("How much is the bill? "))
tip = amount * .12
newamount = tip + amount

print(f"Your new total is ${newamount}")