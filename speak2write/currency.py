#This code only for conversion of currency dollar.Any other currency can be updated.

class Dollar:
        def __init__(self, value):
            self.value = value
        def __add__(self, other):
            return Dollar(self.value + other.value)
        def __sub__(self, other):
            return Dollar(self.value - other.value)
        def __repr__(self):
            return 'Dollar({})'.format(self.value)
        def __str__(self):
            return '${:.2f}'.format(self.value)
        

class currency(object):
    """docstring for currency"""
    def __init__(self):
        pass

    def tocurrency(sentence):
        
        for i in sentence:
            if i.isdigit():
                return Dollar(i).__str__()
            else:
                pass

        