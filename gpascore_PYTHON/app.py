import pandas as pd

data = pd.read_csv('gpascore.csv')


import tensorflow as tf
model = tf.keras.models.sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'] )

# model.fit( x데이터, y데이터, epochs=10 )