from numpy import array, dot, exp
from datetime import datetime

txt_file = open('txt_file.txt', 'w')
log_file = open('log_file.csv', 'w')

txt_file.write(str(datetime.now())+'\n')
log_file.write('time,values\n')

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
    log_file.write(str(datetime.now()) + ',' + str(weights)+'\n')


txt_file.write(
    str("[1, 0, 0] =" + str(1 / (1 + exp(-(dot(array([1, 0, 0]), weights))))))+'\n')
txt_file.write(str(datetime.now()))

txt_file.close()
log_file.close()
