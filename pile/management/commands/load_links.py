from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Command to load our user data and their links"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        from pile.models import Post
        from django.contrib.auth.models import User
        from mimesis import Person, Text, Internet
        # person = Person('en')
        # text = Text('en')
        # internet = Internet('en')

        # print("Deleting Posts...")
        # Post.objects.all().delete()
        
        # posts = []
        # for _ in range(5):
        #     post = Post.objects.create(text.title(), person.username(), internet.home_page(), text.quote())
        #     posts.append(post)
        # print("Posts loaded!")

        # print("Deleting users...")
        # User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for _ in range(5):
            user = User.objects.create_user(person.username(), person.email(), 
                                            'password' )
            users.append(user)
            print("Users created")

