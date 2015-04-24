# coding: utf-8
"""
    Open graph parser
    ~~~~~~~~~~~~~~~~~

    Parsing open graph meta data, including twitter cards.
"""

import re

# use simple regex, no need for lxml
HEAD = re.compile(r'<head>(.*?)</head>', re.I | re.S)
META_TAG = re.compile(r'<meta.*?/?>', re.I | re.S)
META_ATTR = re.compile(r'(name|property|content)=(?:"|\')(.*?)(?:"|\')', re.I)
