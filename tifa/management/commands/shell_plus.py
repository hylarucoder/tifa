import importlib
import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "shell plus"

    def handle(self, *args, **options):
        from IPython import embed
        import cProfile
        import pdb
        import django.apps

        models = {model.__name__: model for model in django.apps.apps.get_models()}
        main = importlib.import_module("__main__")
        ctx = main.__dict__
        ctx.update(
            {
                **models,
                "ipdb": pdb,
                "cProfile": cProfile,
            }
        )
        embed(user_ns=ctx, banner2="", colors="neutral", using="asyncio")
