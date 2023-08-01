q = input("Are you UWS student?(yes/no)")
if q == "yes":
    print("Free")
else: 
    n = int(input("How old are you?"))
    if n < 18:
        print("£24")
    elif n > 18:
        print("£44")