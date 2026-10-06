weight =  int (input("weight: "))
unit = input("(k)g or (L)bs:")
if unit.upper() == "K":
    converted = weight /0.45
    print("weight in Lbs: "+str( converted))  
    converted = weight * 0.45
    print("weight in  Kgs: "+str (converted))