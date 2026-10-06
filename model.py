import tensorflow as tf

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))  # 1 neuron, input shape of 1 dimension
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Prepare the data
X = [[1], [2], [3], [4], [5]]  # Features
y = [[2], [4], [6], [8], [10]]  # Labels

# Train the model
model.fit(X, y, epochs=500)

# Make predictions
predictions = model.predict(X)

# Print the predictions
print(predictions)
