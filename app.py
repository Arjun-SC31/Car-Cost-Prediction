# Importing Libraries

import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib

pickle_in = open('30_model.pkl', 'rb')
predictor_model = pickle.load(pickle_in)

#data = pd.read_csv('car_dataset.csv')

def Car_predict(Km_driven, fuel_type, transmission_type, owners, Mileage, Engine, Max_power, Seats, Torque, Age, seller_type_Individual, seller_type_Trustmark_Dealer):
    prediction = predictor_model.predict([[Km_driven, fuel_type, transmission_type, owners, Mileage, Engine, Max_power, Seats, Torque, Age, seller_type_Individual, seller_type_Trustmark_Dealer]])
    return prediction


def main():
    
    st.title("Trying to sell a car?")
    html_temp = """
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h3 style = 'color: white; text-align: center;'>Use this ML-based App to find out how much it's worth!</h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    st.text_input("Enter your Name: ", key="name")
    
    #if st.checkbox('Show the dataset'):
     #   data


    st.subheader("Please enter the required information below.")
    
    # Enter the km driven value
    Km_driven = st.text_input('Kilometers driven', 'Enter Km driven')

    # Input for fuel type
    Fuel = st.selectbox('Enter Fuel type: ', options=['Diesel', 'Petrol', 'LPG', 'CNG'])

    fuel_type = 0
    if Fuel == 'Petrol':
        fuel_type = 1
    elif fuel_type == 'LPG':
        fuel_type = 2
    elif fuel_type == 'CNG':
        fuel_type = 3
    else:
        fuel_type = 4
        

    # Input for transmission
    Transmission = st.selectbox('Enter Transmission type: ', options = ['Manual', 'Automatic'])

    transmission_type = 0
    if Transmission == 'Manual':
        transmission_type = 1
    else:
        transmission_type = 2

    # Input for owner
    Owner = st.selectbox('Enter the number of previous owners: ', options = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner',
 'Test Drive Car'])

    owners = 0
    if Owner == 'First Owner':
        owners = 5
    elif Owner == 'Second Owner':
        owners = 4
    elif Owner == 'Third Owner':
        owners = 3
    elif Owner == 'Fourth & Above Owner':
        owners = 2
    else:
        owners = 1

    # Input for mileage
    Mileage = st.slider('Enter the car mileage in km: ', 0, 60, 1)

    # Input for engine
    Engine = st.slider('Enter the engine capacity(CC): ', 0, 4000, 50)

    # Input for max_power
    Max_power = st.slider('Enter the max power generated by your vehicle: ', 0, 500, 5)

    # Input for seats
    Seats = st.slider('Enter the number of seats in your vehicle: ', 2, 15, 1)

    # Input for torque
    Torque = st.slider('Enter the torque generated by your vehicle(Nm): ', 25, 1000, 5)

    # Input for Age
    Age = st.slider('Enter how old your vehicle is (in Years): ', 1, 30, 1)

    # Input for seller type
    Seller = st.selectbox('Enter Seller type: ', options=['Individual' , 'Trustmark Dealer' , 'Dealer'])

    seller_type_Individual, seller_type_Trustmark_Dealer = 1, 1

    if Seller == 'Individual':
        seller_type_Trustmark_Dealer = 0

    elif Seller == 'Trustmark Dealer':
        seller_type_Individual = 0
    else:
        seller_type_Individual = 0
        seller_type_Trustmark_Dealer = 0

    result = ''

    if st.button('Estimate Car Price'):
        result = Car_predict(Km_driven, fuel_type, transmission_type, owners, Mileage, Engine, Max_power, Seats, Torque, Age, seller_type_Individual, seller_type_Trustmark_Dealer)
        st.success('Your car is approximately worth: ${}'.format(str(int(result/80))))
        st.write(f'Thank you {st.session_state.name}! I hope you liked it.')

    
    



if __name__ == '__main__':
    main()
    st.write(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.write(f"Here is my [Personal Website](https://arjun-sc31.github.io)")
