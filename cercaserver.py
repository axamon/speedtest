import re
import requests
from xml.etree import ElementTree

citta = []
link = []
servers = {}
resp = requests.get('http://www.speedtest.net/speedtest-servers.php')
tree = ElementTree.fromstring(resp.content)
for node in tree.iter('server'):    
      if node.attrib.get('country') == "Italy" and node.attrib.get('sponsor') == "Telecom Italia S.p.A.":
            a = node.attrib.get('name')
            citta.append(a)

for node in tree.iter('server'):
		for city in citta:
			if node.attrib.get('name') == city:
				l = node.attrib.get('url')
				url = re.sub(r'upload.*','latency.txt',l)
				#link.append(nl)
				isp = node.attrib.get('sponsor')
				id = node.attrib.get('id')
				servers[id] = {'isp': isp, 'citta' : city, 'url' : url}
				
print(servers)			
			
print(''' i server telecom sono presenti nelle seguenti città''')
print(citta)
print(link)

