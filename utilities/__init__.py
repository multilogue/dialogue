# -*- coding: utf-8 -*-
# Python
from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv()
from github_branches import creupdate_repo, creupdate_file


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