\*\*NTT Stock Price Prediction Model\*\*

\====================================

\*\*Project Overview\*\*

\--------------------

This project involves building a time-series stock price prediction model using NTT stock data. We use Exploratory Data Analysis (EDA) to understand the data, preprocess the data for machine learning, and build a predictive model using \*\*Long Short-Term Memory (LSTM)\*\*, a type of recurrent neural network suited for time-series prediction.

\*\*Requirements\*\*

\----------------

- Python 3.7+
- Libraries:
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `keras`
- `tensorflow`

You can install the required libraries using the following command:

bash

Copy code

`pip install -r requirements.txt`

\*\*Dataset\*\*

\-----------

The dataset used contains stock price data of NTT with the following columns:

- `Date`: Date of the stock price.
- `closing price`: Closing price of the stock on the given date.
- `opening price`: Opening price of the stock on the given date.
- `high price`: Highest price of the stock on the given date.
- `low price`: Lowest price of the stock on the given date.
- `volume`: Trading volume in millions (M).
- `change rate %`: Daily percentage change in the stock price.

The data file should be in CSV format (`data.csv`).

\*\*Exploratory Data Analysis (EDA)\*\*

\-----------------------------------

1. \*\*Data Understanding\*\*: We load and inspect the dataset to get an overview of the stock price trends.
1. \*\*Visualizations\*\*:
- Plotting stock price trends (Closing price).
- Visualizing trading volume.
- Examining moving averages (20-day and 50-day).
- Correlation matrix to understand the relationships between price metrics.

\*\*Data Preprocessing\*\*

\----------------------

The following preprocessing steps were performed:

1. Handling missing values.
1. Converting columns like `Volume` and `Change rate %` into numerical format.
1. Generating lag features (e.g., previous 3 days' closing prices).
1. Scaling the data using \*\*MinMaxScaler\*\* for LSTM model input.

\*\*Modeling: LSTM for Stock Price Prediction\*\*

\---------------------------------------------

\### \*\*Model Selection\*\*

We chose the \*\*LSTM (Long Short-Term Memory)\*\* model for time-series prediction because of its ability to capture long-term dependencies in sequential data. The model consists of two LSTM layers followed by dense layers to predict the stock price.

\### \*\*Model Architecture\*\*

- \*\*Input\*\*: Sequences of 60 time steps (days).
- \*\*LSTM Layers\*\*: Two stacked LSTM layers to capture sequential dependencies.
- \*\*Dense Layers\*\*: A fully connected layer to output the predicted closing price.

\### \*\*Training\*\*

- Optimizer: Adam
- Loss Function: Mean Squared Error (MSE)
- Epochs: 10
- Batch Size: 64

\*\*Evaluation\*\*

\--------------

The model is evaluated using \*\*Root Mean Squared Error (RMSE)\*\*. Additionally, we visualize the predicted vs. actual stock prices to compare model performance.

\*\*Usage Instructions\*\*

\----------------------

1. \*\*Clone the Repository\*\*

Clone the repository to your local machine:

bash

Copy code

`git clone https://github.com/Alok-Kumar-Ydv/stock-price-prediction-model

cd stock-price-prediction`

1. \*\*Prepare the Dataset\*\*

- Place your dataset in the root directory of the project and name it `data.csv`.

3\.  \*\*Run the Code\*\*

You can run the project using a Jupyter Notebook or Python script.

- \*\*Using Jupyter Notebook\*\*: Open the notebook file, run each cell sequentially.

- \*\*Using Python script\*\*: Run the main Python script:

bash

Copy code

`python main.py`

4\.  \*\*Model Output\*\*

The model will output predictions and generate plots comparing actual and predicted stock prices, as well as evaluation metrics like RMSE.

\*\*Project Structure\*\*

\---------------------

- `data.csv`: Stock price dataset.
- `main.py`: Python script for the entire process (EDA, preprocessing, LSTM model training, evaluation).
- `README.md`: Instructions and project overview.
- `requirements.txt`: Python package dependencies.

\*\*Results and Analysis\*\*

\------------------------

- \*\*Root Mean Squared Error (RMSE)\*\*: The model's RMSE score on the test dataset.
- \*\*Prediction vs Actual Plot\*\*: A graph that shows how well the model's predictions match the actual stock prices.
- \*\*Moving Averages\*\*: Insights into short-term and long-term trends in the stock price.

\*\*Future Work and Improvements\*\*

\--------------------------------

- \*\*Hyperparameter Tuning\*\*: Further optimization of LSTM parameters such as epochs, batch size, and time steps.
- \*\*Feature Engineering\*\*: Adding more technical indicators or external factors (e.g., macroeconomic indicators) to improve model accuracy.
- \*\*Model Architecture\*\*: Experimenting with different neural network architectures like GRU, CNN, or Transformer models.
