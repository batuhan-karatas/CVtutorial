import tensorflow as tf

eye_tensor = tf.eye(num_rows=5,num_columns=None,dtype=tf.dtypes.float32,name=None)
print(eye_tensor)

fill_tensor = tf.fill([3,4],5, name=None)
print(fill_tensor)

random_tensor = tf.random.normal([3,2],mean=4,stddev=2,dtype=tf.dtypes.float16)
print(random_tensor)