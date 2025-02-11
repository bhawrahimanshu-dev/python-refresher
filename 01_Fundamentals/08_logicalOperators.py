# and 	Returns True if both statements are true	                x < 5 and  x < 10	
# or	Returns True if one of the statements is true	            x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

temp =25
is_raining = False 
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")



temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside🥵")
    print("It is SUNNY☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside🥶")
    print("It is SUNNY☀️")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside😊")
    print("It is SUNNY☀️")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY ☁️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY ☁️")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY ☁️")