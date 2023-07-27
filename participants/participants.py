# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import List, Dict
from multilectic import Position
from multilogue import Entity


class Facilitator(Entity, Position):
    """ Multilogue facilitator

        Entity.  # from multilogue
            name: str
            role: str  # role in the multilogue, not an API role
            instructions: str
            functions: str
            python_code: str
        Positions.  # from multilectic
            thesis: str
            antithesis: str
            facts: List
            presuppositions: List[str]
            conversation: List[Dict]
    """
    utterance: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.utterance = "I am a facilitator"
        super(Facilitator, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class Protagonist(Entity, Position):
    """ multilogue protagonist """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'protagonist'
        self.thesis = kwargs['thesis']
        super(Protagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class Antagonist(Entity, Position):
    """ multilogue antagonist """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'antagonist'
        self.thesis = kwargs['thesis']
        super(Antagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"


class Interlocutor(Entity, Position):
    """ multilogue interlocutor """

    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'interlocutor'
        self.thesis = kwargs['thesis']
        super(Interlocutor, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        return f"{self.name}, {self.role}"
