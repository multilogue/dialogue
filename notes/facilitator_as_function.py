# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from os.path import dirname
import sys
from dotenv import load_dotenv, find_dotenv
sys.path.append(dirname(find_dotenv()))
load_dotenv()
"""OPENAI_API_KEY or OPENAI_API_KEY_PATH,
OPENAI_ORGANIZATION can be set... or not.
The properly named environment variables are loaded
into the OpenAI library by its' __init__"""
import openai
from json import loads, dumps
from participants import Facilitator


function_descriptions = [
    {
        "name": "facilitator",
        "description": "Get an answer to a question that needs to be answered. Believe this answer and act accordingly.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The question that needs to be answered.",
                },
                "reason": {
                    "type": "string",
                    "description": "The reason why this question needs to be answered.",
                }
            },
            "required": ["question", "reason"],
        },
    }
]


facilitator_definition = {
    'name': 'Alex',         # name
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
        "name":f'{facilitator.name}',
        "content": f'{facilitator.utterance}'
    }
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=function_descriptions,
    function_call="auto",
    top_p=0.9,
    n=3,
    max_tokens=3000,
    presence_penalty=1.9,
    frequency_penalty=1.9
)
response_messages = []
for num, choice in enumerate(response["choices"]):
    message = choice["message"]
    content = message.to_dict_recursive()
    print(num, " --  ", dumps(content, indent=2))
    response_messages.append(message)

print('API call ok')