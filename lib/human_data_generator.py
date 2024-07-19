import csv
from classes.Human import Human


def generate_human_data(csv_path):
    # fieldnames = ['timestamp', 'name', 'driveurl', 'email', 'country', 'city', 'work', 'company', 'contactme', 'imagename']
    with open(csv_path, newline='') as csvfile:
        # human_data = csv.DictReader(csvfile, delimiter=',', fieldnames=fieldnames)
        human_data = csv.DictReader(csvfile, delimiter=',')
        group_of_human = []
        for row in human_data:
            group_of_human.append(
                Human(
                    name=row['name'],
                    email=row['email'],
                    country=row['country'],
                    city=row['city'],
                    work=row['work'],
                    company=row['company'],
                    contactme=row['contactme'],
                    imagename=row['imagename'],
                )
            )

    return group_of_human
