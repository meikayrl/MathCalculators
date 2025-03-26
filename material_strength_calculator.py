# (c) 2025 Mecah Rose A. Lao & Pinklet Alyanna M. Cubian
# B. Material Strength Calculation for Steel

def main():
	force = float(input("Enter force (N): "))
	area = float(input("Enter cross-sectional area (mm**2): "))
	
	conversion = area * 0.000001
	
	stress = force / conversion
	
	print(f"So the stress on the beam is {stress:,.2f} Pa.")

if __name__ == "__main__":
	main()