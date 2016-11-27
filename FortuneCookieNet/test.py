
import logging

import tensorflow as tf


def test():
    """
    what do you want.
    """
    sess = tf.Session()
    first = tf.constant(4)
    second = tf.constant(5)
    return sess.run(first * second)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(test())
