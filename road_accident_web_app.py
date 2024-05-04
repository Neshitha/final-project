import pandas as pd
import pickle
import streamlit as st

# Load the pickled model
#loaded_model = pickle.load(open("C:/Users/jaya2/OneDrive/Desktop/final coapps project/accident_prediction.sav", 'rb'))

# Load your dataset (assuming you have a DataFrame named 'df')
# Replace 'path_to_your_dataset.csv' with the actual path to your dataset file
#df = pd.read_csv("path_to_your_dataset.csv")
df = pd.read_csv("C:/Users/jaya2/OneDrive/Desktop/final coapps project/dataset.csv")


def manual_testing(date, district):
    # Filter the DataFrame based on date and district
    filtered_data = df[(df['Accident Date'] == date) & (df['District Area'] == district)]
    
    # Perform prediction using the loaded model
    # Example: prediction = loaded_model.predict(filtered_data)
    # Replace the above line with your actual prediction logic
    
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
    df = pd.read_csv("C:/Users/jaya2/OneDrive/Desktop/final coapps project/dataset.csv")
    # Proceed with further processing of the DataFrame
except Exception as e:
    print("Error reading CSV file:", e)

    

