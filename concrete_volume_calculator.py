# (c) 2025 Mecah Rose A. Lao & Pinklet Alyanna M. Cubian
# C. Concrete Volume Calculation

def main():
	length = float(input("Enter length (m): "))
	width = float(input("Enter width (m): "))
	height = float(input("Enter height (m): "))
	
	volume = length * width * height
	
	print (f"So, you need {volume:,.2f} cubic meters of concrete.")
	
if __name__ == "__main__":
	main()