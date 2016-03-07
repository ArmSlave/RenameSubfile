import os
import re

video_ext = ['.mkv','.avi','.mp4']
sub_ext = ['.ass','.srt']

dir = os.getcwd()
filelist = os.listdir(dir)
for video_file in filelist:
	if video_file[-4:len(video_file)] in video_ext:
		video_name = video_file
		pos = re.search('s\d\de\d\d|ep\d\d', video_name, re.I).span()
		ep = video_name[pos[0]:pos[1]]
		for sub_file in filelist:
			ext = sub_file[-4:len(sub_file)]
			if ext in sub_ext:
				if (sub_file.find(ep)+sub_file.find(ep.swapcase())) > -1:
					print sub_file+'->'+video_name[0:-4]+ext
					os.rename(sub_file,video_name[0:-4]+ext)
