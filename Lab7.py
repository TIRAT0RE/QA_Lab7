import subprocess
import paramiko
from parse import parse
import pytest 

server_ip = '192.168.0.1'
password = 'tiratore250701'
username = 'tiratore'
port = 22

#@pytest.fixture(scope="function")
def server():
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname=server_ip, username=username, password=password, port=port)
	print('connected')
	stdin, stdout, stderr = client.exec_command('iperf -s')
	print('iperf -s started')
	client.close()
	print('closed server')

#@pytest.fixture(scope='function')
def client (server_ip=server_ip):
	my_iperf_process = subprocess.Popen(["iperf", "-c", server_ip,"-t 10","-i 1"],stdout=subprocess.PIPE)

	return my_iperf_process.communicate()



server()
result, error = client()
result = result.decode('utf-8')
#print(result)
"""
result_list = parse(result)
	
if error:
	print(error)
else:
	for value in result_list:
		if float(value['Transfer']) > 10:
			print(value)
"""