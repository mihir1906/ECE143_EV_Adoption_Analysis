from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train_model(df: pd.DataFrame, features: list, target_feature: str, model, model_name: str):
    """
    Train a regression model on the given DataFrame and return feature importance.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the dataset.
        features    (list): List of features from the datatset that you want to use for training.
        target_feature  (str): feature that has to be predicted.
        model: The regression model to be trained.
        model_name (str): The name of the model ('Linear Regression' or 'Random Forest Regressor').

    Returns:
        feature_importance   (dict): A dictionary containing feature names and their corresponding importance scores.
        r2  (float): R2 Score for the model on test data
        mse (float): Mean Squared Error for the model on test data
        scaler  : The scaler that was used to scale the train data
        model   : The trained model instance
    
    """
    assert isinstance(df, pd.DataFrame), "Input 'df' must be a DataFrame."
    assert isinstance(features, list) and isinstance(model_name, str) and isinstance(target_feature, str)
    assert target_feature in list(df.columns)
    assert model_name in ['Linear Regression', 'Random Forest Regression'], "Invalid model_name. Use 'Linear Regression' or 'Random Forest Regressor'."
    
    subset_df = df[features]
    
    X = subset_df.drop(target_feature, axis=1)
    y = subset_df[target_feature]

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
    elif model_name == 'Random Forest Regression':
        feature_importance_dict = dict(zip(X.columns, model.feature_importances_))
    
    return feature_importance_dict, r2, mse, scaler, model