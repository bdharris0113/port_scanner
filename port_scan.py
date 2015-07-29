#! bin/python


import urllib2, socket,sys,nmap,os,ftplib


def rscan(url):
	socket.setdefaulttimeout(1)
	rec = None
	#url = 'www.google.com'
	print url
	for i in range(78,82):
		try:
			s = socket.socket()
			s.connect((url,i))
			print "%s open on %d" % (url,i)
			s.send("HEAD / HTTP/1.0\r\n\r\n")
			rec = s.recv(1000)
	
			s.close()
		except:
			print "port %d closed" % i
	print "\n\n"
	if rec == None:
		return 
	else:
		return rec

def nscan(host,port):
	nmScan = nmap.PortScanner()
	nmScan.scan(host,port)
	state = nmScan[host]['tcp'][int(port)]['state']
	print host + " tcp/" + port + ' ' + state


def anonlog(host):
	try:
		ftp = ftplib.FTP(host)
		ftp.login('anonymous','me@your.com')
		print 'anon login at ' + host + ' successful'
		ftp.quit()
		return True
	except Exception, e:
		print 'anon login at ' + host + ' failed'
		return False


def main():
	while 1:
		x = raw_input('OPTIONS: \n scan (find open ports) \n nscan (full nmap report) \n  ftp (is anon ftp available) \n exit (exit system) \n')
		if x == 'scan':
			y = raw_input('url to scan: ')
			rscan(y)
		elif x == 'nscan':
			y = raw_input('url to scan: ')
			z = raw_input('port to search: ')
			nscan(y,z)
		elif x == 'exit':
			os.system('clear')
			exit()
		elif x == 'ftp':
			y = raw_input('url to scan: ')
			anonlog(y)
		else:
			os.system('clear')
			print 'invalid option, try again'
	#url = sys.argv[1]
	#print scan(url)

main()