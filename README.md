\# 📈 Nifty 50 Stock Price Prediction (25-Year Analysis)



\## 📌 Project Objective

The objective of this project is to build and evaluate predictive models for Nifty 50 stock prices using a 25-year historical dataset (2000–2024). 



To ensure robustness, models are evaluated across \*\*four distinct market regimes\*\*:

\- Pre-2019 (Stable Market)

\- COVID Era (High Volatility)

\- Post-COVID Recovery

\- Modern Market (Recent Trends)



\---



\## 🧠 Models Implemented

\- Linear Regression

\- XGBoost

\- ARIMA

\- LSTM (Deep Learning)



\---



\## ⚙️ Installation \& Setup



\### 1. Prerequisites

This project is developed using \*\*Python 3.11\*\*\[cite: 2].



\### 2. Install Dependencies

Run the following command to install the necessary libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost statsmodels tensorflow
```


## 📊 Results \& Analysis



\### 🔹 Experimental Setup

Models were evaluated across four different market regimes to test robustness:

\- \*\*Split 1:\*\* 2000–2018 (Stable Market)

\- \*\*Split 2:\*\* COVID Era (High Volatility)

\- \*\*Split 3:\*\* Recovery Phase

\- \*\*Split 4:\*\* Modern Market



\---



\### 🔹 Split-wise Performance



\#### 📌 Split 1: 2000–2018

| Model | MAE | RMSE | MAPE | R² | DA |

|------|------|------|------|------|------|

| Linear Regression | 51.55 | 67.52 | 0.55 | 0.996 | 57.57 |

| XGBoost | 936.71 | 1264.27 | 8.95 | -0.11 | 14.59 |

| ARIMA | 75.02 | 93.56 | 1.02 | 0.82 | 44.90 |

| LSTM | 4161.43 | 4245.41 | 44.59 | -14.65 | 50.88 |



\---



\#### 📌 Split 2: COVID Era

| Model | MAE | RMSE | MAPE |

|------|------|------|------|

| Linear Regression | 93.68 | 144.06 | 0.87 |

| XGBoost | 352.19 | 581.36 | 3.52 |

| ARIMA | 57.57 | 74.11 | 0.57 |

| LSTM | 4372.93 | 4445.19 | 43.72 |



\---



\#### 📌 Split 3: Recovery Phase

| Model | MAE | RMSE |

|------|------|------|

| Linear Regression | 113.07 | 149.71 |

| XGBoost | 3115.31 | 3353.53 |

| ARIMA | 151.62 | 202.71 |

| LSTM | 7853.07 | 8041.22 |



\---



\#### 📌 Split 4: Modern Market

| Model | MAE | RMSE | MAPE | R² | DA |

|------|------|------|------|------|------|

| Linear Regression | 109.66 | 154.89 | 0.51 | 0.996 | 57.49 |

| XGBoost | 2947.11 | 3794.39 | 12.73 | -1.15 | 8.91 |

| ARIMA | 108.06 | 134.99 | 0.60 | 0.75 | 61.22 |

| LSTM | 11921.01 | 12155.78 | 56.79 | -25.40 | 56.45 |



\---



\### 📊 Overall Model Performance (Averages)



| Model | MAE ↓ | RMSE ↓ | MAPE ↓ | R² ↑ | DA ↑ |

|------|------|------|------|------|------|

| \*\*Linear Regression\*\* | \*\*91.99\*\* | 129.05 | 0.65 | \*\*0.99\*\* | 59.03 |

| ARIMA | 98.07 | \*\*126.34\*\* | 0.79 | 0.76 | \*\*59.69\*\* |

| XGBoost | 1837.83 | 2248.39 | 10.72 | -1.71 | 11.57 |

| LSTM | 7077.11 | 7221.90 | 47.00 | -27.61 | 54.21 |



\---



\### 🧠 Key Insights



\- \*\*Linear Regression\*\*

&#x20; - Most stable and consistent across all splits

&#x20; - Best overall error metrics (MAE, R²)



\- \*\*ARIMA\*\*

&#x20; - Best at capturing \*\*trend direction\*\* (highest DA)

&#x20; - Strong performance in volatile conditions



\- \*\*XGBoost\*\*

&#x20; - Poor generalization across time splits

&#x20; - Likely needs better feature engineering



\- \*\*LSTM\*\*

&#x20; - Extremely high error and instability

&#x20; - Indicates poor tuning or insufficient data scaling



\---



\### 🏆 Final Conclusion



\- ✅ \*\*Best Overall Model:\*\* Linear Regression  

\- 📈 \*\*Best for Direction Prediction:\*\* ARIMA  

\- ⚖️ \*\*Most Robust Model:\*\* Linear Regression  



👉 \*\*Final Recommendation:\*\* Use \*\*Linear Regression\*\* for deployment due to its consistency and low error across all market conditions.

