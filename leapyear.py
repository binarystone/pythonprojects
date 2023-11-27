# LEAP YEAR CALCULATOR

year = int(input("Enter the year: "))

fourhundred = year % 400
onehundred = year % 100
four = year % 4
print (fourhundred)
    
if (fourhundred != 0):
    print("Could be")
elif (onehundred != 0):
    print("maybe")
else:
    print("dont think so")
    

# if year % 400 != 0:
#     print("COULD BE")
# elif year % 100 == 0:
#     print("NOPE")
# elif year % 4 == 0:
#     print("LEAP YEAR")

# else:
#     "NOT A LEAP YEAR"