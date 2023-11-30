from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train_model(df: pd.DataFrame, model, model_name):
    """
    Train a regression model on the given DataFrame and return feature importance.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the dataset.
    - model: The regression model to be trained.
    - model_name (str): The name of the model ('Linear Regression' or 'Random Forest Regressor').

    Returns:
    - dict: A dictionary containing feature names and their corresponding importance scores.
    - pd.DataFrame: Scaled training features (X_train_scaled).
    - pd.Series: Training labels (y_train).
    """
    assert isinstance(df, pd.DataFrame), "Input 'df' must be a DataFrame."
    assert model_name in ['Linear Regression', 'Random Forest Regressor'], "Invalid model_name. Use 'Linear Regression' or 'Random Forest Regressor'."
    
    subset_df = df[['EV_perc', 'Median_Household_Income', 'Latino_perc', 'White_perc','Asian_perc', 'Black_perc', 'BachOrHigher_perc']]
    
    X = subset_df.drop('EV_perc', axis=1)
    y = subset_df['EV_perc']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    if model_name == 'Linear Regression':
        feature_importance_dict = dict(zip(X.columns, model.coef_ / model.coef_.sum() * 100))
    elif model_name == 'Random Forest Regressor':
        feature_importance_dict = dict(zip(X.columns, model.feature_importances_))
    
    return feature_importance_dict, scaler, X_train_scaled, y_train, model