import streamlit as st
from streamlit_option_menu import option_menu

class PhonepeMain(): 
    
    # Setting Wider Page Layout and Title
    st.set_page_config(layout="wide")
    st.title("PhonePe Pulse") 
    
    # Horizontal Menu
    Selected = option_menu(menu_title="Dashboard",
                menu_icon="bi bi-speedometer2"
                ,orientation="horizontal",
                options=["Insurance","Payments"],
                icons=["bi bi-hospital","bi bi-currency-rupee"])
    
    
    if Selected =="Insurance":
        
        #Splitting the page into three columns
        col1,col2,col3 = st.columns(3,gap="Small")
        
        col1.subheader("All India Policies")
        Year = col1.selectbox("Select Year",options=["2020","2021","2022","2023"])
        Quarter =col1.selectbox("Select Quarter",options=["Q1(Jan - Mar)","Q2(Apr - Jun)","Q3(Jul - Sep)","Q4(Oct - Dec)"])
    
        col2.map()
        
        col3.header("Insurance")
        col3.text("All India Insurance Policies Purchased (Nos.)")
        col3.text("Total Premium Value")  
        col3.text("Average Premium Value")   
        
        col3.divider()
        col3.tabs = st.tabs(["States","Districts","Postalcodes"])
        
    if Selected =="Payments":
        st.write(f"welcome to {Selected} dashboard")
    

    
    
    
    