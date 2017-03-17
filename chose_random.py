import csv
import random

filtered_rows = []
with open('user_albums_export.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['Rating']) >= 7:
            filtered_rows.append(row)

chosen_album = random.choice(filtered_rows)

print chosen_album['Title'] + ' ' + chosen_album[' First Name'] + ' ' + chosen_album['Last Name']
