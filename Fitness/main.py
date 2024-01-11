import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict exercise based on input attributes
def predict_exercise(attributes):
    # Convert input data to a DataFrame
    input_data = pd.DataFrame([attributes])
    
    # Use the pre-trained model to make predictions
    predicted_exercise = model.predict(input_data)
    
    return predicted_exercise[0]

# Streamlit UI
st.title('Exercise Recommendation App')

# # User input for attributes
age = st.slider('Age', 18, 80, 30)
# gender = st.selectbox('Gender', ['Male', 'Female'])
# fitness_level = st.selectbox('Fitness Level', ['Beginner', 'Intermediate', 'Advanced'])
# health_condition = st.selectbox('Health Condition', ['Poor', 'Fair', 'Good', 'Excellent'])
# fitness_goal = st.selectbox('Fitness Goal', ['Weight Loss', 'Muscle Gain', 'General Fitness'])
# calories_intake = st.slider('Calories Intake', 1000, 3000, 2000)
# bmi = st.slider('BMI', 15.0, 40.0, 25.0)
# ex= st.selectbox('Strength Training	', ['Strength Training	', 'Cardio'])
# import streamlit as st

gender_mapping = {'Male': 1, 'Female': 0}
fitness_level_mapping = {'Beginner': 0, 'Intermediate': 1, 'Advanced': 2}
health_condition_mapping = {'Poor': 0, 'Fair': 1, 'Good': 2, 'Excellent': 3}
fitness_goal_mapping = {'Weight Loss': 0, 'Muscle Gain': 1, 'General Fitness': 2}
exercise_mapping = {'Strength Training': 0, 'Cardio': 1}

gender = st.selectbox('Gender', ['Male', 'Female'])
fitness_level = st.selectbox('Fitness Level', ['Beginner', 'Intermediate', 'Advanced'])
health_condition = st.selectbox('Health Condition', ['Poor', 'Fair', 'Good', 'Excellent'])
fitness_goal = st.selectbox('Fitness Goal', ['Weight Loss', 'Muscle Gain', 'General Fitness'])
calories_intake = st.slider('Calories Intake', 1000, 3000, 2000)
bmi = st.slider('BMI', 15.0, 40.0, 25.0)
ex = st.selectbox('Strength Training', ['Strength Training', 'Cardio'])

# Mapping selected values to numerical values
gender_numeric = gender_mapping[gender]
fitness_level_numeric = fitness_level_mapping[fitness_level]
health_condition_numeric = health_condition_mapping[health_condition]
fitness_goal_numeric = fitness_goal_mapping[fitness_goal]
exercise_numeric = exercise_mapping[ex]

# Use the numerical values in your further processing

# Combine user inputs into a dictionary
user_attributes = {
    'Age': age,
    'Gender': gender_numeric,
    'Fitness-Level': fitness_level_numeric,
    'Health Condition': health_condition_numeric,
    'Fitness Goal': fitness_goal_numeric,
    'Calories Intake': calories_intake,
    'BMI': bmi,
    'Exercise': exercise_numeric
}

# # Display the user inputs
# st.subheader('User Input:')
# st.write(user_attributes)

# Predict exercise based on user inputs
predicted_exercise1 = predict_exercise(user_attributes)
if predicted_exercise1==1.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Right Arm Biceps Curls, Left Arm Biceps Curls & Dumbell Lateral Raise ")
if predicted_exercise1==2.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Right Arm Biceps Curls, Left Arm Biceps Curls & Dumbell Lateral Raise ")

if predicted_exercise1==3.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Both Arm Bicep Curls, Over Head Dumbell Press & Pullups")
if predicted_exercise1==4.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Squarts, Pullups & Crunches")
if predicted_exercise1==5.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Cruches, Reverse Pushup from chair & Dumbell Rows")
if predicted_exercise1==0.0:
    st.subheader('Predicted Exercise:')
    st.subheader("Plank, Pushups & Reverse-Pushups")
if predicted_exercise1>=0.0:
    link = '[AI-TRAINNER](http://github.com)'
    st.markdown(link, unsafe_allow_html=True)
# Display the predicted exercise