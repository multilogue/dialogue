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
kwa = {'top_p': 0.1, 'n': 2, 'max_tokens': 100}
the_answer = chatgpt.answer(messages=messages, **kwa)
print('ok')
