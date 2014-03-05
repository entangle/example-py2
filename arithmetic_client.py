from entangle.constants import MAX_INT64, MIN_INT64
from entangle.exceptions import EntangleException
from definitions.arithmetic.clients import ArithmeticServiceClient


client = ArithmeticServiceClient(('127.0.0.1', 5555))

# Let's multiply some numbers!
for a, b in [
        (5, 6),
        (2, MAX_INT64),
        (MIN_INT64, MAX_INT64),
        (MIN_INT64, MIN_INT64),
        (0, 0),
]:
    try:
        result, trace = client.multiply_ints(a, b)
        print '%d * %d = %d' % (a, b, result)
    except EntangleException as e:
        print '%d * %d failed: %s' % (a, b, e)

# And then, divide some numbers.
for a, b in [
        (6, 5),
        (MAX_INT64, 2),
        (MIN_INT64, MAX_INT64),
        (MIN_INT64, MIN_INT64),
        (0, 0),
]:
    try:
        result, trace = client.divide_ints(a, b)
        print '%d / %d = %d' % (a, b, result)
    except EntangleException as e:
        print '%d / %d failed: %s' % (a, b, e)
