# API-versions-accepted

![example output in json notation](./output.png)
 

## Use Case Description

This script assists an API developer to determine which API versions are accepted with a specific Firepower Defense Manager console.
It can be run from any platform that has python3 installed.


## Installation

No dependencies outside python3 and the management IP address of the FDM-managed Firepower Threat Defense sensor.


## Configuration

No configuration possible. This script is a simple GET request for the accepted API versions.


## Usage

apiGET.py is a python script that makes use of the requests module to ask the target server what APIVersions it accepts.
There is only one input (first command line argument) which is an IP address.
The accepted API versions are the output.

To run the script use the following syntax:
`./apiGET.py <IP address of server>`
`python3 apiGET.py <IP address of server>`


### DevNet Sandbox

A great way to make your repo easy for others to use is to provide a link to a [DevNet Sandbox](https://developer.cisco.com/site/sandbox/) that provides a network or other resources required to use this code. In addition to identifying an appropriate sandbox, be sure to provide instructions and any configuration necessary to run your code with the sandbox.


## How to test the software

For testing, please review the "apiGETtest.py" script bundled in this repo.


## Known issues

Document any significant shortcomings with the code. If using [GitHub Issues](https://help.github.com/en/articles/about-issues) to track issues, make that known and provide any templates or conventions to be followed when opening a new issue. 


## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.


## Author(s)

This project was written and is maintained by the following individuals:

* Sudhir H. Desai <suddesai@cisco.com>
