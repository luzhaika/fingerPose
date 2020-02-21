import os 
import numpy as np 

dir_name = '/home/fingerpose/Videos/output/' 
dir_name_write = '/home/fingerpose/nsu.sharapov.uz/edited_data_from_video' 
test = os.listdir(dir_name) 

for item in test: 
	with open(dir_name + '/' + item) as fo: 
		f = fo.read() 

	newf=(f.split('"hand_right_keypoints_2d":[')[1]) 
	newf=(newf.rsplit('],"pose')[0]) 

	newf=(newf.split(',')) 
	newf=np.array(newf,float) 
	newf=np.reshape(newf, (21, 3)) 

#fingers=np.zeros(5,2) 
	fingers=np.vstack((newf[4,0:2],newf[8,0:2],newf[12,0:2],newf[16,0:2],newf[20,0:2])) 
	print(fingers) 
	fw = open((dir_name_write + '/' + item), 'w') 
	np.savetxt((dir_name_write + '/' + item), fingers) 

	fw.close()
