import numpy as np
from numpy import *
from struct import *
batch=10
im_size=48
depth=3
quo=batch // 6
rem=batch % 6
psuedo=batch-5*quo
for k in xrange(batch):

	if k % quo ==0 and k//quo != 5 :
		
		fl=np.random.randn(quo,depth,im_size,im_size).astype(np.uint8)
		label=np.random.randn(quo).astype(np.uint8)

		
		fl=fl.flatten()




		final=[]

		fl.tolist()

		for i in xrange(quo):	
			for j in xrange(im_size*im_size*depth):
				if j % (im_size*im_size*depth+1)==0:
					final.append(label[i])				
				final.append(fl[j])

		#for i in xrange((im_size*im_size*depth+1)*10):
		#	final[i]=bytes(255)

		print (final)


		direc='./example%d.bin' %((k+quo)//quo)


		nfile=open(direc,"wb")


		nfile.write(pack('%dB' %(((im_size*im_size*depth+1)*quo)),*final))
	
	elif k // quo ==5 :
		
		
		fl=np.random.randn(psuedo,depth,im_size,im_size).astype(np.uint8)
		label=np.random.randn(psuedo).astype(np.uint8)

		
		fl=fl.flatten()




		final=[]

		fl.tolist()

		for i in xrange(psuedo):	
			for j in xrange(im_size*im_size*depth):
				if j % (im_size*im_size*depth+1)==0:
					final.append(label[i])				
				final.append(fl[j])

		#for i in xrange((im_size*im_size*depth+1)*10):
		#	final[i]=bytes(255)

		print (final)


		direc='./example6.bin' 


		nfile=open(direc,"wb")


		nfile.write(pack('%dB' %(((im_size*im_size*depth+1)*psuedo)),*final))		
		

