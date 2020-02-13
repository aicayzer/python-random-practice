



import csv


def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))

# with open(csv_file, 'a') as f:
#   writer = vcs.writer(f)  # Note: writes lists, not dicts.
#   for data in rows_to_append:  # Maybe your df, or whatever iterable.
#     writer.writerow([data['toto'], data['tata'], data['titi']]




def add_users():
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.DictWriter(csvfile)
        for data in csv_writer:  # Maybe your df, or whatever iterable.
          writer.writerow([data['toto'], data['tata']])

print_users()
add_users()
