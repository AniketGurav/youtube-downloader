from lxml import etree
import os
import urllib
import urllib2
import os
import re
import sys
def download(n):
    if 5 >= n >= 1:
        if 'win' in sys.platform:
            os.chdir('/Python27/Scripts')
        os.system("youtube-dl {0}".format("http://www.youtube.com/watch?v={0}".format(search_results[n - 1])))
def url_gen(vidurl):
	youtube = etree.HTML(urllib.urlopen(vidurl).read())
	return youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon

def youtube(vidsearch):
	query_string = urllib.urlencode({"search_query" : vidsearch})
	html_content = urllib2.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode('utf-8'))
	for i in range(0,4):
		print ("{0}.".format(str(i+1)+''.join(url_gen(search_results("http://www.youtube.com/watch?v={0}".format(search_results[i]))))))
	whichvid = raw_input("Which video would you like to perform an action on? (1,2, etc.)")
	try:
	    n = int(whichvid)
        download(n)
    except TypeError:
        print "Must be valid number between 1 and 5"
        youtube(vidsearch)


if __name__ == "__main__":
	youtube(raw_input('>'))