from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mimesis import Text, Person, Internet
from random import randint
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
        from pile.models import Post, Favorite, Comment
        from django.contrib.auth.models import User
        from mimesis import Person, Text, Internet, Food
        
        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        food = Food('en')
    

        for _ in range(100):
            user = User.objects.create_user(person.username(), person.email(), 
                                            'password' )
            users.append(user)
        print("Users created") 
        print(users)
            # return users   

        print("Deleting Posts...")
        Post.objects.all().delete()
        print("Posts Deleted!")
        

        posts = []
        for i in range(90):
            post = Post(title=text.title(),
                author=users[i],
                link=internet.home_page(),
                description=text.quote(),
                slug=randint(1, 1000))

            post.save()
            posts.append(post)

        # for post_data in initial_posts:
            
        #     post = Post.objects.create(**post_data)
        #     for i in range(5):
        #         posts.append(post)
        print("Posts loaded!")
        #     { "title": text.title(),
        #     "author": users[1],
        #     "link": internet.home_page(),
        #     "description": text.quote(),
        #     "slug": food.vegetable()
        #     }, 
        #     { "title": text.title(),
        #     "author": users[2],
        #     "link": internet.home_page(),
        #     "description": text.quote(),
        #     "slug": food.vegetable()
        #     }, 
        #     { "title": text.title(),
        #     "author": users[3],
        #     "link": internet.home_page(),
        #     "description": text.quote(),
        #     "slug": food.vegetable()
        #     }, 
        #     { "title": text.title(),
        #     "author": users[4],
        #     "link": internet.home_page(),
        #     "description": text.quote(),
        #     "slug": food.vegetable()
        #     }
        # ]       

        # print("Deleting Posts...")
        # Post.objects.all().delete()
    
        # posts = []
        # for post_data in initial_posts:
        #     post = Post.objects.create(**post_data)
        #     initial_posts.append(post)
        # print("Posts loaded!")

        Favorite.objects.all().delete()
        for i in range(90):
            Favorite.objects.create(post=posts[randint(11, 89)], user=users[i])

        # for i in range(90):
        #     Favorite.objects.create(post=posts[randint(11, 89)], user=users[randint(11, 89)])

        print("Favorites added!")

        Comment.objects.all().delete()
        for i in range(90):
            Comment.objects.create(new_comment=text.quote(), post=posts[randint(5, 89)], author=users[i])
        print("Comments added!")

        # Favorite.objects.all().delete()
        # for i in posts:
        #     Favorite.objects.create(post=posts[i], user=users[i])
        #     Favorite.objects.create(post=posts[i], user=users[i])
        #     Favorite.objects.create(post=posts[i], user=users[2])
        #     Favorite.objects.create(post=posts[i], user=users[3])
        #     Favorite.objects.create(post=posts[i], user=users[i])
        #     Favorite.objects.create(post=posts[i], user=users[1])
        #     Favorite.objects.create(post=posts[i], user=users[0])
        #     Favorite.objects.create(post=posts[i], user=users[1])
        #     Favorite.objects.create(post=posts[i], user=users[2])
        #     print("Favorites added!")
