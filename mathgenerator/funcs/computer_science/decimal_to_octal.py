from .__init__ import *


def decimalToOctalFunc(maxDecimal=4096, format='string'):
    x = random.randint(0, maxDecimal)
    problem = "The decimal number " + str(x) + " in Octal is: "
    solution = oct(x)

    if format == 'string':
        return problem, solution
    else:
        return x, oct(x)


decimal_to_octal = Generator("Converts decimal to octal", 84,
                             decimalToOctalFunc, ["maxDecimal=4096"])
