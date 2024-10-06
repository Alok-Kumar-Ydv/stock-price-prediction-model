# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_file_path.csv' with actual path)
data = pd.read_csv('stock_price.csv')

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Check the first few rows of the data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Check basic statistics
print(data.describe())

# Plot the stock prices over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['closing price'], label='Closing Price')
plt.title('NTT Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Plot volume over time
plt.figure(figsize=(10, 6))
plt.bar(data['Date'], data['Volume'].str.replace('M', '').astype(float) * 1e6, color='orange')
plt.title('NTT Stock Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True)
plt.show()

# Calculate and plot moving averages
data['20_MA'] = data['closing price'].rolling(window=20).mean()
data['50_MA'] = data['closing price'].rolling(window=50).mean()

plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['closing price'], label='Closing Price')
plt.plot(data['Date'], data['20_MA'], label='20-Day MA')
plt.plot(data['Date'], data['50_MA'], label='50-Day MA')
plt.title('NTT Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# Correlation matrix between prices and volume
corr = data[['opening price', 'closing price', 'high price', 'low price']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
