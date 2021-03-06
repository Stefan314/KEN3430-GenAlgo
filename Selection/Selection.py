from Selection.SelectionType import SelectionType


class Selection:
    """
    Super class for all other selection types. E.g., TSP and knapsack.
    """

    def __init__(self, sel_type: SelectionType):
        """
        Inheriting classes should tell the super class what kind of selection types they are.
        :param sel_type: A string.
        This makes it easier to see what kind of selection types is being handled.
        """
        self.sel_type = sel_type

    def select(self, pop):
        """
        Selects a list of individuals with the same length as pop, possibly based on their fitness.
        :param pop: The population where individuals can be picked from.
        :return: A list of selected individuals
        """
        pass
