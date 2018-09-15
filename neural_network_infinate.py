from numpy import array, dot, exp
from datetime import datetime

weight_logs = open('weight_logs.csv', 'w')
program_logs = open('program_logs.txt', 'w')

program_logs.write(
    str(datetime.now())
    + '\n'
)

input_set = array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])

output_set = array([
    [0],
    [1],
    [1],
    [0]
])

weights = array([
    [0.],
    [0.],
    [0.]
])

while True:
    weight_logs.write(
        str(weights[0][0]) + ',' +
        str(weights[1][0]) + ',' +
        str(weights[2][0])+'\n'
    )

    mat_mul = dot(input_set, weights)

    prediction = 1 / (1 + exp(-mat_mul))
    error = output_set - prediction

    new_weights = weights + dot(
        input_set.T,
        error * prediction * (1 - prediction)
    )

    if all(new_weights == weights):
        break

    weights = new_weights


program_logs.write(
    "[1, 0, 0] = "
    + str(1 / (1 + exp(-(dot(array([1, 0, 0]), weights)))))
    + '\n'
)

program_logs.write(str(datetime.now()))
