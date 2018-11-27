from django.core.management.base import BaseCommand
from mimesis import Person, Text
from pile.models import Post
import csv
from django.contrib.auth.models import User



class Command(BaseCommand):
    help = "Command to load our user data and their links"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):

        print("Deleting Posts...")
        Post.objects.all().delete()
        
        posts = []

        post = Post.objects.create(**post)
        posts.append(post)
        print("Posts loaded!")

