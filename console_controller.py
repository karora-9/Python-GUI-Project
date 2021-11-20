"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""

from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    try:
        model.move(origin, dest)
    except IllegalMoveError:
        print("You have entered an illegal move.")


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.tm = TOAHModel(number_of_stools)
        self.tm.fill_first_stool(number_of_cheeses)
        self.number_of_stools = number_of_stools
        self.number_of_cheeses = number_of_cheeses

    def choose_valid_stool(self, stool_type):
        """ Prompts the user to enter a valid stool selection.
        according to what stool the user is looking at.
        If the input is valid, then the stool index will be
        returned.

        @type self: ConsoleController
        @type stool_type: str
        @rtype: int
        """
        while True:
            try:
                stool_selection = int(input('Type in a valid ' + stool_type +
                                            ' stool: \n'))
            except ValueError:
                print('That is not a valid ' + stool_type + ' stool!')
                continue
            else:
                if stool_selection > self.number_of_stools \
                        or stool_selection < 1:
                    print('Stool index out of range!')
                else:
                    return stool_selection - 1

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        playing = True
        print(self.tm)
        while playing:
            origin_stool = self.choose_valid_stool('origin')
            destination_stool = self.choose_valid_stool('destination')
            move(self.tm, origin_stool, destination_stool)
            print(self.tm)
            if len(self.tm.get_stool_list()[-1]) == self.number_of_cheeses:
                print('\nYou have won the game!')
                print('Your total move count is: ' +
                      str(self.tm.get_move_seq().length()))
                print('The game will now exit.')
                playing = False
            else:
                keep_playing = input("\nPress enter to "
                                     "continue or type e to exit: \n")
                if keep_playing == 'e':
                    print("The game will now exit.")
                    playing = False


def prompt_number(item):
    """ Prompts the user to input a valid integer
    greater than 0 to be used for the inputed item.

    @type item: str
    @rtype: int
    """
    while True:
        try:
            num_selection = int(input("Enter a valid number of "
                                      + item + ':\n'))
        except ValueError:
            print("You have inputed an invalid number!")
            continue
        else:
            if num_selection > 0:
                return num_selection
            else:
                print('You have inputed an invalid number!')


if __name__ == '__main__':
    INSTRUCTIONS0 = "The goal of this game is to move the entire stack of "\
                    "cheese rounds from the first stool to the last stool."
    INSTRUCTIONS1 = "Each move consists of choosing an origin stool and then"\
                    " a destination stool.\nThe very top cheese of the origin"\
                    " stool is moved on top of the destination stool."
    INSTRUCTIONS2 = "The id of the stools are in the order of how they are "\
                    "displayed, with 1 being the first stool."
    INSTRUCTIONS3 = "A move is only valid if you pick from a non empty stool"\
                    " or if you choose an origin stool with a smaller " \
                    "cheese block."\
                    " than its destination stool."
    INSTRUCTIONS4 = "Each stool choice must be a valid natural number between "\
                    "1 and the total number of stools in the game."
    INSTRUCTIONS5 = "At the end of each move, you will be given the option to "\
                    "exit the game by simply typing e."
    INSTRUCTIONS6 = "Good luck and have fun!"
    print("Hello, welcome to the Tower of Anne Horton!"
          "\nPlease select one of the following numbers below.")
    MENU = None
    while True:
        try:
            MENU = int(input("\nChoose one of the following numbers "
                             "below:\n1: Instructions \n2: Begin game \n3: "
                             "Exit \n"))
        except ValueError:
            print("Invalid Menu selection.")
        else:
            if MENU in range(1, 4):
                break
            else:
                print("Invalid Menu selection.")

    if MENU == 1:
        print("Press enter to skip through the instructions.")
        NEXT = input('')
        print(INSTRUCTIONS0)
        NEXT = input('')
        print(INSTRUCTIONS1)
        NEXT = input('')
        print(INSTRUCTIONS2)
        NEXT = input('')
        print(INSTRUCTIONS3)
        NEXT = input('')
        print(INSTRUCTIONS4)
        NEXT = input('')
        print(INSTRUCTIONS5)
        NEXT = input('')
        print(INSTRUCTIONS6)
        NEXT = input('')
        MENU = 2
    if MENU == 2:
        STOOLS = prompt_number('stools')
        while STOOLS == 1:
            print("\nYou cannot play with one stool!")
            STOOLS = prompt_number('stools')
        CHEESES = prompt_number('cheeses')
        CC = ConsoleController(CHEESES, STOOLS)
        CC.play_loop()
    elif MENU == 3:
        print('\nThe game will now exit.')

    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
