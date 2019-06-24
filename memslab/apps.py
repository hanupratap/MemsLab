from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class MemslabConfig(AppConfig):
    name = 'memslab'
