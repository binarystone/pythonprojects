# calculate tithe

salary = int(input("How much did you earn this month? "))
tip = salary * .10
remainingsalary = salary - tip

print (f"Your tithe is {tip}")
print (f"Your remaining salary is {remainingsalary}")