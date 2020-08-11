import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_four.settings')

import django
django.setup()

## fake pop script
import random
from fourth_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        #create the fkae data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the fake webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create the fake access record entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
