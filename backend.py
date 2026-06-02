#Expense tracker 
import json 
import pandas as pd
import matplotlib.pyplot as plt
expense_list=[] 
try: 
    with open("expense.json","r") as f: 
        expense_list=json.load(f) 
except: 
    with open("expense.json","w") as f: 
        expense_list=[] 
#print("1.Add Expense") 
#print("2.View Expense") 
#print("3.Filtered expenses")
#print("4.update expense")
#print("5.show total") 
#print("6.Delete Expense")
#print("7.Exit")
#userinput=int(input())
def add_expense(amount,category,description,date):
    
    #amount=int(input("amount:")) 
    #category=input("category:") 
    #description=input("description:") 
    expense_list.append({"amount":int(amount),"category":category,"description":description,"date":str(date)}) 
    with open("expense.json","w") as f: 
        b=json.dump(expense_list,f,indent=4)

def view_expense():
    
    return expense_list 
        
    
def filter_by_category(category):
    
    
    i=0
    l=[]
   
    while(i!=len(expense_list)):
        if(expense_list[i]["category"]==category):
            l.append(expense_list[i]) 
        i=i+1
    return l
            
                
        
def show_total():
    sum1=0
    
    i=0 
    while(i!=len(expense_list)): 
        sum1=sum1+int(expense_list[i]["amount"])
        i=i+1 
    return f"total is {sum1}"
def delete_expense(what_to_delete):
    #i=0
    #while(i!=len(expense_list)):
     #   print(f"{i} -> {expense_list[i]}") 
      #  i=i+1
    
    
    #what_to_delete=int(input())
    if(what_to_delete<len(expense_list)):
        expense_list.pop(what_to_delete)
        with open("expense.json","w") as f: 
            b=json.dump(expense_list,f,indent=4)
        
    else:
        print("no value at required index")
def update_expense(choose,updation_field,what_to_update):
    #i=0
    #while(i!=len(expense_list)):
     #   print(f"{i} -> {expense_list[i]}") 
      #  i=i+1
    #choose=int(input())
    #j=0
    #while(j!=len(expense_list)):
     #   if(j==choose):
            #updation_field=input("updation_field:")
                #what_to_update=input("what _to_update:")
    expense_list[int(choose)][updation_field]=what_to_update
        #j=j+1
    with open("expense.json","w") as f: 
            b=json.dump(expense_list,f,indent=4)
def show_graph():
    
    
    
    df=pd.DataFrame(expense_list)
    print(df)
    df["date"]=pd.to_datetime(df["date"])
    df["month"]=df["date"].dt.strftime("%Y-%m")
    grouped = df.groupby(["month", "category"])["amount"].sum()
    pivot=grouped.unstack(fill_value=0)
    fig,ax=plt.subplots()
    pivot.plot(kind="bar",ax=ax);

    return fig
def monthly_summary():
    df=pd.DataFrame(expense_list)
    df["date"]=pd.to_datetime(df["date"])
    df["month"]=df["date"].dt.strftime("%Y-%m")
    grouped = df.groupby(["month", "category"])["amount"].sum()
    pivot=grouped.unstack(fill_value=0)
    return pivot




        
    
"""userinput=0    
while(userinput!=6):
    #print("1.Add Expense") 
    #print("2.View Expense")
    #print("3.filtered expense")
    #print("4.update expense")
    #print("5.show total") 
    #print("6.Delete Expense")
    #print("7.Exit") 
    userinput=int(input())
    match userinput: 
        case 1:
            amount=int(input())
            category=input()
            description= input()
            add_expense(amount,category,description)
                 
        case 2:
            view_expense()
            
        case 3:
            category=input("choose the category you want to see : ")
            filter_by_category(category)
        case 4:
            choose=int(input())
            updation_field=input("updation_field:")
            what_to_update=input("what _to_update:")

            update_expense(choose,updation_field,what_to_update)
            
        case 5:
            show_total()
             
        case 6: 
            what_to_delete=int(input())
            delete_expense(what_to_delete)
        case 7:
            break"""