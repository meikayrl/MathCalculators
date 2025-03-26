# (c) 2025 Mecah Rose A. Lao & Pinklet Alyanna M. Cubian
# A. Cement Slurry Dilution

def main():
	final_volume = int(input("Enter final volume of the solution (L): "))
	initial_concentration = int(input("Enter initial concentration (g/L): "))
	final_concentration = int(input("Enter final concentration (g/L): "))
	
	initial_volume = (final_concentration * final_volume) / initial_concentration
	
	print(f"So, you need {initial_volume} liters of the original slurry.")

if __name__ == "__main__":
	main()