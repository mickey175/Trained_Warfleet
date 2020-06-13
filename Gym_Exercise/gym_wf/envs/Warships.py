class Warships:

    """
    This class creates a single ship based on random values.
    The generates Objects contain all information about the ship.
    """
    small_ship = "X"
    middle_ship = "X"
    big_ship = "X"
    cruiser_ship = "X"

    def __init__(self, pos_bow, pos_stern, orientation, row_or_col, size):

        self.pos_bow = pos_bow
        self.pos_stern = pos_stern
        self.orientation = orientation
        self.row_or_col = row_or_col
        self.size = size

    @classmethod
    def check_size(cls, size):
        """
        Defines the symbol inside the console for the ship based on the ship size.
        """
        if size == 2:
            return Warships.small_ship
        if size == 3:
            return Warships.middle_ship
        if size == 4:
            return Warships.big_ship
        if size == 5:
            return Warships.cruiser_ship


