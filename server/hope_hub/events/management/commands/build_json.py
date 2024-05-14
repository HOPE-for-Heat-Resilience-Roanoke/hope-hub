import json

from django.core.management.base import BaseCommand

from hope_hub.events.models import Engagement


class Command(BaseCommand):
    """Put an example of running this command in this comment so you can
    copy/paste to terminal later.

    Example:
    ./manage.py inspection
    """

    help = './manage.py inspection --help will print this out'

    # def add_arguments(self, parser):
    #     """Setup arguments.

    #     See here https://docs.python.org/3/library/argparse.html
    #     """
    #     parser.add_argument('required_argument', type=str)
    #     parser.add_argument('--bool_flag', dest='bool_flag', action='store_true', default=False)

    def handle(self, *args, **options):
        # Your command line arguments are in options
        # required_argument = options["required_argument"]
        # bool_flag = options["bool_flag"]

        data = [e.to_json() for e in Engagement.objects.filter(approved=True)]
        print(json.dumps(data))
