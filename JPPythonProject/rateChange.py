# Import the modules needed
import twder
import pandas as pd


class Currency_convertor:
	# empty dict to store the conversion rates
	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self):
		df = pd.DataFrame()
		countries = ['AUD','EUR','GBP','JPY','KRW','TWD','USD']
		rates = []
		usd = float(twder.now('USD')[1])
		twd = 1/usd
		for country in countries[:-2]:
			rates.append(twd*float(twder.now(country)[1]))

		
		rates = rates + [twd, 1]
		# limiting the precision to 2 decimal places
		df['Currency'] = countries
		df['Rate'] = rates
		df.to_csv('./currencyrates.csv')

# Driver code
if __name__ == "__main__":

	c = Currency_convertor()

	c.convert()