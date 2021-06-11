import os

for i in sorted(os.listdir('.')):
	if i.endswith('.mp4'):
		os.system('ffmpeg -i {} -c:v libx264 -c:a aac {}'.format(i, "out/" + i))