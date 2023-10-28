import requests
import random
import string 
import time
import pyfiglet
from printy import printy



d = 0;
def generate(d):
	
	time.sleep(1)
	print("\nHow many codes do you want to generate?")
	num = int(input())
	time.sleep(1)
	with open("Nitro Codes"+str(d)+".txt", "w", encoding='utf-8') as f:
		print("\nCodes are being generated")
		d=d+1
		for i in range(num):
			code = "".join(random.choices(
				string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
			print("https://discord.gift/"+code+"\n")
			f.write(f"https://discord.gift/{code}\n")

	print("Generated "+str(num)+ " codes\n")
	printy("Select from the options bellow: \n\n", "pB")
	time.sleep(1)
	printy("1- Generate\n", "gB")
	printy("2- Check\n", "gB")


	 

def check():
	print("\nSelect the file that contains nitro codes")
	time.sleep(2)

	root = tk.Tk()
	root.withdraw()

	file_path = filedialog.askopenfilename()
	
	with open(file_path) as file:

		for line in file.readlines():


			nitro = line.strip("\n")

			url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

			r = requests.get(url)

			if r.status_code == 200:
				printy("\n[grD]"+nitro) 
				with open("Nitro Codes.txt", "w", encoding='utf-8') as f:
					f.write(str(nitro)+"\n")
			else:
				printy("\n[rD]"+nitro)  
	printy("Select from the options bellow: \n\n", "pB")
	time.sleep(1)
	printy("1- Generate\n", "gB")
	printy("2- Check\n", "gB")

			



#main code


result = pyfiglet.figlet_format("Nitro Gen", font = "doh" )
printy("[pD]"+result)
printy("                                                                                                                                  by Demitri\n\n\n", "rB")
time.sleep(1)

printy("1- Generate\n", "gB")
printy("2- Check\n", "gB")
printy("Select from [1/2]\n\n", "pB")

while True:
	op = input()
	if int(op) == 1:
		generate(d)
		continue
	elif int(op) == 2:
		check()
		continue
	else:
		continue


