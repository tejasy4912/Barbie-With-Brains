
from os.path import abspath, dirname, join

from mycroft.api import Api
from mycroft.messagebus.message import Message
from mycroft.skills.context import adds_context, removes_context
from mycroft.skills import (MycroftSkill, FallbackSkill,
                            intent_handler, intent_file_handler)
from mycroft.skills.intent_service import AdaptIntent
from mycroft.util.log import LOG

MYCROFT_ROOT_PATH = abspath(join(dirname(__file__), '..'))

__all__ = ['MYCROFT_ROOT_PATH',
           'Api',
           'Message',
           'adds_context',
           'removes_context',
           'MycroftSkill',
           'FallbackSkill',
           'intent_handler',
           'intent_file_handler',
           'AdaptIntent']

LOG.init()
