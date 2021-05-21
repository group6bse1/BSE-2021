from os import path


def open_file():
	# function for requesting file name from user
	# and checking if the file exists in the specified directory or not
	while True:
		file = input('Enter file name: ')
		if path.exists(file):
			break
		else:
			print('Invalid file name or it does not exists!!')
	return open(file)


def inc_lv(a):
	# function for corresponding the set in_level elements to their respective representation in the file object
	if a == 1:
		return 'WB_LI'
	elif a == 2:
		return 'WB_LMI'
	elif a == 3:
		return 'WB_UMI'
	elif a == 4:
		return 'WB_HI'


def process_file(b):
	# function for processing the specific data from the file
	count = 0
	total = 0
	in_level = {1, 2, 3, 4}		# set for income levels to be input
	per_vaccinated = []		# list for storing specified percentages of vaccinated children
	country_hl = []		# list for storing specified countries
	file = b		# assigning file object to 'file'
	year = str(input('Enter year: '))
	income = int(input('Enter income level: '))
	if income in in_level:
		for line in file.readlines():
			if year in line[88:]:
				if inc_lv(income) in line[51:]:
					# converting to integer adding the vaccination percentages to the list
					per_vaccinated.append(int(line[59:61]))
					# removing whitespace at the end and adding the vaccination countries to the list
					country_hl.append(line[0:50].rstrip(' '))
					count = count + 1		# counting number of records specified
					total = total + int(line[59:61])		# Summing up all the percentages

		# computing the average percentage and obtaining the result without a fraction or decimal point.
		average_percent = total//count
		print('-------------------------------------------------')
		print('Number of records found: ', count)
		print('Average percentage of records: ', average_percent, '%')

		# obtain the index of the highest and lowest value from the list of 'per_vaccinated'
		index_high = per_vaccinated.index(max(per_vaccinated))
		index_low = per_vaccinated.index(min(per_vaccinated))
		print('\n')
		# using the index obtained above to get the country with the highest and lowest value from the list 'country_hl'
		print('Highest Record:')
		print('-------------------------------------------------')
		print('Country: ', country_hl[index_high], '\nChildren Vaccinated: ', max(per_vaccinated), '%')
		print('\n')
		print('Lowest Record:')
		print('-------------------------------------------------')
		print('Country: ', country_hl[index_low], '\nChildren Vaccinated: ', min(per_vaccinated), '%')

	else:
		print('Error occurred!!, income level not there...')
	b.close()


def main():
	# main() function to invoke all the above functions
	print('*******************************Welcome to WHO data Extractor**********************************')
	process_file(open_file())		# calling function to process file info
	print('\n')
	print('		(C) Group 6		')


main()
