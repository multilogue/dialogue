# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import multilogue.utilities.chatgpt as chatgpt
from multilogue.participants import Expert


description_of_the_expert = f"""
Get an answer to any question regarding the area of expertise of the expert. 
The expert has been trained to answer questions about the area of expertise.
You need to specify the area of expertise of the expert, the question and the 
purpose of the question, what are you trying to achieve."""

# However, he can introduce a subconscious bias to his answers. Analyse whether
# the answer is trustworthy in your opinion.Take it into account or not
# according to the result of your assessment.

description_of_the_area_of_expertise = """
The area of expertise of the expert needed to answer the question.
"""

description_of_the_question = """
This is a question to the expert possessing knowledge of the area of expertise.
This expert might have participated in the previous conversation, then
what have been said by this entity should be taken into account when 
you will be asking the question."""

description_of_the_purpose = """
The reason why this question needs to be answered by this expert. For what
purpose is this question being asked?"""

function_descriptions = [
    {
        "name": "expert",
        "description": description_of_the_expert,
        "parameters": {
            "type": "object",
            "properties": {
                "area_of_expertise": {
                    "type": "string",
                    "description": description_of_the_area_of_expertise,
                },
                "question": {
                    "type": "string",
                    "description": description_of_the_question,
                },
                "purpose": {
                    "type": "string",
                    "description": description_of_the_purpose,
                }
            },
            "required": ["area_of_expertise", "question", "purpose"],
        },
    }
]


expert_definition = {
    'name': 'expert',  # name
    'role': 'expert on human nature',  # role in the dialogue
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
expert = Expert(**expert_definition)

general_instructions = {
        "role": "system",
        "content": f'Generate only the short answers to questions with no introductory text and conclusion text. '
      + f'Call Expert if you have a particular question regarding the discussed topic.'

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
    n=1,
    max_tokens=300,
    # presence_penalty=2.0,
    # frequency_penalty=2.0
)

for response in responses:
    if 'function_call' in response.values():
        message = response['message']
        try:
            function = globals()[message['function_call']['name']]
            result = function(**message)
        except Exception as e:
            print(e)
    print(response)

print('API call ok')