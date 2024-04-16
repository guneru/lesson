import tensorflow as tf

텐서 = tf.constant( [3,4,5] )
텐서2 = tf.constant( [6,7,8] )

텐서3 = tf.constant( [ [1,2],
                    [3,4] ] )

print(텐서 / 텐서2)