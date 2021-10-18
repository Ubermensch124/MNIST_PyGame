from tqdm import tqdm
import random as rd
import csv
import numpy as np
import numdifftools as nd

"""
В этом словаре хранится информация о всех параметрах нашей уже обученной нейронной сети
"""
MODEL_INFO = {'w': np.array(), 'b': np.array()}
MODEL_ARCHITECTURE = [784, 16, 10]


class Model:
    """
    Класс полносвязного перцептрона
    """
    def __init__(self, layers: list[int], ready_set=None):
        if ready_set:
            pass
        else:
            count_layers = len(layers) - 1
            weights = np.array([[]*count_layers])
            bias = np.array([[]*count_layers])
            for i in range(count_layers):
                w = np.array([rd.random() for _ in range(layers[i]*layers[i+1])])
                weights[i] = w
                b = np.array([rd.random() for _ in range(layers[i+1])])
                bias[i] = b
            self.bias = bias
            self.weights = weights
            self.output = np.array()

    def forward(self, input_layer: list[float]) -> list[float]:
        pass

    def update_weights(self, number_of_layer: int) -> None:
        pass

    def update_bias(self, number_of_layer: int) -> None:
        pass


def softmax():
    """

    :return:
    """
    pass


def loss_function():
    """

    :return:
    """
    pass


def activation_func():
    """

    :return:
    """
    pass


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

