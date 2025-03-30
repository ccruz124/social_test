"""a simple social network for tracking connections between people.""

class Person:
    """ A person in the social network.
    
    Attributes:
        name (str): the person's name.
        connections (set of Person): other people in the social network who know this person.
    """
    def connect(self, person2):
        """
        Args:
            person2 (Person): the other person to connect to.
