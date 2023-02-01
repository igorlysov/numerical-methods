import numpy as np
import warnings

type_display = {
    'float16': np.float16,
    'float32': np.float32,
    'float64': np.float64
}


def calculate_machine_constants(type_name):
    k = 0
    number_type = type_display[type_name]
    num = number_type(1)
    while num != 0:
        num = number_type(num / 2)
        k += 1
    print(f"{type_name} machine zero: 2^({-k})")

    k = 0
    num = number_type(1)
    while num != np.inf:
        num = number_type(num * 2)
        k += 1
    print(f"{type_name} machine infinity: 2^{k}")

    k = 0
    num = number_type(1)
    while 1.0 + num > 1.0:
        num = number_type(num / 2)
        k += 1
    print(f"{type_name} machine epsilon: 2^({-k})")


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for typename in type_display.keys():
        print()
        calculate_machine_constants(typename)
