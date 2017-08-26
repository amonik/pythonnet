from netmiko import ConnectHandler
platform = 'arista_eos'
username = 'admin'
password = 'arista'
devices = ['10.1.1.3','10.1.1.4']
# append to text file
f = open('device.txt', 'a')
# SSH to each host in array and run a show version on it, then append the output to a file.
for host in devices:
	sshconnect = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
	f.write(host + ':\n\n')
	f.write(sshconnect.send_command('show version'))




try:
	# Some commands on data
	# Add some Exception, like ValueError
except ValueError as err:
	# This will show what has the error
	print('Bad data:'data)
	# This will show you what the error is
	print('Reason:' err)
	continue # Skips to next item in loop
	raise err



