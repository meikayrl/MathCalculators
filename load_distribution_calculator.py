def main ():
	beam_load = int(input("Enter beam load (N/m): "))
	length = int(input("Enter length (m): "))
	
	Force = beam_load * length
	
	print (f"So, the total load acting on the beam is {Force} N.")
	
if __name__ == "__main__":
	main()