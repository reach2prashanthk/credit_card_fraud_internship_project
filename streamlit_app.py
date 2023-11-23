import streamlit_app as st
import joblib
import numpy as np

# Load the model
loaded_model = joblib.load("C:\\Users\\prash\\OneDrive\\Documents\\temp\\credit_card_fraud\\saved_models\\0\\model\\model.pkl")

# Title for the app
st.title('Machine Learning Model Deployment with Streamlit')

def fraud_prediction(features):
    prediction = loaded_model.predict(features.reshape(1, -1))
    return prediction

input_df = st.text_input('Input all features (comma-separated total 29 features )')

# Create a button to submit and get predictions
submit = st.button('Submit')

if submit:
    input_df_lst = input_df.split(',')
    try:
        features = np.array(input_df_lst, dtype=np.float)
        prediction = fraud_prediction(features)
        if prediction[0] == 0:
            st.write("Legitimate transaction")
        else:
            st.write("Fraudulent Transaction")
    except ValueError:
        st.write("Please enter valid input for all features")
