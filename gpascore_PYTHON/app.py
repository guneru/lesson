import pandas as pd

data = pd.read_csv('gpascore.csv')

# print(data.isnull().sum())
data = data.dropna()

y데이터 = data['admit'].values

x데이터 = [ ]

for i, rows in data.iterrows():
    x데이터.append([ rows['gre'], rows['gpa'], rows['rank'] ])

import tensorflow as tf
model = tf.keras.models.sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'] )

model.fit( x데이터, y데이터, epochs=10 )