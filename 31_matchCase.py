# 1

def day_of_week(day):
    match day:
        case 1:
            return "It is Saturday"
        case 2:
            return "It is Sunday"            
        case 3:
            return "It is Monday"    
        case 4:
            return "It is Tuesday"        
        case 5:
            return "It is Wednesday"
        case 6:
            return "It is Thursday"            
        case 7:
            return "It is Friday"
        case _:
            return "Invalid day"
        

print(day_of_week(1))        


# 2
def is_weekend(day):
    match day:
        case "Sunday" | "Monday" | "Tuesday" | "Wednesday" | "Thursday":
            return False
        case "Friday" | "Saturday":
            return True
        
        case _:
            print("Invalid day")    

print(is_weekend('Saturday'))
