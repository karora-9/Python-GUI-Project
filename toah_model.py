"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. 
"""

class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        self._stools = []
        for i in range(0, number_of_stools):
            self._stools.append(Stool(i))
        self._number_of_stools = number_of_stools
        self._move_seq = MoveSequence([])
        self._number_of_cheeses = 0
        self._animated_moves = []

    def get_stool_at(self, index):
        """ Returns the stool at the given index inside of TOAHModel's
        list of stools.

        @type self: TOAHModel
        @type index: int
        @rtype: Stool object

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.get_stool_at(0).get_stool_id()
        0
        """
        return self._stools[index]

    def get_stool_list(self):
        """ Returns the list of stools in TOAHModel.

        @type self: TOAHModel
        @rtype: list[Stool objects]

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> len(M.get_stool_list())
        4
        """
        return self._stools

    def fill_first_stool(self, number_of_cheeses):
        """ Fills the first stool with the given number of cheese.
        with the largest cheese size diamater being the given number
        of cheeses and the smallest being 1.

        @type self: TOAHModel
        @type number_of_cheeses: int
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> len(M.get_stool_at(0))
        5
        """
        self._number_of_cheeses = number_of_cheeses
        for size in range(1, number_of_cheeses + 1):
            self.add(Cheese(number_of_cheeses + 1 - size), 0)

    def get_number_of_stools(self):
        """ Return the number of stools in the instance of TOAHModel.

        @type self: TOAHModel
        @rtype: int

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(4)
        >>> M.get_number_of_stools()
        4
        """
        return self._number_of_stools

    def get_number_of_cheeses(self):
        """ Returns the total number of cheeses in TOAHModel.

        @type self: TOAHModel
        @rtype: int

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(4)
        >>> M.get_number_of_cheeses()
        4
        """
        return self._number_of_cheeses

    def number_of_moves(self):
        """ Returns the total number of moves the user has
        made so far.

        @type self: TOAHModel
        @rtype: int

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(4)
        >>> M.move(0, 1)
        >>> M.move(0, 2)
        >>> M.number_of_moves()
        2
        """
        return self._move_seq.length()

    def get_move_seq(self):
        """ Return the move sequences made so far in TOAHModel.

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> isinstance(toah.get_move_seq(), MoveSequence)
        True
        """
        return self._move_seq

    def get_cheese_location(self, cheese):
        """ Looks for for the given cheese throughout the stools
        and returns the stool index that the cheese is on top of.

        Return None if no stool is holding the specified cheese.

        @type self: TOAHModel
        @type cheese: Cheese
        @rtype: int | None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> a_cheese = Cheese(4)
        >>> M.get_cheese_location(a_cheese)
        0
        """
        for stool in self._stools:
            if stool.is_empty() is False:
                if stool.locate_cheese(cheese) is not None:
                    return stool.locate_cheese(cheese)
        return None

    def get_top_cheese(self, stool_index):
        """ Returns the cheese at the top of the given stool.

        @type self: TOAHModel
        @type stool_index: int
        @rtype: Cheese object

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.get_top_cheese(0).size
        1
        """
        return self._stools[stool_index].get_top_cheese()

    def get_animated_moves(self):
        """ Returns the list of moves made so far where each move
        is an animation leading to the next move.

        @type self: TOAHModel
        @type: list[str]

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0, 1)
        >>> M.move(0, 2)
        >>> len(M.get_animated_moves())
        2
        """
        return self._animated_moves

    def add(self, cheese, stool_number):
        """ Stacks the given cheese on top of the desired stool.

        @type self: TOAHModel
        @type cheese: Cheese object
        @type stool_number: int
        @rtype: None

        >>> M = TOAHModel(4)
        >>> a_cheese = Cheese(3)
        >>> M.add(a_cheese, 0)
        >>> M.get_top_cheese(0).size
        3
        """
        selected_stool = None
        for stool in self._stools:
            if stool.get_stool_id() == stool_number:
                selected_stool = stool
        if selected_stool.is_empty() is True:
            selected_stool.add_cheese_to_end(cheese)
        elif selected_stool.get_top_cheese().size > cheese.size:
            selected_stool.add_cheese_to_end(cheese)

    def move(self, source_stool, destination_stool):
        """ Moves the top cheese from the source stool to the
        top of destination stool if the move is a valid move.

        @type self: TOAHModel
        @type source_stool: int
        @type destination_stool: int
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0, 1)
        >>> M.move(0, 2)
        >>> M.get_top_cheese(1).size
        1
        >>> M.get_top_cheese(2).size
        2
        """
        if self._stools[source_stool].get_top_cheese() is None:
            print("\nSelected stool has no cheese!")
            raise IllegalMoveError
        elif self._stools[destination_stool].is_empty() is True:
            selected_cheese = self._stools[source_stool].remove_top_cheese()
            self._stools[destination_stool].add_cheese_to_end(selected_cheese)
            self._move_seq.add_move(source_stool, destination_stool)
            self._animated_moves += [str(self)]
        elif self._stools[destination_stool].get_top_cheese().size \
                > self._stools[source_stool].get_top_cheese().size:
            selected_cheese = self._stools[source_stool].remove_top_cheese()
            self._stools[destination_stool].add_cheese_to_end(selected_cheese)
            self._move_seq.add_move(source_stool, destination_stool)
            self._animated_moves += [str(self)]
        else:
            print("\nCant move the cheese there!")
            raise IllegalMoveError

    def _cheese_at(self, stool_index, stool_height):
        """ Return (stool_height)th from stool_index stool, if possible.

        @type self: TOAHModel
        @type stool_index: int
        @type stool_height: int
        @rtype: Cheese | None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        if 0 <= stool_height < len(self._stools[stool_index]):
            return self._stools[stool_index][stool_height]
        else:
            return None

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        result = True
        if not isinstance(other, TOAHModel):
            return False
        if not self.get_number_of_stools() == other.get_number_of_stools():
            return False
        if not self.get_number_of_cheeses() == other.get_number_of_cheeses():
            return False
        stool_list = self.get_stool_list()
        other_s_list = other.get_stool_list()
        for i in range(len(stool_list)):
            cheese_stack = stool_list[i].get_cheese_stack()
            for cheese in cheese_stack:
                if stool_list[i].locate_cheese(cheese) != \
                        other_s_list[i].locate_cheese(cheese):
                    result = False
        return result

    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str
        return lines


