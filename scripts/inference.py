import pandas as pd
import numpy as np

def make_predictions(model, scaler, input_data):
    """
    Make predictions using the trained regression model.

    Parameters:
        model: The trained or untrained regression model.
        scaler: The MinMaxScaler used for scaling during training.
        input_data (pd.DataFrame): The DataFrame containing the input features for prediction.

    Returns:
        pd.Series: Predicted values.
    """
    assert isinstance(input_data, (np.ndarray, pd.DataFrame)), "Input 'input_data' must be a DataFrame."
    assert hasattr(model, 'predict'), "Model instance has no method called 'fit'"
    assert hasattr(scaler, 'transform'), "Scaler instance has no attribute 'transform'"
    
    # Scale input data using the same scaler used during training
    input_data_scaled = scaler.transform(input_data)

    # Make predictions
    predictions = model.predict(input_data_scaled)

    return pd.Series(predictions, name='Predicted_EV_perc')