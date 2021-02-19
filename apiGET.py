#! /usr/bin/python3

"""
apiGET.py is a python script that makes use of the requests module to ask
the target FDM-managed FTD sensor what APIVersions it accepts.
There is only one input (first command line argument) which is an IP address.
The accepted API versions are the output.

To run the script use the following syntax:
./apiGET.py <IP address of server>
python3 ./apiGET.py <IP address of server>
"""

import requests
import ipaddress
import sys
import os

from requests.models import HTTPError


def sanitizeInput(inputs):
	""" if there is more than one command line argument, exit """
	if len(inputs) != 2:
		print(f"Usage: {inputs[0]}  <IP address of FTD management interface>\n")
		sys.exit(1)

	""" now that there is only one command line argument, make sure it's an IP & return """	
	try:
		IPaddr = ipaddress.ip_address(inputs[1])
		return IPaddr
	except ValueError:
	    print(f"address/netmask is invalid: {inputs[1]}\n")
	    sys.exit(1)
	except HTTPError:
		print(f"address has no exposed API: {inputs[1]}\n")
		sys.exit(1)
	except:
	    print(f"Usage: {inputs[0]}  <IP address of FTD management interface>\n")
	    sys.exit(1)



def getVersions(IPaddr):
	""" make sure IP exists """
	IP = str(IPaddr)
	if (os.system(f"ping -c 1 -t 1 {IP}") != 0):
		print("Please enter a useable IP address.\n")
		sys.exit(1)

	""" getting valid versions using the built-in module exceptions to handle errors """
	r = requests.get('https://{}/api/versions'.format(str(IPaddr)), verify=False)

	try:
		r.raise_for_status()
	except:
		print(f"The IP address at {IPaddr} has no exposed API and has returned a {r.status_code} error.")
		exit(1)

	return r,IPaddr


if __name__ == "__main__":
	try:
		whichVersions, IP = getVersions(sanitizeInput(sys.argv))
		print(f"\n\nThe Firepower Device Manager at {IP} accepts the following API versions:\n{whichVersions.text}\n")
	except:
		exit(1)