# coding=utf-8
"""
Solver class. This module has the actual logic for solving the Water Capacity game.
"""


class Solver(object):
    """
    The solver class. This class holds the logic for solving the Water Capacity game.
    """

    def __init__(self, steps, buckets, solution, flags=None):
        """
        Constructor for the solver; initializes the game, solves it and stores the result.
        :param steps:
         :type steps: int
        :param buckets:
         :type buckets: list[tuple[float, float]]
        :param solution:
         :type solution: tuple[int, float]
        :param flags:
         :type flags: int
        """
        self._max_steps = steps
        self._bucket_list = buckets
        self._buckets = len(buckets)
        self._solution_bucket = solution[0]
        self._solution_quantity = solution[1]
        self._flags = flags
        self._result = list()
        self._result.append([bucket[0] for bucket in buckets])
        self._moves = self._create_moves()
        self._solve()

    def _create_moves(self):
        """
        Create the steps available for solving the game.
        :return: A list of actions to take on each step.
         :rtype: list[str]
        """
        actions = list()
        # creating halves, fills and empties
        for i in range(self._buckets):
            # actions.append("self._half({})".format(i))
            actions.append("self._fill({})".format(i))
            actions.append("self._empty({})".format(i))
            for j in range(1, self._buckets):
                actions.append("self._add({}, {})".format(i, i + j))
        return actions

    def _is_full(self, idx):
        """
        Check if a bucket passed by it's index is already full so we won't count an extra move for nothing.
        :param idx: The index of the bucket to check.
         :type idx: int
        :return: A boolean value showing if the bucket is full.
         :rtype: bool
        """
        return self._result[-1][idx] == self._bucket_list[idx][1]

    def _is_empty(self, idx):
        """
        Check if a bucket passed by it's index is already empty so we won't count an extra move for nothing.
        :param idx: The index of the bucket to check.
         :type idx: int
        :return: A boolean value showing if the bucket is empty.
         :rtype: bool
        """
        return self._result[-1][idx] == 0.0

    def _half(self, idx):
        """
        Halving the quantity of liquid in a bucket passed by it's index.
        :param idx: The index of the bucket in the bucket list.
         :type idx: int
        :return: A boolean value showing if the move is validated.
         :rtype: bool
        """
        if not self._can_move() or self._is_empty(idx):
            return False
        temp = [quantity for quantity in self._result[-1]]
        temp[idx] /= 2
        self._result.append(temp)
        return True

    def _fill(self, idx):
        """
        Fulfilling the quantity of liquid in a bucket passed by it's index.
        :param idx: The index of the bucket in the bucket list.
         :type idx: int
        :return: A boolean value showing if the move is validated.
         :rtype: bool
        """
        if not self._can_move() or self._is_full(idx):
            return False
        temp = [quantity for quantity in self._result[-1]]
        temp[idx] = self._bucket_list[idx][1]
        self._result.append(temp)
        return True

    def _empty(self, idx):
        """
        Emptying the bucket passed by it's index.
        :param idx: The index of the bucket in the bucket list.
         :type idx: int
        :return: A boolean value showing if the move is validated.
         :rtype: bool
        """
        if not self._can_move() or self._is_empty(idx):
            return False
        temp = [quantity for quantity in self._result[-1]]
        temp[idx] = 0
        self._result.append(temp)
        return True

    def _add(self, idx, span):
        """
        Add into the bucket passed by the index the liquid from the bucked at span distance from the first bucket.
        :param idx: The index of the destination bucket.
         :type idx: int
        :param span: The distance from the destination bucket to the source bucket.
         :type span: int
        :return: A boolean value showing if the move is validated.
         :rtype: bool
        """
        if not self._can_move():
            return False
        temp = [quantity for quantity in self._result[-1]]
        total = temp[idx] + temp[(idx + span) % self._buckets]
        if total <= self._bucket_list[idx][1]:
            temp[idx] = total
            temp[(idx + span) % self._buckets] = 0
        else:
            temp[idx] = self._bucket_list[idx][1]
            temp[(idx + span) % self._buckets] = total - self._bucket_list[idx][1]
        self._result.append(temp)
        return True

    def _undo(self):
        """
        Undo the last move.
        """
        self._result.pop()

    def _is_solved(self):
        """
        Checks if we have reached a solution.
        :return: Boolean value that tells if we have found a solution.
         :rtype: bool
        """
        return self._result[-1][self._solution_bucket] == self._solution_quantity

    def _can_move(self):
        """
        Checks if the current number of steps has not reach the maximum number.
        :return: A boolean value that tells if we have more steps available.
         :rtype: bool
        """
        return len(self._result) <= self._max_steps

    def _solve(self):
        """
        Solve the game.
        """
        pass
