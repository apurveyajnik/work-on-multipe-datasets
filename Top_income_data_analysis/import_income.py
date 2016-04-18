import csv

data_file = "data.csv"
'''
with open(data_file,'r') as csvfile:
	reader = csv.DictReader(csvfile)
	data = list(reader)

print(len(data))

print(len(reader.fieldnames))
'''

def dataset(path):
	with open(path,'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			yield row


print(min([int(row["Year"]) for row in dataset(data_file)]))	
print(max([int(row["Year"]) for row in dataset(data_file)]))

filter(lambda row: row["Country"] == "United States",dataset(data_file))

print({row["Country"] for row in dataset(data_file)})
	
