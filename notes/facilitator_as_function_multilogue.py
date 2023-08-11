# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

import multilogue.utilities.chatgpt as chatgpt
from multilogue.participants import Facilitator, Expert


description_of_the_function = """
Get an answer to a question of interest. Analyse whether it is trustworthy.
Take it into account or not according to the result of your assessment."""

description_of_the_qestion = """
This is a question to an entity mentioned in the name of the function.
This entity might have participated in the previous conversation, then
what have been said by this entity should be taken into account when 
you will be asking the question."""

description_of_the_purpose = """
The reason why this question needs to be answered. For what
purpose is this question being asked?"""

function_descriptions = [
    {
        "name": "facilitator",
        "description": description_of_the_function,
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": description_of_the_qestion,
                },
                "purpose": {
                    "type": "string",
                    "description": description_of_the_purpose,
                }
            },
            "required": ["question", "purpose"],
        },
    }
]


facilitator_definition = {
    'name': 'facilitator',  # name
    'role': 'facilitator',  # role in the dialogue
    'instructions': '',     # The facilitator is a human by definition.
    'functions': [],        # no function_descriptions
    'python_code': '',      # no Python code
    'thesis': '',
    'antithesis': '',
    'facts': [],
    'presuppositions': [],
    'assumptions': [],
    'utterance': ''
}
facilitator = Facilitator(**facilitator_definition)
facilitator.utterance = f'Can human nature be changed?'

general_instructions = {
        "role": "system",
        "content": f'Generate only the short answers to questions with no introductory text and conclusion text. '
    +   f'Call facilitator if you need guidance or need to make a choice between several alternatives. '
    +   f'Facilitator is an expert on any subject, he can help.',
}
messages = [
    general_instructions,
    {
        "role": "user",
        "name": "Alex",
        "content": "Can human nature be changed?",
    }
]

responses = chatgpt.answer(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=function_descriptions,
    function_call="auto",
    temperature=0.5,
    # top_p=1.0,
    n=3,
    max_tokens=300,
    # presence_penalty=2.0,
    # frequency_penalty=2.0
)

print('API call ok')