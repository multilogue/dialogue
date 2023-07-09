# -*- coding: utf-8 -*-
# Python
def facilitator(multilogue: str) -> str:
    """Return what facilitator has to say about the given thought"""
    utterance = multilogue
    return utterance


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


def presuppositions(assertion: str) -> str:
    def implicit_assumptions(utterance: str) -> str:
        return ''
    """Return what presupposition has to say about the given thought"""
    utterance = implicit_assumptions(assertion)
    return utterance