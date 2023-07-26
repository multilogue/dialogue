# -*- coding: utf-8 -*-
# Python
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


statement = """What's the weather like in Chicago, IL?"""
who = 'Alex'
messages = [
    {
        "role": "user",
        "name":f'{who}',
        "content": f'{statement}'
    }
]
functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions,
    function_call="auto",  # auto is default
)

response_messages = list()
for choice in response["choices"]:
    message = choice["message"]
    content = message.to_dict_recursive()

    print(dumps(content, indent=2))
    if message._previous['content'] == None:
        pass
    # dumps(response_message, indent=2)
    # if input('Keep this choice?') == 'y':
    #     response_messages.append(response_message)

print('ok')