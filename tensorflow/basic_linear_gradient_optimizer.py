import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*52.327  - 31.813

slope = tf.Variable(tf.random_uniform([1],-100.0,100.0))
intercept = tf.Variable(tf.zeros([1]))

y = x_data*slope + intercept

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()


sess = tf.Session()
sess.run(init)


for i in range(201):
    sess.run(train)
    print(i,sess.run(loss),sess.run(slope),sess.run(intercept))