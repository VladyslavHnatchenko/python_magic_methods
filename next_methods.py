from os.path import join


class FileObject:
    """ The wrapper for the file object to ensure that the file will be closed upon deletion."""

    def __init__(self, filepath='~', filename='sample.txt'):
        # Open file filename in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


class Word(str):
    """ The class for word s that defines a comparison by word length."""

    def __new__(cls, word):
        # We have to use __new__, since the type of str is immutable
        # and we need to initialize it earlier (when creating)
        if ' ' in word:
            print("Value contains spaces. Trancating to first space.")
            word = word[:word.index(' ')] # Now Word is all characters up to first space
            return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __setattr__(self, key, value):
        self.name = value
        """
        This's a recursion, because whenever any attribute is assigned a value, 
        __setattr__() is called. That is, in fact, is equivalent to
        self.__setattr__('name', value).
        Since the method calls itself, the recursion will continue indefinitely, 
        until everything falls
        """

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        """
        Assignment of class variables to the dictionary.
        Further definition of arbitrary behavior.
        """


class AccessCounter(object):
    """
    The class that contains the value attribute and implements an access counter for it.
    The counter is incremented every time the value changes.
    """

    def __int__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # We won't make any condition here.
        # If you want to prevent other attributes from being modified,
        # throw an AttributeError(name) exception.
        super(AccessCounter, self).__setattr__(name, value)
        
    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)


class FunctionalList:
    """
    Class wrapper over the list with some functional magic added:
    head, tail, last, drop, take.
    """

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if the value or key type is incorrect, the list throw an exception
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)

    def head(self):
        # return first element
        return self.values[0]

    def tail(self):
        # return all elements except 1st
        return self.values[1:]

    def init(self):
        # return all elements except the last
        return self.values[:-1]

    def last(self):
        # return the last element
        return self.values[-1]

    def drop(self, n):
        # all elements except n first elements
        return self.values[n:]

    def take(self, n):
        # first n elements
        return self.values[:n]
    