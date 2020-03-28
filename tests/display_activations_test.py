import os
import unittest
from glob import glob

import tensorflow.keras.backend as K
import numpy as np
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Dense

from keract import get_activations, display_activations


def dummy_model_and_inputs():
    i1 = Input(shape=(10,), name='i1')
    a = Dense(1, name='fc1')(i1)
    model = Model(inputs=[i1], outputs=[a])
    x = np.random.uniform(size=(1, 10))
    return model, x


class DisplayActivationsTest(unittest.TestCase):

    def setUp(self) -> None:
        K.clear_session()

    def tearDown(self) -> None:
        K.clear_session()
        for image in glob('*.png'):
            os.remove(image)

    def test_display_1(self):
        model, x = dummy_model_and_inputs()
        acts = get_activations(model, x)
        display_activations(acts, save=True)
