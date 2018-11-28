from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mimesis import Text, Person, Internet


person = Person('en')
text = Text('en')
internet = Internet()





class Command(BaseCommand):
    help = "Command to load our user data and their links"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        from pile.models import Post
        from django.contrib.auth.models import User
        from mimesis import Person, Text, Internet
        
        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for _ in range(5):
            user = User.objects.create_user(person.username(), person.email(), 
                                            'password' )
            users.append(user)
        print("Users created")        

        for user in users:
                initial_posts = [
                { "title": text.title(),
                "author": user,
                "link": internet.home_page(),
                "description": text.quote()
                }, 
                    { "title": text.title(),
                "author": user,
                "link": internet.home_page(),
                "description": text.quote()
                }, 
                    { "title": text.title(),
                "author": user,
                "link": internet.home_page(),
                "description": text.quote()
                }, 
                    { "title": text.title(),
                "author": user,
                "link": internet.home_page(),
                "description": text.quote()
                }, 
                    { "title": text.title(),
                "author": user,
                "link": internet.home_page(),
                "description": text.quote()
                }
            ]       

        print("Deleting Posts...")
        Post.objects.all().delete()
        
        posts = []
        for post_data in initial_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print("Posts loaded!")






