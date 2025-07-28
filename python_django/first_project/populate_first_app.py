import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    """
    Add a topic to the database using a random topic name from the
    predefined list of topics.

    Returns:
        Topic: The topic added to the database.
    """
    t = Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    """
    Populate the database with fake entries. The number of entries to
    create is specified by the parameter N. If N is not specified, the
    default is 5.

    :param N: The number of entries to create.

    :return: None
    """
    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("Populating data into the models!")
    populate(20)
    print("Populating complete!")


