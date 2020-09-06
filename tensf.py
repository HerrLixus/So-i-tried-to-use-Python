import tensorflow as tf
import numpy as np

a = tf.constant(np.array([[1, 0, 0, 1],
                          [0, 1, 1, 0],
                          [1, 0, 1, 0],
                          [0, 1, 0, 1]], dtype=float))

b = tf.constant(np.array([[0, 1, 0, 1]], dtype=float).T)

c = tf.constant(np.array([[1, 1, 1, 1],
                          [0, 0, 0, 0],
                          [1, 1, 0, 0],
                          [1, 1, 1, 1]]))

d = tf.constant(np.array([[1, 0, 1, 1]]).T)

