#!/usr/bin/python

'''Simple expression evaluator for PLN and reversed PLN.'''

class Evaluator(object):
    _funcs = {'+':lambda x, y: x+y,
                '-':lambda x, y: x-y,
                '*':lambda x, y: x*y,
                '/':lambda x, y: x/y,}
    def __init__(self, expression, notation, verbose):
        self.expr = expression.split(' ')
        self.notation = notation
        self.stack = []
        self.v = verbose
    def _apply(self, operator, operands):
        '''Applies ``operator`` to ``operands``.'''
        self.stack.append(Evaluator._funcs[operator](*operands))
    def evaluate(self):
        '''Evaluates expression. Raises ``ValueError`` on invalid elements.'''
        nodes = self.expr[::-1] if self.notation=='prn' else self.expr
        if self.v:
            print "Working nodes are {0}".format(nodes)
        for node in nodes:
            if node in self._funcs:
                if self.v:
                    print "Operator encountered: %s" % node
                opd1 = self.stack.pop()
                opd2 = self.stack.pop()
                if self.v:
                    print "Operands are: {0} {1}".format(opd1, opd2)
                self._apply(node, [opd1, opd2] if self.notation=='prn' else [opd2, opd1])
                if self.v:
                    print "Stack is: {0}".format(self.stack)
                continue
            num = float(node)
            self.stack.append(num)
            if self.v:
                print "Number encountered: {0}".format(num)
                print "Stack is: {0}".format(self.stack)
        return self.stack.pop()

if __name__ == '__main__':
    import sys
    notation = 'rprn'
    verbose = False
    if '-p' in sys.argv:
        notation = 'prn'
    if '-v' in sys.argv:
        verbose = True
    if '-e' in sys.argv:
        expr = sys.argv[sys.argv.index('-e')+1]
        evl = Evaluator(expr, notation, verbose)
        print "Evaluated value is: %f" % evl.evaluate()
