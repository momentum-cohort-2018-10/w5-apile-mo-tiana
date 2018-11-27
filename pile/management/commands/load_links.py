from django.core.management.base import BaseCommand
from mimesis import Person, Text, 


class Command(BaseCommand):
    help = "Command to load our user data and their links"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        raise NotImplementedError()
