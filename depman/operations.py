from syn.base import ListWrapper, Attr

#-------------------------------------------------------------------------------
# Utilities

def subclass_equivalent(o1, o2):
    def comp(x, y):
        return issubclass(x, y) or issubclass(y, x)

    if isinstance(o1, type) and isinstance(o2, type):
        return comp(o1, o2)
    elif isinstance(o1, object) and isinstance(o2, object):
        return comp(type(o1), type(o2))
    raise TypeError("Cannot compare type and object")

#-------------------------------------------------------------------------------
# Operation


class Operation(ListWrapper):
    _attrs = dict(order = Attr(int, doc='An integer specifying the order in '
                               'which to perform the operation (smaller values'
                               ' are performed earlier)'),
                  repetitions = Attr(int, 0, doc='Number of times to repeat '
                                     'the operation'))
    _opts = dict(init_validate = True)

    def combine(self, other):
        '''Combine with another operation to increase execution efficiency.'''
        raise NotImplementedError

    def execute(self):
        '''Execute the operation on the system'''
        raise NotImplementedError

    def reduce(self, ops):
        '''Reduce a list of operations for optimizing total execution'''
        while ops:
            op = ops[0]
            if not subclass_equivalent(self, op):
                break
            
            self.compbine(op)
            ops.pop(0)


#-------------------------------------------------------------------------------
