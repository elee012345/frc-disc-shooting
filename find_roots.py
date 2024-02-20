


def root_finder(equation: list, error) -> list:
    derivatives = [equation]
    # take derivatives of the equation down to the quadratic
    for i in range(len(equation) - 3):
        derivatives.append(take_derivative(derivatives[i]))
    # find solutions to the quadratic
    roots = sorted(quadratic_formula(derivatives[-1]))
    if len(roots) != 2:
        print("could not find roots :(")
        return
    # we just got the roots of the quadratic so we can remove it
    derivatives.pop(-1)
    for i in reversed(range(len(derivatives))):
        #print(i)
        new_roots = []
        new_roots.append(newtons_method(derivatives[i], roots[0] - 20, error))
        #print("done")
        for j in range(len(roots)-1):
            # we need to know if we're binary searching values that are ascending or descending
            if (function_output(derivatives[i], roots[j]) > function_output(derivatives[i], roots[j+1])):
                root = binary_search_descending(derivatives[i], roots[j], roots[j+1], error)
            else:
                root = binary_search_ascending(derivatives[i], roots[j], roots[j+1], error)
            # check if there are actually roots there
            if type(root) != bool:
                new_roots.append(root)

        new_roots.append(newtons_method(derivatives[i], roots[-1] + 20, error))
        roots = new_roots
    return roots


def take_derivative(equation: list) -> list:
    """
    Taking derivatives of simple polynomnials using the power rule
    """
    derivative = []
    largest_power = len(equation) - 1
    for i in range(largest_power):
        exponent = largest_power - i
        derivative.append(exponent * equation[i])
    return derivative

def quadratic_formula(equation: list) -> list:
    a = equation[0]
    b = equation[1]
    c = equation[2]
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    elif discriminant == 0:
        return [-b/(2*a)]
    square_root = discriminant ** 0.5
    return [(-b + square_root)/(2*a), (-b - square_root)/(2*a)]


def binary_search_descending(equation, left, right, error):
    while left <= right:
        mid = (left + right) / 2
        output = function_output(equation, mid)
        #print(left, right, mid, output)
        if within_range(output, 0, error):
            return mid
        elif output > 0:
            left = mid + error/100
        else:
            right = mid - error/100
    return False

def binary_search_ascending(equation, left, right, error):
    while left <= right:
        mid = (left + right) / 2
        output = function_output(equation, mid)
        #print(left, right, mid, output)
        if within_range(output, 0, error):
            return mid
        elif output < 0:
            left = mid + error/100
        else:
            right = mid - error/100
    return False

def function_output(equation: list, input):
    length = len(equation)
    return sum([equation[length - i - 1] * input**i for i in reversed(range(length))])

def within_range(num, target, range):
    return num <= target + range and num >= target - range

def newtons_method(equation, guess, error):
    # am lazy so i copied and pasted from here:
    # https://danielhomola.com/learning/newtons-method-with-10-lines-of-python/
    derivative = take_derivative(equation)
    delta = abs(0-function_output(equation, guess))
    while delta > error:
        guess = guess - function_output(equation, guess)/function_output(derivative, guess)
        delta = abs(0-function_output(equation, guess))
    return guess

# roots = root_finder([0.3, -3, 5, 3, -1], 0.001)
# print(roots)