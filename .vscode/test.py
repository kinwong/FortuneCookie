import tensorflow as tf
import logging

def test():
    data = {'a': 1, 'b': 2, 'c': 3}
    sess = tf.Session()
    a = tf.constant(4)
    b = tf.constant(5)
    return sess.run(a * b)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    data = {'a': 1, 'b': 2, 'c': 3}
    sess = tf.Session()
    a = tf.constant(4)
    b = tf.constant(5)
    c = sess.run(a * b)
    print(c)
