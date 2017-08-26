# mortage_calculator.py
#
# Find out how long to pay off a mortgage

def mortage(principal, payment, rate, total_paid):
	while principal > 0:
		interest = principal*(rate/12)
		principal = principal + interest - payment
		total_paid += payment
	print('Total Paid:', total_paid)
	return 

mortage(500000, 2684.11,0.05,0)

	