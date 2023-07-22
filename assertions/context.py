# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

metacontext = dict(
    world       = """the general state of affairs and knowledge available in the world before the cutoff date""",
    system      = """the AI language model itself, known as ChatGPT""",
    user        = """the entity that engages in a conversation with the AI model; it initiates the conversation, asks questions, provides information, and guides the direction of the interaction; user can have a name, then she or he should be addressed by that name""",
    function    = """one of the functions described in the current call of the system; has name and parameters""",
    name        = """the name of the function or user, participating in the interaction"""
)

presuppositions = dict(
    existence   = """objects and entities, discussed in the statements, exist"""
)
