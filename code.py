import tensorflow as tf
import numpy as np

def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)

def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)

def nlp_layer(one_hot_vec,x):
	W=weight_variable([x,5746])
	b=bias_variable([x,1])
	y=tf.nn.relu(matmul(W,one_hot_vec)+b)
