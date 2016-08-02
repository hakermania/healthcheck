#!/usr/bin/env python2

import configparser, sys, urllib2, base64, chardet

class bcolors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
	if len(sys.argv) != 2:
		print 'Parse the ini file'
		sys.exit(1)

	config = configparser.ConfigParser()
	config.read(sys.argv[1])

	sectionCounter = 0
	for section in config.sections():
		sectionCounter += 1

		print

		try:
			site = config[section]['site']
			check = config[section]['check']
			print bcolors.HEADER + '--->', str(sectionCounter) + '.', section, '(' + site + ') ->', check + bcolors.ENDC
		except:
			print bcolors.FAIL + 'Malformed section', section + bcolors.ENDC
			continue

		request = urllib2.Request(site)

		if 'username' in config[section] and 'password' in config[section]:
			# authentication is needed
			print bcolors.INFO + 'Using basic auth for', section + bcolors.ENDC
			base64string = base64.encodestring('%s:%s' % (config[section]['username'], config[section]['password'])).replace('\n', '')
			request.add_header('Authorization', 'Basic %s' % base64string)

		try:
			req = urllib2.urlopen(request)
		except urllib2.HTTPError as e:
			print bcolors.FAIL + 'Could not get', site, '(' + str(e) + ')' + bcolors.ENDC
			continue

		content = req.read()

		encoding = req.headers['content-type'].split('charset=')[-1]

		if encoding == 'text/html':
			ucontent = unicode(content, chardet.detect(content)['encoding'])
		else:
			ucontent = unicode(content, encoding)

		print bcolors.OK + 'OK' + bcolors.ENDC if check in ucontent else bcolors.FAIL + 'FAIL' + bcolors.ENDC

if __name__ == '__main__':
	main()