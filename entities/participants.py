# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from typing import Any


class Entity:
    """ Human or other entity, participating in the multilogue """
    instruction:    str = ''
    functions:      str = ''
    python_code:    str = ''
    name:           str = ''
    role:           str = ''

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    def __repr__(self, *args, **kwargs):
        return f"""     Entity:
            intruction - {self.instruction},
            functions - {self.functions},
            python_code - {self.python_code},
            name - {self.name},
            role - {self.role},
            """


class Facilitator(Entity):
    """ multilogue facilitator """
    utterance: str = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.utterance = "I know nothing."
        super(Facilitator, self).__init__(**kwargs)

    def __call__(self, *args, **kwargs):
        ...
        return self.utterance

    def __repr__(self):
        pass


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
