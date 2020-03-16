import csv

with open('names.csv', 'r') a csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open('save_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name']

		csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter ='\t')
		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)


.DictReader
.DictWriter

# Create_name.csv
# save_names.csv
# ID must be inserted first
# to add header in excel
# separate between first_name and last_name
# ID, first_name and last_name must be consequetive in the new excel file