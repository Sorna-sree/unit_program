seed_prize=70 
labour_charge=50
oil_price=200
punnaku_prize=40

def get():
    quantity=int(input("Enter the oil quantity needed in liters: "))
    if(quantity<=0): 
        print("Invalid input")

    elif(quantity>=1):
        preparation_cost=quantity*2*70 +labour_charge #1*2*70+50=190 
        total_oil_cost=quantity*oil_price #calculate the sales oil prize
        other=quantity*punnaku_prize # other profit of punnaku sales
        total=total_oil_cost+other  
        profit=total-preparation_cost 
        print(f"{quantity} liter preparation amount is ",preparation_cost)
        print("punnaku sales amount: ",other)
        print("The total amount is: ",total)
        print(f"{quantity} litter oil cost is: ",total_oil_cost)
        print("The profit is: ",profit)
    
get() #funtion call


