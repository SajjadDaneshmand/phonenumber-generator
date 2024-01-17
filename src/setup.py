import csv
import os

# internal
import settings

with open(settings.CSV_FILE, 'r') as file:
    csv_reader = csv.reader(file)
    csv_reader = [i[0] for i in csv_reader]


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
