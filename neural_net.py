import random as rd
import csv
import numpy as np
import numdifftools as nd

"""
В этом словаре хранится информация о всех параметрах нашей уже обученной нейронной сети
"""
MODEL_INFO = {'w': np.array(), 'b': np.array()}


class Model:
    def __init__(self, input_layer: str):
        self.name = input_layer

    def input_layer(self):
        pass

    @staticmethod
    def forward():
        pass

    # метод для прогона значений слева-направо
    # метод для рандомной инициализации параметров
    # методы возврата любых значений на каждом слое


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


def train_model():
    """
    Сделана
    :return:
    """
    pass


nn = Model('784x16x10')

