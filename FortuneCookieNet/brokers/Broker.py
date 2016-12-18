from abc import ABCMeta, abstractmethod


class Broker(object):
    """ Represents a broker. """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_orders(self):
        """ ffewff """
        pass


