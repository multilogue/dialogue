# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict


class Left(object):
    def __init__(self):
        super(Left, self).__init__()
        print("left")


class Right(object):
    conversation: List[Dict]

    def __init__(self):
        super(Right, self).__init__()
        print("right")


class Child(Left, Right):
    name: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super(Child, self).__init__()
        print("child")


if __name__ == '__main__':
    kwa = {
        'conversation': [
            {'role': 'user',
            'name': 'Alex',
            'content': 'What\'s the weather like in Chicago, IL?'
             }
        ],
        'name': 'Alex'
    }
    chi = Child(**kwa)
    print('ok')