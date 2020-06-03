import datetime
import json
import os
from io import BytesIO

from django.core.management import BaseCommand
from django.conf import settings
from django.utils import timezone
from shop.models import Product
from PIL import Image
from django.core.files.base import ContentFile


PRODUCT_DIR = os.path.join(
    settings.BASE_DIR,
    'data',
    'products'
)

IMG_DIR = os.path.join(
    settings.BASE_DIR,
    'data',
    'img'
)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-t', '--truncate',
            help='Clear the database before loading the data',
            action='store_true',
            default=False
        )

    def handle(self, *args, **options):
        if options['truncate']:
            Product.objects.all().delete()

        for file in os.listdir(PRODUCT_DIR):
            with open(
                os.path.join(PRODUCT_DIR, file)
            ) as f:
                data = json.load(f)
                txt = data['name']
                image = None

                product = Product.objects.create(
                    name=txt,
                    category=data['category'],
                    image=image,
                    price=data['price'],
                    description=data['description'],
                    height=data['height'],
                    width=data['width'],
                    manufacturer=data['manufacturer'],
                    reinforcement_material=data['reinforcement_material'],
                    power=data['power'],
                    armature_color=data['armature_color'],
                    lighting_area=data['lighting_area'],
                    number_of_lamps=data['number_of_lamps'],
                    created=timezone.now()
                )
                '''if data['image']:
                    image_name = data['image']
                    im = Image.open(
                        os.path.join(IMG_DIR, image_name)
                    )
                    thumb_to = BytesIO()
                    im.thumbnail((220, 130), Image.ANTIALIAS)
                    im.save(thumb_to, im.format, quality=60)

                    product.image = im
                    product.image.save(im.filename, ContentFile(thumb_to.getvalue()), save=False)
                '''
                product.save()