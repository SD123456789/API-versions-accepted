#! /usr/bin/python3

"""
apiGET.py is a python script that makes use of the requests module to ask
the target server what APIVersions it accepts.
There is only one input (first command line argument) which is an IP address.
The accepted API versions are the output.

To run the script use the following syntax:
./apiGET.py <IP address of server>
python3 apiGET.py <IP address of server>
"""

import requests
import ipaddress
import sys
import os


def sanitizeInput(inputs):
	""" if there is more than one command line argument, exit """
	if len(inputs) != 2:
		print('Usage: %s  <IP address of API server>' % inputs[0])
		sys.exit(1)

	""" now that there is only one command line argument, make sure it's an IP & return """	
	try:
		IPaddr = ipaddress.ip_address(inputs[1])
		return IPaddr
	except ValueError:
	    print('address/netmask is invalid: %s' % inputs[1])
	    sys.exit(1)
	except:
	    print('Usage: %s  <IP address of API server>' % inputs[0])
	    sys.exit(1)



def getVersions(IPaddr):
	""" make sure IP exists """
	if (os.system("ping -c 1 -t 1 " + IPaddr) != 0):
		print("Please enter a useable IP address.")
		sys.exit(1)

	""" getting valid versions using the built-in module exceptions to handle errors """
	r = requests.get('https://{}/api/versions'.format(str(IPaddr)), verify=False)

	try:
		r.raise_for_status()
	except:
	    return "Unexpected error: " + str(sys.exc_info()[0])

	return r


if __name__ == "__main__":
	print(getVersions(sanitizeInput(sys.argv)).text + '\n')