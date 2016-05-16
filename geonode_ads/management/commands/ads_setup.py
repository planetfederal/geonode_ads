import os
import shutil
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    help = 'Moves ADS default images to the correct image directory'

    def handle(self, *args, **options):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        ads_img_dir = os.path.join(current_dir, '../../static/img')
        src_files = os.listdir(ads_img_dir)
        dest = os.path.join(settings.MEDIA_ROOT, 'img')
        if not os.path.exists(dest):
            os.makedirs(dest)
        for file_name in src_files:
            full_file_name = os.path.join(ads_img_dir, file_name)
            if (os.path.isfile(full_file_name)):
                self.stdout.write("Copying " + file_name, ending='\n')
                shutil.copy(full_file_name, dest)
        self.stdout.write("Complete.", ending='\n')