class Stool:
    """ A stool for stacking cheese rounds on top of
    in TOAHModel.

    === Private Attributes ===
    @param int _id:
        The unique identifier of this stool. Each stool
        is identified dby their position in TOAHModel.
    @param list[objects] _cheese_stack:
        A list containing a stack of cheese, ordered
        from the biggest size cheese to the smallest.
    """

    def __init__(self, _id):
        """ Initializes a stool with the given _id.

        @type self: Stool
        @type _id: int | None
        @rtype: None

        >>> s = Stool(0)
        >>> s.is_empty()
        True
        """
        self._id = _id
        self._cheese_stack = []

    def get_cheese_stack(self):
        """ Returns the cheese stack on this stool.

        @type self: Stool
        @rtype: list

        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.get_cheese_stack()[0].size
        1
        """
        return self._cheese_stack

    def is_empty(self):
        """ Returns whether or the the stool is an empty stool.

        @type self: Stool
        @rtype: Boolean

        >>> s = Stool(0)
        >>> s.is_empty()
        True
        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.is_empty()
        False
        """
        return len(self._cheese_stack) == 0

    def get_stool_id(self):
        """ Returns this stools unique number id.

        @type self: Stool
        @rtype: int

        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.get_stool_id()
        0
        """
        return self._id

    def get_top_cheese(self):
        """ Returns the top cheese on the stool.

        @type self: Stool
        @rtype: None | Cheese object

        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.get_top_cheese().size
        1
        >>> s1 = Stool(0)
        >>> s1.get_top_cheese()
        """
        if self.is_empty() is True:
            return None
        else:
            return self._cheese_stack[-1]

    def remove_top_cheese(self):
        """ Removes the top cheese on the stool and
        returns it.

        Returns None if there the stool is empty.

        @type self: Stool
        @rtype: Cheese object | None

        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.remove_top_cheese().size
        1
        """
        if len(self._cheese_stack) != 0:
            return self._cheese_stack.pop()
        return None

    def add_cheese_to_end(self, cheese):
        """ Stacks the cheese on the very top of the stool if
        it is smaller than the cheese before it.

        @type self: Stool
        @type cheese: Cheese
        @rtype: None

        >>> s = Stool(0)
        >>> a_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.get_top_cheese().size
        1
        """
        if self.is_empty() is True:
            self._cheese_stack.append(cheese)
        elif self._cheese_stack[-1].size > cheese.size:
            self._cheese_stack.append(cheese)

    def locate_cheese(self, specified_cheese):
        """ Searches through the stool's cheese_stack and tries
        to locate the specified cheese. If the cheese is present
        within stool, return the stool's id.

        Return None if no such cheese is present.

        @type self: Stool
        @type specified_cheese: Cheese
        @rtype: None | int

        >>> s = Stool(0)
        >>> a_cheese = Cheese(2)
        >>> b_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.add_cheese_to_end(b_cheese)
        >>> s.locate_cheese(a_cheese)
        0
        """
        for cheese in self._cheese_stack:
            if cheese.size == specified_cheese.size:
                return self._id
        return None

    def __len__(self):
        """ Returns the number of cheeses stacked on
        top of this stool.

        @type self: Stool
        @rtype: int

        >>> s = Stool(0)
        >>> a_cheese = Cheese(2)
        >>> b_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.add_cheese_to_end(b_cheese)
        >>> len(s)
        2
        """
        return len(self._cheese_stack)

    def __getitem__(self, cheese_location):
        """ Returns the cheese location on this Stool

        @type self: Stool
        @type cheese_location: int
        @rtype: int

        >>> s = Stool(0)
        >>> a_cheese = Cheese(2)
        >>> b_cheese = Cheese(1)
        >>> s.add_cheese_to_end(a_cheese)
        >>> s.add_cheese_to_end(b_cheese)
        >>> s[1] == b_cheese
        True
        """
        return self._cheese_stack[cheese_location]

    def __eq__(self, other):
        """ returns True iff self is equivilent to other.

        @param Stool self: this Stool
        @param Stool other: other Stool
        @rtype: bool

        >>> s1 = Stool(1)
        >>> s2 = Stool(1)
        >>> s1 == s2
        True
        >>> s2.add_cheese_to_end(Cheese(5))
        >>> s1 == s2
        False
        """
        return isinstance(other, Stool) and (self.get_stool_id() ==
                                             other.get_stool_id() and
                                             self.get_cheese_stack() ==
                                             other.get_cheese_stack())


class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool

        >>> c = Cheese(3)
        >>> c2 = Cheese(3)
        >>> c == c2
        True
        """
        return self.size == other.size

    def __str__(self):
        """ returns a str represention of the cheese self.

        @param Cheese self: this cheese object
        @rtype: str

        >>> c = Cheese(3)
        >>> print(c)
        This Cheese has size 3
        """
        return 'This Cheese has size {}'.format(self.size)


class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass


class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        >>> ms.length()
        1
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.add_move(2, 3)
        >>> ms.length()
        2
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
 
