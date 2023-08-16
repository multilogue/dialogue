# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import multilogue.utilities.chatgpt as chatgpt
import multilogue.utilities.functions as functions


dont_like_the_answer = functions.DontLikeTheAnswer(functon='dont_like_the_answer')

general_instructions = {
        "role": "system",
        "content": f'Generate only the short answers to questions with no introductory text and conclusion text. '
      + f'Call dont_like_the_answer function if the answer you come up with does not satisfy you.'

}
messages = [
    # general_instructions,
    {
        "role": "user",
        "name": "Alex",
        "content": "Can human nature be changed?",
    }
]

responses = chatgpt.answer(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=[dont_like_the_answer.definition],
    function_call="auto",
    temperature=0.5,
    # top_p=1.0,
    n=1,
    max_tokens=3000,
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