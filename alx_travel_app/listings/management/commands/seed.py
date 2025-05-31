from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with listings and users'

    def handle(self, *args, **kwargs):
        for i in range(10):
            Listing.objects.create(
                title=f"Listing {i + 1}",
                description="Form imekubali",
                price_per_night=random.randint(50, 500),
                location=f"Kanairo {random.randint(1, 100)}",
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with listings'))