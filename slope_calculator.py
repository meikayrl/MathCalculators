# (c) 2025 Mecah Rose A. Lao & Pinklet Alyanna M. Cubian
# E. Slope of a Road

def main():
	rise = int(input("Enter rise (m): "))
	run = int(input("Enter run (m): "))
	
	slope = (rise / run) * 100
	
	print(f"So, the slope of the road is {slope}%")
	
if __name__ == "__main__":
	main()
	
	