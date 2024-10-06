# Predict the stock price using the test data
predictions = model.predict(X_test_lstm)
predictions = scaler.inverse_transform(predictions)

# Calculate RMSE
rmse = np.sqrt(np.mean((predictions - scaler.inverse_transform(y_test_lstm.reshape(-1, 1)))**2))
print(f'Root Mean Squared Error: {rmse}')

# Plot actual vs. predicted prices
plt.figure(figsize=(10,6))
plt.plot(data['Date'][train_size:], scaler.inverse_transform(y_test_lstm.reshape(-1, 1)), label='Actual Price')
plt.plot(data['Date'][train_size:], predictions, label='Predicted Price')
plt.title('NTT Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
