# For the model from part2 design custom exception classes and implement handling of possible exceptional situations.
# For example, there is no element that meets required criteria in the collection, impossible to delete an element etc.
# Leave your explanation in commented blocks of your exception class.
# Create at least 3 custom exceptions and use 5 built-in exceptions minimum
# (3 custom and 2 built-in this file, others are in part2_task1 file)

class AircraftError(TypeError):
    """ When adding object, that is not of Aircraft class """
    def __init__(self):
        self.message = 'The object is not an Aircraft'
        super().__init__(self.message)


class DistanceError(ValueError):
    """ When trying to sort objects without distance set """
    def __init__(self, aircraft):
        self.message = f'Distance for {aircraft} is not set'
        super().__init__(self.message)


class DurationError(ValueError):
    """ When trying to get duration that is negative """
    def __init__(self, flight):
        self.message = f'Duration for {flight} is negative'
        super().__init__(self.message)
