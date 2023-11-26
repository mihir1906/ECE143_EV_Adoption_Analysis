def fun_clean(data_set):
    """
     Detailed Description:
     The following function cleans the data frame by replacing the missing values with the mean value.
     
     Parameters:
    - data_set (pd.DataFrame): It is an uncleaned data frame.

    `Returns:
    - pd.DataFrame: Returns cleaned data frame
    
    """
    assert isinstance(data_set , pd.core.frame.DataFrame)
    
    data_set["Median_Household_Income"].fillna(np.mean(data_set["Median_Household_Income"]), inplace = True)
    data_set["Zillow_Home_Value_Index"].fillna(np.mean(data_set["Zillow_Home_Value_Index"]), inplace = True)
    return data_set
    