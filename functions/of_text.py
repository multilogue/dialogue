# -*- coding: utf-8 -*-
# Python

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