# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import Any


class Entity:
    """ human or other entity, participating in the multilogue """
    instruction:    str = ''
    functions:      str = ''
    python_code:    str = ''
    name:           str = ''

    def __init__(self, *args, **kwargs):
        pass


class Facilitator(Entity):
    """ multilogue facilitator """
    utterance: str = ''

    def __init__(self, *args, **kwargs):
        self.utterance = "I know nothing."
        super(Facilitator, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        pass


def protagonist(thought: str) -> str:
    def thesis(thought: str) -> str:
        return ''
    """Return what protagonist has to say about the given thought"""
    utterance = thesis(thought)
    return utterance


def antagonist(thought: str) -> str:
    def antithesis(thought: str) -> str:
        return ''
    """Return what antagonist has to say about the given thought"""
    utterance = antithesis(thought)
    return utterance


def interlocutor(name: str, thoughts: str) -> str:
    def response(thought: str) -> str:
        return ''
    """Return what interlocutor has to say about the given thought"""
    utterance = response(thoughts)
    return utterance
