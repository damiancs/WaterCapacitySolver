# coding=utf-8
"""
The Bucket class that models a bucket from the game.
"""

from errors import BucketError


class Bucket(object):
    """
    A model of a bucket from the game.
    """

    def __init__(self, capacity=10.0, quantity=0.0):
        """
        Constructor for the bucket; setting the bucket capacity and the initial quantity of water.
        :param capacity: The maximum capacity of this bucket.
         :type capacity: float
        :param quantity: The initial quantity of liquid hold by the bucket.
         :type quantity: float
        """
        if quantity > capacity:
            raise BucketError("The capacity of this bucket does not allow you to hold this quantity of liquid.")
        self.capacity = capacity
        self.quantity = quantity
