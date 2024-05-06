import pandas as pd
import pickle
import streamlit as st


#df = pd.read_csv("path_to_your_dataset.csv")
df = pd.read_csv("C:/Users/jaya2/OneDrive/Documents/final data.csv")


def manual_testing(date, district):
    # Filter the DataFrame based on date and district
    filtered_data = df[(df['Accident Date'] == date) & (df['District Area'] == district)]
    
    
    
    # For now, let's return the filtered data as a placeholder
    return filtered_data

def main():
    st.title("Accident Prediction Web App")

    # User input for date and district
    date = st.text_input("Enter a date (dd-mm-yyyy format):")
    district = st.text_input("Enter district:")

    if st.button("Predict Road Accident"):
        # Perform manual testing and get the result
        accident_data = manual_testing(date, district)
        
        # Display the prediction result
        st.success("Prediction Result:")
        st.write(accident_data)

if __name__ == '__main__':
    main()
try:
    df = pd.read_csv("C:/Users/jaya2/OneDrive/Documents/final data.csv")
    # Proceed with further processing of the DataFrame 
except Exception as e:
    print("Error reading CSV file:", e)

    

