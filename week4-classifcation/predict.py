from draw import Paint
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

drawing = Paint()
im_arr = drawing.get_digit()


plt.axis('off')
plt.imshow(im_arr, cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()


im_vec = im_arr.reshape(1, -1)

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Construct model
pred = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

sess = tf.Session()
new_saver = tf.train.import_meta_graph('./model.ckpt')
new_saver.restore(sess, tf.train.latest_checkpoint('./'))

# saver = tf.train.Saver()

# sess = tf.Session()
# saver.restore(sess, "./model.ckpt")

prediction = tf.argmax(pred,1)
print (prediction.eval(feed_dict={x: im_vec}, session=sess))

classification = sess.run(pred, {x: im_vec})
print (classification)
