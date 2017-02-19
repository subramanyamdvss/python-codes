# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""A very simple MNIST classifier.
See extensive documentation at
http://tensorflow.org/tutorials/mnist/beginners/index.md
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf



data_dir = '/tmp/tensorflow/mnist/input_data'

def model2():
  # Import data
  mnist = input_data.read_data_sets(data_dir, one_hot=True)

  # Create the model
  x1 = tf.placeholder(tf.float32, [None, 784])
  W1 = tf.Variable(tf.zeros([784, 10]))
  b1 = tf.Variable(tf.zeros([10]))
  y1 = tf.nn.softmax(tf.matmul(x1, W1) + b1)

  # Define loss and optimizer
  y_1 = tf.placeholder(tf.float32, [None, 10])

  # The raw formulation of cross-entropy,
  #
  #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
  #                                 reduction_indices=[1]))
  #
  # can be numerically unstable.
  #
  # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
  # outputs of 'y', and then average across the batch.
  l2 = tf.nn.l2_loss(y1 - y_1)
  train_step1 = tf.train.GradientDescentOptimizer(0.5).minimize(l2)





  sess1 = tf.InteractiveSession()
  tf.initialize_all_variables().run()
  # Train
 
  for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    batch_ys1 = sess.run(y, feed_dict={x: batch_xs2, y_: batch_ys2})
    sess1.run(train_step1, feed_dict={x1: batch_xs2, y_1: batch_ys1})
  
  # Test trained model
  correct_prediction1 = tf.equal(tf.argmax(y1, 1), tf.argmax(y_1, 1))
  accuracy1 = tf.reduce_mean(tf.cast(correct_prediction1, tf.float32))
  print(sess1.run(accuracy1, feed_dict={x1: mnist.test.images,
                                      y_1: mnist.test.labels}))
  return W1,b1

W2,b2=model2()




