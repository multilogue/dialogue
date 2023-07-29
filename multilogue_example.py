# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from multilogue.utilities import chatgpt

messages = [
    {
        "role": "user",
        "name": "Alex",
        "content": "Can human nature be changed?"
    }
]
the_answer = chatgpt.answer(messages=messages)
print('ok')
