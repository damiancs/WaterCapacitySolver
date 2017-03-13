# coding=utf-8
"""
The exceptions that should be raised if errors happen in the process of solving the game.
"""


class SolverError(StandardError):
    """
    The error raised if something bad happens in Solver class.
    """
    pass


class BucketError(StandardError):
    """
    The error raised if something bad happens in Bucket class.
    """
    pass
