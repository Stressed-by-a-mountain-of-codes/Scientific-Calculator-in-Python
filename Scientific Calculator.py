import math
import operator

class HybridCalculator:
    def __init__(self):
        self.binary_ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': self.safe_divide,
            '^': operator.pow,
            'pow': operator.pow
        }
        self.unary_funcs = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'log': math.log,
            'log10': math.log10,
            'sqrt': math.sqrt,
            'exp': math.exp,
            'degrees': math.degrees,
            'radians': math.radians,
            'factorial': math.factorial,
            'ceil': math.ceil,
            'floor': math.floor,
            'abs': abs
        }

    def safe_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError('Division by zero')
        return a / b

    def evaluate(self, expr):
        tokens = expr.strip().split()
        if len(tokens) == 2:
            func, val = tokens[0], float(tokens[1])
            if func not in self.unary_funcs:
                raise ValueError(f'Unsupported function: {func}')
            return self.unary_funcs[func](val)
        elif len(tokens) == 3:
            a, op, b = float(tokens[0]), tokens[1], float(tokens[2])
            if op not in self.binary_ops:
                raise ValueError(f'Unsupported operator: {op}')
            return self.binary_ops[op](a, b)
        else:
            raise SyntaxError('Invalid input format')


if __name__ == '__main__':
    calc = HybridCalculator()
    expr = input('Enter expression (e.g. 2 + 3 or sin 0.5): ')
    result = calc.evaluate(expr)
    print(f'Result: {result}')
