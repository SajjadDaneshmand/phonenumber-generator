import csv
import os

# internal
from . import settings
from . import tools


csv_reader = tools.read_prefix_from_csv(settings.CSV_FILE)


prefixes = settings.JsonConfigHandler(settings.PREFIXES_FILE)
for i in csv_reader:
    prefixes.set_config(i, 0)

prefixes.save_config()

if not os.path.exists(os.path.join(settings.BASE_DIR, settings.docs_folder)):
    os.makedirs(os.path.join(settings.BASE_DIR, settings.docs_folder))

if not os.path.exists(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.star_folder)):
    os.makedirs(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.star_folder))

if not os.path.exists(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.number_folder)):
    os.makedirs(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.number_folder))

for i in csv_reader:
    if not os.path.exists(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.number_folder, i)):
        os.makedirs(os.path.join(settings.BASE_DIR, settings.docs_folder, settings.number_folder, i))

config = settings.JsonConfigHandler()
config.set_config('setup-run', True)
config.save_config()
