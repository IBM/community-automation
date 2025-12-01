#!/usr/bin/python3

"""b64decode lookup plugin."""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import base64

from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_bytes, to_text

try:
    from ansible import context
except ImportError:
    context = False

DOCUMENTATION = """
    name: b64decode
    author: Glenn Marcy
    short_description: Decode base64 encoded text string
    description: Decodes the value of a string encoded with base64
    options:
      _terms:
        description: Text string encoded as base64
"""

EXAMPLES = """
    - name: Show decoded text
      debug: msg="{{ lookup('b64decode', encoded_string) }}"
      vars:
        encoded_string: "{{ 'hello' | b64encode }}"
"""

RETURN = """
_raw:
  description:
    - The decoded value of the base64 encoded text
  type: raw
"""


class LookupModule(LookupBase):
    """Define LookupModule."""

    def run(self, terms, variables=None, **kwargs):
        """Define run function."""
        ret = []

        for t in terms:
            ret.append(to_text(base64.b64decode(to_bytes(t, errors='surrogate_or_strict')), encoding='utf-8'))

        return ret
