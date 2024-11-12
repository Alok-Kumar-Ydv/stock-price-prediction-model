# Preprocess the 'Volume' column (remove 'M' and multiply by 1e6)
data['Volume'] = data['Volume'].str.replace('M', '').astype(float) * 1e6

# Preprocess the 'Change rate %' column (remove '%' and convert to float)
data['Change rate %'] = data['Change rate %'].str.replace('%', '').astype(float)

# Create lag features (previous 3 days closing price)
data['Prev_Close_1'] = data['closing price'].shift(1)
data['Prev_Close_2'] = data['closing price'].shift(2)
data['Prev_Close_3'] = data['closing price'].shift(3)
//code is changed
data['Prev_Close_1'] = data['closing price'].shift(4)
data['Prev_Close_2'] = data['closing price'].shift(5)
data['Prev_Close_3'] = data['closing price'].shift(6)

# Drop NaN values created by the shift operation
data.dropna(inplace=True)

# Prepare features and target variable
features = ['opening price', 'high price', 'low price', 'Volume', 'Change rate %', 'Prev_Close_1', 'Prev_Close_2', 'Prev_Close_3']
target = 'closing price'

X = data[features]
y = data[target]

# Split the data into training and test sets (80% training, 20% testing)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

print(X_train.shape, X_test.shape)
