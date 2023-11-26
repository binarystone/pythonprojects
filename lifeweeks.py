age = int(input("How old are you? "))
life_expectancy = int(input("What is your expected life expectancy? "))

lifeweeks = age * 52
remainingweeks = (life_expectancy - age) * 52

print (f"You have already lived {lifeweeks} weeks")

print ("You have " + str(remainingweeks) + " weeks left")

print ("Live life to the fullest :)")