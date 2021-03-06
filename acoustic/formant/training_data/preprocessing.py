import pandas as pd
import numpy as np
from sklearn import preprocessing

train_set_ID_list = [303, 304, 305, 310, 312, 313, 315, 316, 317, 318, 319, 320, 321, 322, 324, 325, 326, 327, 328, 330, 333, 336, 338, 339, 340, 341, 343, 344, 345, 347, 348, 350, 351, 352, 353, 355, 356, 357, 358, 360, 362, 363, 364, 366, 368, 369, 370, 371, 372, 374, 375, 376, 379, 380, 383, 385, 386, 391, 392, 393, 397, 400, 401, 402, 409, 412, 414, 415, 416, 419, 423, 425, 426, 427, 428, 429, 430, 433, 434, 437, 441, 443, 444, 445, 446, 447, 448, 449, 454, 455, 456, 457, 459, 463, 464, 468, 471, 473, 474, 475, 478, 479, 485, 486, 487, 488, 491]
incomplete_data_ID_list = [342, 394, 398, 460, 373, 444, 451, 458, 480, 402]

for ID in incomplete_data_ID_list:
	if(ID in train_set_ID_list):
		train_set_ID_list.remove(ID)

max_frames = -1
min_frames = 1000000000

for ID in train_set_ID_list:
	
	print(ID, end='\r')
	
	data = pd.read_csv('/data/chercheurs/qureshi191/raw_data/'+str(ID)+'_P/'+str(ID)+'_FORMANT.csv', header=None)

	data = data.values
	a = np.arange(data.shape[0])

	data = preprocessing.scale(data)
	data = data[a%10 == 0]

	if(max_frames < data.shape[0]):
		max_frames = data.shape[0]

	if(min_frames > data.shape[0]):
		min_frames = data.shape[0]

	np.save('/data/chercheurs/qureshi191/preprocessed_data/training_data/acoustic/formant/individual/'+str(ID)+'_formant.npy', data)

print(max_frames, min_frames)