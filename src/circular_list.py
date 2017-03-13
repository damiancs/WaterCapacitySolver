# coding=utf-8
"""
A circular list so we won't have to calculate the real index.
"""


class CircularList(list):
    """
    A circular list.
    """

    def __getattr__(self, idx):
        """
        Get a item by it's index.
        :param idx: The index to access.
         :type idx: int
        """
        return super(CircularList, self).__getattribute__(idx % len(self))

    def __setattr__(self, idx, value):
        """
        Set a item's value by it's index.
        :param idx: The index to access.
         :type idx: int
        :param value: The new value to set.
        """
        super(CircularList, self).__setattr__(idx % len(self), value)
