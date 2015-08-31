from lxml import etree
import os
import urllib
import urllib2
import os
import re


#Note, If you are on a windows system, go through and uncomment the lines that say os.chdir("Python27/Scripts")
#This plugin also depends on the installation of youtube-dl


def youtube(vidsearch):
    query_string = urllib.urlencode({"search_query" : vidsearch})  
    html_content = urllib2.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode('utf-8'))
    vidurl1 = ("http://www.youtube.com/watch?v=" + search_results[0])
    vidurl2 = ("http://www.youtube.com/watch?v=" + search_results[2])
    vidurl3 = ("http://www.youtube.com/watch?v=" + search_results[3])
    vidurl4 = ("http://www.youtube.com/watch?v=" + search_results[4])
    vidurl5 = ("http://www.youtube.com/watch?v=" + search_results[5])
    youtube = etree.HTML(urllib.urlopen(vidurl1).read()) #enter your youtube url here
    video_title1 = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    print('1.'+''.join(video_title1))
    youtube = etree.HTML(urllib.urlopen(vidurl2).read()) #enter your youtube url here
    video_title2 = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    print('2.'+''.join(video_title2))

    youtube = etree.HTML(urllib.urlopen(vidurl3).read()) #enter your youtube url here
    video_title3 = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    print('3.'+''.join(video_title3))

    youtube = etree.HTML(urllib.urlopen(vidurl4).read()) #enter your youtube url here
    video_title4 = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    print('4.'+''.join(video_title4))

    youtube = etree.HTML(urllib.urlopen(vidurl5).read()) #enter your youtube url here
    video_title5 = youtube.xpath("//span[@id='eow-title']/@title") #get xpath using firepath firefox addon
    print('5.'+''.join(video_title5))

    whichvid = raw_input("Which video would you like to perform an action on? (1,2, etc.)")
    if '1' in whichvid:
        vidaction = raw_input("Would you like to download this video? (y/n)")
        if vidaction == 'y': 
            #os.chdir('/Python27/Scripts')
            os.system("youtube-dl " + vidurl1)


    elif '2' in whichvid:
        vidaction = raw_input("Would you like to download this video? (y/n)")
        if vidaction == 'y': 
            #os.chdir('/Python27/Scripts')
            os.system("youtube-dl " + vidurl2)

    elif '3' in whichvid:
        vidaction = raw_input("Would you like to download this video? (y/n)")
        if vidaction == 'y': 
           # os.chdir('/Python27/Scripts')
            os.system("youtube-dl " + vidurl3)

    elif '4' in whichvid:
        vidaction = raw_input("Would you like to download this video? (y/n)")
        if vidaction == "y": 
            #os.chdir('/Python27/Scripts')
            os.system("youtube-dl " + vidurl4)

    elif '5' in whichvid:
        vidaction = raw_input("Would you like to download this video? (y/n)")
        if vidaction == 'y': 
            #os.chdir('/Python27/Scripts')
            os.system("youtube-dl " + vidurl5)
q = raw_input('>')
youtube(q)
