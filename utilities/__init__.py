# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""

from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv()
from github_records import creupdate_repo, creupdate_file

"""OPENAI_API_KEY or OPENAI_API_KEY_PATH,
OPENAI_ORGANIZATION can be set... or not.
The properly named environment variables are loaded
into the OpenAI library by its' __init__"""


organization    = getenv('GITHUB_ORGANIZATION', 'multilogue')
github_token    = getenv('GITHUB_TOKEN', '')
github_name     = getenv('GITHUB_NAME', '')
github_email    = getenv('GITHUB_EMAIL', '')

__all__ = [
    # organization,
    # github_token,
    # github_name,
    # github_email,
    creupdate_repo,
    creupdate_file
]