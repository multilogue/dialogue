# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import Any
from multilectic import Position
from multilogue import Entity


class Facilitator(Entity, Position):
    """ multilogue facilitator """
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


class Protagonist(Entity):
    """ multilogue protagonist """
    thesis: str = ''
    antithesis: str = ''
    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'protagonist'
        self.thesis = kwargs['thesis']
        super(Protagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        pass


class Antagonist(Entity):
    """ multilogue antagonist """
    thesis: str = ''
    antithesis: str = ''
    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'antagonist'
        self.thesis = kwargs['thesis']
        super(Antagonist, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        pass


class Interlocutor(Entity):
    """ multilogue interlocutor """
    opinion: str = ''
    utterance: str = ''

    def __init__(self, **kwargs):
        kwargs['role'] = 'protagonist'
        self.thesis = kwargs['thesis']
        super(Interlocutor, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        pass
