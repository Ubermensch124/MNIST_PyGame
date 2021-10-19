from tqdm import tqdm
import random as rd
import csv
import numpy as np
import numdifftools as nd

"""
В этом словаре хранится информация о всех параметрах нашей уже обученной нейронной сети
"""
MODEL_INFO = {
    'w': {'w0': np.array([0.15, 0.20, 0.25, 0.40]), 'w1': np.array([0.40, 0.45, 0.50, 0.55])},
    'b': {'b0': np.array([0.35, 0.35]), 'b1': np.array([0.35, 0.35])}
}
MODEL_ARCHITECTURE = [784, 16, 10]


class Model:
    """
    Класс полносвязного перцептрона
    """
    def __init__(self, layers: list[int], ready_set=None):
        if ready_set:
            self.bias = ready_set['b']
            self.weights = ready_set['w']
            self.layers = {}
        else:
            count_layers = len(layers) - 1
            weights = {}
            bias = {}
            for i in range(0, count_layers):
                w = np.array([rd.random() for _ in range(layers[i] * layers[i + 1])])
                np.reshape(w, (layers[i], layers[i+1]))    # reshape(784, 16).transpose()
                np.transpose(w)
                weights[f'w{i}'] = w
                b = np.array([rd.random() for _ in range(layers[i + 1])])
                bias[f'b{i}'] = b
            self.bias = bias
            self.weights = weights
            self.layers = {}

    def forward(self, input_layer):
        self.layers['input_layer'] = input_layer
        for i in range(0, len(self.weights)):
            z = np.dot(self.weights[f'w{i}'], input_layer.transpose()) + self.bias[f'b{i}'].transpose()
            if i == len(self.weights):
                out = activation_func(z.transpose())
                self.layers['output_layer'] = softmax(out)
            else:
                input_layer = activation_func(z.transpose())
                self.layers[f'h{i}'] = input_layer

    def update_weights(self, number_of_layer: int) -> None:
        pass

    def update_bias(self, number_of_layer: int) -> None:
        pass


def softmax(a: list[float]):
    """
    SOFTMAX
    :return:
    """
    s = np.exp(a)
    res = np.array(list(map(lambda x: round(x / np.sum(s), 2), s)))
    return res


def loss_function(our: list[float], their: list[float]):
    """
    MSE
    :return:
    """
    cost = 1 / len(our) * np.sum(np.array([(our[i] - their[i]) ** 2 for i in range(len(our))]))
    return cost


def activation_func(a):
    """
    RELU
    :return:
    """
    new_a = np.array(list(map(lambda x: max(0.0, x), a)))
    return new_a


def prediction_model(input_array: list[int]) -> tuple[int, float]:
    """
    Берет значения всех параметров из отдельного файла. Просто прогоняет через
    нейронку с этими параметрами входные значения.
    :return: Ответ + точность предсказания
    """

    # из класса Model вызываем метод forward
    # потом вызываем метод для получения значений на последнем слое
    # потом применяем к массиву softmax
    # использовать np.amax() + np.index()
    digit = probability = 0
    return digit, probability


def train_model() -> None:
    """
    :return:
    """
    nn = Model(MODEL_ARCHITECTURE)
    epochs = 5
    fit_speed = 0.05
    for epoch in range(epochs):
        pass

    # проверяем на тестовых данных
    # записываем параметры в словарь


print(activation_func(np.array([1.3, 5.1, 2.2, 0.1, 1.1])))
