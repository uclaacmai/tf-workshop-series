from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
import tensorflow as tf
import numpy as np

# define placeholders for our training variables
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

def weight_variable(shape):
    """Initializes weights randomly from a normal distribution
    Params: shape: list of dimensionality of tensor
    """
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    """Initializes the bias term randomly from a normal distribution.
    Params: shape: list of dimensionality for the bias term.
    """
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# create weights and biases and function for our first layer
W_fc1, b_fc1 = weight_variable([784, 100]), bias_variable([100])
# hidden layer computes relu(Wx + b)
h_fc1 = tf.nn.relu(tf.matmul(x, W_fc1) + b_fc1)

keep_prob_1 = tf.placeholder(tf.float32)
# add dropout: discard activations with probability given by keep_prob
h_fc1_dropout = tf.nn.dropout(h_fc1, keep_prob_1)

# create w, b, and function for our next layer
W_fc2, b_fc2 = weight_variable([100, 30]), bias_variable([30])
h_fc2 = tf.nn.relu(tf.matmul(h_fc1_dropout, W_fc2) + b_fc2)

# add dropout
keep_prob_2 = tf.placeholder(tf.float32)
# discard second hidden layer activations with keep_prob_2 probability
h_fc2_dropout = tf.nn.dropout(h_fc2, keep_prob_2)
# define w and b for the softmax layer
W_fc3, b_fc3 = weight_variable([30, 10]), bias_variable([10])

# softmax Output
y_pred = tf.nn.softmax(tf.matmul(h_fc2_dropout, W_fc3) + b_fc3)
cross_entropy = -tf.reduce_sum(y_*tf.log(y_pred))
sae = -tf.reduce_sum(y_-y_pred)
#train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
#sae_train_step = tf.train.AdamOptimizer(1e-4).minimize(sae)
train_step = tf.train.MomentumOptimizer(1e-4, 0.5, name='Momentum', use_nesterov=True).minimize(cross_entropy)
# accuracy variables
cp = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y_, 1))
acc = tf.reduce_mean(tf.cast(cp, tf.float32))
init = tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        # iterate for 10k epochs and run batch SGD.
        batch = mnist.train.next_batch(100)
        print(type(batch[0]))
        exit()
        sess.run(train_step, feed_dict={x: batch[0], y_: batch[1], keep_prob_1: 0.8,
                                        keep_prob_2: 0.5})
        if i % 100 == 0:
            print("epoch: {}".format(i + 1))
            print(acc.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob_1: 1.0,
                                      keep_prob_2: 1.0}))
    print("done training!")
    test_acc = acc.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob_1: 1.0,
                                   keep_prob_2: 1.0})
    print("test acc: {}".format(test_acc))

sess.close()
