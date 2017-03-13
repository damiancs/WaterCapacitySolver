# coding=utf-8
"""
Test this package.
"""
from __future__ import print_function
from unittest import TestCase
from src.solver import Solver


class TestSolver(TestCase):
    """
    Test case to check if the solver works.
    """

    @classmethod
    def setUpClass(cls):
        cls._solver = Solver(5, [(0.0, 10.0), (0.0, 9.0), (5.0, 7.0)], (1, 4.0))

    def test_result(self):
        """
        Test the solution.
        """
        print(self._solver._moves)