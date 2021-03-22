import numpy as np

res_malhas = np.array([  # I1, I2, I3 das malhas
    [3, -1, -2],
    [-1, 5, -9],
    [-2, -4, 9]
])
tensoes_malhas = np.array(  # valor de igualdade das malhas
    [8,
     0,
     0]
)
res_malhas = np.linalg.inv(res_malhas)
correntes = res_malhas * tensoes_malhas

print(correntes[0][0], '\n', correntes[1][0], '\n', correntes[2][0])  # valor das correntes das malhas
