# -*- coding: utf-8 -*-
# Python
"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict
from dataclasses import dataclass
from json import dumps

critic = dict(
    name        = "critic",
    description = "criticize from all points of view the logical sentence that consists of antecedent and consequent",
    parameters  = {
        "type": "object",
        "properties": {
            "antecedent": {
                "type": "string",
                "description": "A concise logical statement of the problem that can be proven or disproven",
            },
            "consequent": {
                "type": "string",
                "description": "What allegedly follows from the antecedent"
            },
            "required": ["antecedent", "consequent"]
        }
    }
)

# description_of_the_function = """
# Call this function if the requested answer to a question or statement that you have prepared is not satisfactory.
# Explain what is wrong with the answer. Get a response accepting the answer or cancelling the previous request."""
# description_of_the_answer = """
# The answer that you have prepared but it is not good enough."""
# description_of_the_reason = "What exactly in this answer is not good enough?"
# definition = {
#         "name": "dont_like_the_answer",
#         "description": description_of_the_function,
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "answer_that_is_not_good": {
#                     "type": "string",
#                     "description": description_of_the_answer
#                 },
#                 "reason": {
#                     "type": "string",
#                     "description": description_of_the_reason
#                 }
#             },
#             "required": ["reason"]
#         }
#     }


@dataclass
class DontLikeTheAnswer(object):

    definition: Dict

    def __init__(self, **kwargs):
        """
            Either you call it with kwargs or there will be defaults.
        """
        description_of_the_function = kwargs.get("description_of_the_function", """
            Call this function if the requested answer to a question or statement that you have prepared is not satisfactory.
            Explain what is wrong with the answer. Get a response accepting the answer or cancelling the previous request.""")
        description_of_the_answer = kwargs.get("description_of_the_answer", """
            The answer that you have prepared but it is not good enough.""")
        description_of_the_reason = kwargs.get("description_of_the_reason", "What exactly in this answer is not good enough?")

        self.definition = {
            "name": "dont_like_the_answer",
            "description": description_of_the_function,
            "parameters": {
                "type": "object",
                "properties": {
                    "answer_that_is_not_good": {
                        "type": "string",
                        "description": description_of_the_answer
                    },
                    "reason": {
                        "type": "string",
                        "description": description_of_the_reason
                    }
                },
                "required": ["reason"]
            }
        }
        super(DontLikeTheAnswer, self).__init__()

    def __call__(self, **kwargs):
        return

    def __str__(self):

        return dumps(self.definition, indent=2)