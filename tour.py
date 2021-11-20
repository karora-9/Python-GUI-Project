"""
functions to run TOAH tours.
"""


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'

import time
from toah_model import TOAHModel


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """

    def three_stool_solver(n, source, base_stool, destination):
        """ A helper function that is used to moving n number of cheeses
        from the origin stool to the destination stool.

        @type n: int
        @type source: int
        @type base_stool: int
        @type destination: int

        "Examples are not practical here."
        """
        if n > 1:
            three_stool_solver(n - 1, source, destination, base_stool)
            model.move(source, destination)
            three_stool_solver(n - 1, base_stool, source, destination)
        elif n == 1:
            model.move(source, destination)

    def four_stool_solver(n, source, stool1, stool2, destination):
        """ A helper function that is used to solve ordering n number of
        cheeses from the first stool to the fourth stool.

        n is a valid natural number greater than 0

        @type n: int
        @type source: int
        @type stool1: int
        @type stool2: int
        @type destination: int
        @rtype: None

        "Examples are not practical here."
        """
        if n == 1:
            model.move(source, destination)
        elif n == 2:
            model.move(source, stool1)
            model.move(source, destination)
            model.move(stool1, destination)
        elif n == 3:
            model.move(source, stool1)
            model.move(source, stool2)
            model.move(source, destination)
            model.move(stool2, destination)
            model.move(stool1, destination)
        elif n > 3:
            four_stool_solver(n - 3, source, stool2, destination, stool1)
            three_stool_solver(3, source, stool2, destination)
            four_stool_solver(n - 3, stool1, stool2, source, destination)

    four_stool_solver(model.get_number_of_cheeses(), 0, 1, 2, 3)

    if animate is True:
        for move in model.get_animated_moves():
            print(move)
            time.sleep(delay_btw_moves)


if __name__ == '__main__':
    NUM_CHEESES = 5
    DELAY_BETWEEN_MOVES = 0.5
    CONSOLE_ANIMATE = True

    # DO NOT MODIFY THE CODE BELOW.
    FOUR_STOOLS = TOAHModel(4)
    FOUR_STOOLS.fill_first_stool(number_of_cheeses=NUM_CHEESES)

    tour_of_four_stools(FOUR_STOOLS,
                        animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)
    print(FOUR_STOOLS.number_of_moves())
