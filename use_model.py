from tensorflow.keras.models import load_model
import joblib


def btn_click(self, a, b, c):

    print(a)
    print(b)
    print(c)

    # Load our trained model
    model = load_model('salary_estimate.h5')

    # Load the data scalers so that we can transform new data and prediction the same way as training data.
    X_scaler = joblib.load('X_scaler.pkl')
    y_scaler = joblib.load('y_scaler.pkl')

    # Define the house that we want to value (with the values in the same order as in the training data).
    employee = [
        a,  # Geography
        b,  # Gender
        c,  # Age
    ]

    # Keras assumes we want to predict the values for multiple of houses at once, so it expects an array.
    # We only want to value a single house, so it will be the only item in our array.
    employees = [
        employee
    ]

    # Scale the new data like the training data
    scaled_emp_data = X_scaler.transform(employees)

    # Make a prediction for each house in the homes array (but we only have one)
    emp_values = model.predict(scaled_emp_data)

    # The prediction from the neural network will be scaled 0 to 1 just like the training data
    # We need to unscale it using the same factor as we used to scale the training data
    unscaled_emp_values = y_scaler.inverse_transform(emp_values)

    # Since we are only predicting the price of one house, grab the first prediction returned
    predicted_value = unscaled_emp_values[0][0]

    geography = "France"

    if employee[0] == 2:
        geography = "Germany"
    elif employee[0] == 3:
        geography = "Spain"

    gender = "Female"

    if employee[1] == 2:
        gender = "Male"

    # Print the results
    print("Employee details:")
    print(f"- Geography:  {geography}")
    print(f"- Gender:  {gender}")
    print(f"- Age:  {employee[2]}")
    print(f"Estimated Salary: ${predicted_value:,.2f}")

    text = f'A {employee[2]} year old {gender} in {geography} can expect to make ${predicted_value:,.2f}'

    result = text
    return result

