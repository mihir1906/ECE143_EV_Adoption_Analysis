import pandas as pd

def make_predictions(model, scaler, input_data, X_train_scaled=None, y_train=None, fit_model=True):
    """
    Make predictions using the trained regression model.

    Parameters:
    - model: The trained or untrained regression model.
    - scaler: The MinMaxScaler used for scaling during training.
    - input_data (pd.DataFrame): The DataFrame containing the input features for prediction.
    - X_train_scaled: Scaled training features (only required if fit_model=True).
    - y_train: Training labels (only required if fit_model=True).
    - fit_model (bool): If True, fit the model before making predictions. Default is True.

    Returns:
    - pd.Series: Predicted values.
    """
    assert isinstance(input_data, pd.DataFrame), "Input 'input_data' must be a DataFrame."

    if fit_model:
        assert X_train_scaled is not None and y_train is not None, "X_train_scaled and y_train must be provided if fit_model=True."
        # Fit the model using the same scaler used during training
        assert hasattr(model, 'fit'), "Model must have a 'fit' method for training."
        model.fit(X_train_scaled, y_train)

    # Scale input data using the same scaler used during training
    input_data_scaled = scaler.transform(input_data)

    # Make predictions
    predictions = model.predict(input_data_scaled)

    return pd.Series(predictions, name='Predicted_EV_perc')