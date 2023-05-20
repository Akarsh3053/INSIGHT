import requests, re, json
from colorama import init, Fore,  Back,  Style
from terminaltables import SingleTable

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"


def ipFinder():
	ip = input(" Enter the IP Address : ")
	print("\n"+wait+" Locating '%s'..." % (ip))

	TABLE_DATA = []

	url = "http://ip-api.com/json/"
	data = requests.get(url+ip).content.decode('utf-8')
	values = json.loads(data)

	status = values['status']

	if status != "success":
		print(warning+" Invalid IP Address.")

	else:
		infos = ("IP", ip)
		TABLE_DATA.append(infos)
		infos = ("ISP", values['isp'])
		TABLE_DATA.append(infos)
		infos = ("Organisation", values['org'])
		TABLE_DATA.append(infos)
		infos = ("Country", values['country'])
		TABLE_DATA.append(infos)
		infos = ("State", values['regionName'])
		TABLE_DATA.append(infos)
		infos = ("City", values['city'])
		TABLE_DATA.append(infos)
		infos = ("Postal Code", values['zip'])
		TABLE_DATA.append(infos)
		localisation = str(values['lat'])+', '+str(values['lon'])
		infos = ("Coordinates", localisation)
		TABLE_DATA.append(infos)
		infos = ("Maps", "https://www.google.fr/maps?q="+localisation)
		TABLE_DATA.append(infos)

		table = SingleTable(TABLE_DATA, ip)
		print("\n"+table.table)
