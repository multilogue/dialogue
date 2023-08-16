# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import multilogue.utilities.chatgpt as chatgpt


hypothesis_yes = {
    "prompt": "Yes,",
    "suffix": "That is why the answer is yes.",
}
hypothesis_no = {
    "prompt": "No,",

    "suffix": "That is why the answer is no.",
}
hypothesis_unknown = {
    "prompt": "It is unknown,",
    "suffix": "That is why the answer is unknown.",
}
hypothesis_unknowable = {
    "prompt": "It is unknowable,",
    "suffix": "That is why the answer is unknowable.",
}

connector = {
    "prompt": " and here are the reasons why:",
}

question = {
    "prompt": "Can human nature be changed?",
}

hypothesis_list = [
    hypothesis_yes,
    hypothesis_no,
    hypothesis_unknown,
    hypothesis_unknowable
]

for hypothesis in hypothesis_list:
    prompt = f'{question["prompt"]} {hypothesis["prompt"]} {connector["prompt"]}'
    suffix = f'{hypothesis["suffix"]}'
    kwa = {
        "temperature" : 0.5,
        "top_p" : 1.0,
        "n" :  1,
        "best_of" : 3,
        "frequency_penalty" : 2.0,
        "presence_penalty" : 2.0,
        "max_tokens" : 256,
        "stop" : ["stop"]
    }
    response = chatgpt.fill_in(prompt, suffix, **kwa)
    print('ok')
