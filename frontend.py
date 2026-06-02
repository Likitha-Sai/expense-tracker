from backend import add_expense,view_expense,filter_by_category,update_expense,show_total,delete_expense,show_graph,monthly_summary

import streamlit as st
st.title("Expense tracker")
option=st.selectbox("choose an option",
             ("Add Expense",
              "View Expense",
              "Filtered Expense",
              "Update Expense",
              "show total",
              "Delete Expense",
              "show graph",
              "monthly_summary",
              "Exit"))
if(option=="Add Expense"):
    amount_f=st.number_input("amount : ")
    category_f=st.text_input("category: ")
    

    description_f=st.text_input("description: ")
    date_f=st.date_input("date: ")
    add=st.button("add expense")
    if add:
        add_expense(amount_f,category_f,description_f,date_f)
        st.write("added successfully")
        
if(option=="View Expense"):

    view=st.button("view all expenses")
    if view:
        data=view_expense()
        st.table(data)
        
if(option=="show graph"):
    a=show_graph()
    st.pyplot(a)




if(option=="Filtered Expense"):
    filtered=st.button("view only specific category expenses")
    filter_category=st.selectbox("choose the category of expenses to view",
                                      ("food",
                                       "stationary",
                                       "purchasings"))
    if filtered:
        output=filter_by_category(filter_category)
        st.table(output)
if(option=="Update Expense"):
    data=view_expense()
    for i,expense in enumerate(data):
        st.write(f"{i}->{expense}")
    
    choose_f=st.number_input("choose the index to update : ")
    updation_field_f=st.selectbox("field to update",
                                    ("amount",
                                    "category",
                                    "description"))
    if(updation_field_f=="amount"):
        what_to_update_f=st.number_input("what to update : ")
    else:
        what_to_update_f=st.text_input("what to update : ")
    update=st.button("update")
    if update:
        
        update_expense(choose_f,updation_field_f,what_to_update_f)
        st.write("updated")
if(option=="show total"):
    total=st.button("total")
    if total:
        a=show_total()
        st.write(a)
if(option=="monthly_summary"):
    
    data = monthly_summary()

    st.write(data)
if(option=="Delete Expense"):
    a=view_expense()
    st.table(a)
    delete=st.button("delete")
    if delete:
        what_to_delete_f=st.number_input("select the index yo want to delete : ")
        delete_expense(int(what_to_delete_f))
if(option=="Exit"):
    st.write("Hava a good day..bye")

    




