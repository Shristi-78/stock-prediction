import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess(file_path):
    """
    Standardizes data loading and missing value handling.
    """
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)
    
    # Handling missing values via forward fill as per EDA best practices
    df.fillna(method='ffill', inplace=True)
    return df

def create_features(df):
    """
    Generates lag variables and technical indicators for ML models.
    """
    df = df.copy()
    # Predicting Close price[cite: 2]
    df['Target'] = df['Close']
    df['Lag_1'] = df['Close'].shift(1)
    df['Lag_2'] = df['Close'].shift(2)
    df['MA_5'] = df['Close'].rolling(window=5).mean()
    df.dropna(inplace=True)
    return df

def get_timeseries_split(df, start_train, end_train, start_test, end_test):
    """
    Returns dataframes based on specific assignment regimes[cite: 2].
    """
    train = df.loc[start_train:end_train]
    test = df.loc[start_test:end_test]
    return train, test

def prepare_lstm_windows(data, window_size=60):
    """
    Reshapes data into [samples, time_steps, features] for Deep Learning[cite: 2].
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))
    
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i, 0])
        y.append(scaled_data[i, 0])
    
    return np.array(X).reshape(-1, window_size, 1), np.array(y), scaler