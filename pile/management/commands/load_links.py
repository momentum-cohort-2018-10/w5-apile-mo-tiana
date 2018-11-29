from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mimesis import Text, Person, Internet
# from pile.models import Post


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
        from mimesis import Person, Text, Internet, Food
        
        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        food = Food('en')
    

        for _ in range(5):
            user = User.objects.create_user(person.username(), person.email(), 
                                            'password' )
            users.append(user)
            print("Users created") 
            print(users)
            # return users   

        for user in users:
            initial_posts = [
            { "title": text.title(),
            "author": users[0],
            "link": internet.home_page(),
            "description": text.quote(),
            "slug": food.vegetable()
            },
            { "title": text.title(),
            "author": users[1],
            "link": internet.home_page(),
            "description": text.quote(),
            "slug": food.vegetable()
            }, 
            { "title": text.title(),
            "author": users[2],
            "link": internet.home_page(),
            "description": text.quote(),
            "slug": food.vegetable()
            }, 
            { "title": text.title(),
            "author": users[3],
            "link": internet.home_page(),
            "description": text.quote(),
            "slug": food.vegetable()
            }, 
            { "title": text.title(),
            "author": users[4],
            "link": internet.home_page(),
            "description": text.quote(),
            "slug": food.vegetable()
            }
        ]       

        print("Deleting Posts...")
        Post.objects.all().delete()
    
        posts = []
        for post_data in initial_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print("Posts loaded!")






