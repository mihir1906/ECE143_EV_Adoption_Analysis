import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your CSV file into a DataFrame
df = pd.read_csv('data\final_ev_analysis.csv')  # Replace 'your_file.csv' with the actual path to your CSV file

# Select features (X) and target variable (y)
features = df[['Median_Household_Income', 'County']]  # Replace with relevant feature columns
target = df['Total_EV']  # Replace with the target variable column (Total_EV or EV_perc)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Extract feature coefficients (for linear models)
coefficients = pd.DataFrame({'Feature': features.columns, 'Coefficient': model.coef_})
print(coefficients)
