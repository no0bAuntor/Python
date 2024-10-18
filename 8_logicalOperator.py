# or
temp=25
is_raining=True

if temp>35 or temp<0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")    



# and
temp=30
is_sunny=True

if temp>=28 and is_sunny:
    print("Very hot 🥵")
else:
    print("Can go outside")    

# not
temp=15
if 10<temp<20 and not is_sunny:
    print("very cold")
else:
    print("warm weather")    