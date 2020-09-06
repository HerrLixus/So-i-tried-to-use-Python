import numpy as np
import numba


@numba.jit(nopython=True)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


inputs_for_test = np.array([])

expected_outputs = np.array([])


@numba.jit(nopython=True, parallel=True)
def train(inputs, weight, expected):
    output = sigmoid(np.dot(inputs, weight))
    error = expected - output
    adj = np.dot(inputs.T, error*(output*(1-output)))
    weight = weight + adj
    return weight


@numba.jit(nopython=True, parallel=True)
def form_weights(train_data, etal):
    weight = 2 * np.random.random((2, 1)) - 1
    for i in range(200):
        weight = train(train_data, weight, etal)
    # out = sigmoid(np.dot(inp, weight))
    # out = list(map(lambda x: x[0], out))
    # out = list(map(lambda x: 1 if x > 0.5 else 0, out))
    return weight


# print(*form_outputs(inputs_for_test, np.array([0, 1, 0]), expected_outputs))
