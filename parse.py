import re

def parse(client_output):
	REGEXP = "(\d{1,4}.\d{1,4}-\d{1,4}.\d{1,4}) sec\s+(\d{1,4}.?\d{1,4})\s(\w?Bytes)\s+(\d{1,4}.?\d{1,4})\s\w?(bits/sec)"

	res = re.findall(REGEXP, client_output)
	l = []
	for tuple in res:
		l.append({'Interval': tuple[0],'Transfer': float(tuple[1]),'Transfer_rate': tuple[2],'Bandwidth': float(tuple[3]),'Bandwidth_rate': tuple[4]})
	return l
