from pickle import load
import streamlit as st
import os

model_file = "src/optimized_random_forest_model_1000estimators_max_depth5_min_samples_split5_min_samples_leaf2_42.sav"

if not os.path.exists(model_file):
    st.error(f"The file of the model {model_file} is not found. Make sure it i in the system")
else:
    # Load the saved model
    with open(model_file, "rb") as file:
        model = load(file)
    # Class dictionary: 
    class_dict = {
    0: "Iris setosa",
    1: "Iris versicolor",
    2: "Iris virginica"
}

    # Set application title
    st.title("Iris - Model prediction")

    # Silders to collect user data entry

    val1 = st.slider("Petal width", min_value=0.1, max_value=2.5, step=0.1)
    val2 = st.slider("Petal length", min_value=1.0, max_value=7.0, step=0.1)
    val3 = st.slider("Sepal width", min_value=2.0, max_value=4.5, step=0.1)
    val4 = st.slider("Sepal length", min_value=4.0, max_value=8.0, step=0.1)

    # Precict button
    if st.button("Predict"):
        try: 
            prediction = model.predict([[val1, val2, val3, val4]])[0]
            pred_class = class_dict.get(prediction, "Unkown class")
            st.write("Prediction:", pred_class)
        except Exception as e:
            st.error(f"Failed predicting: {e}")