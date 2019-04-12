from __future__ import division
import os
import numpy as np
import csv
from scipy import interp
from sklearn.metrics import auc
import matplotlib.pyplot as plt


def plot_roc_curve(fpr_LAP, tpr_LAP, AUC_LAP, fpr_NN, tpr_NN, AUC_NN, out_fname):
   	plt.figure()
   	lw = 1
   	plt.plot(fpr_LAP, tpr_LAP, color='y', lw=lw, label='ROC curve (area = %0.2f)' %AUC_LAP)
	plt.plot(fpr_NN, tpr_NN, color='g', lw=lw, label='ROC curve (area = %0.2f)' %AUC_NN)
	plt.plot([0, 1], [0, 1], color='r', lw=lw, linestyle='--')
	plt.xlim([0.0, 1.0])
 	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
  	plt.title('ROC curve %s' %out_fname)
   	plt.legend(loc="lower right")
   	plt.savefig(out_fname)
	#plt.show()


if __name__ == '__main__':

	csv_files = os.listdir('csv_all')
	
	fpr_LAP=dict()
	tpr_LAP=dict()
	AUC_LAP = dict()
    
	fpr_NN=dict()
	tpr_NN=dict()
	AUC_NN = dict()

	for i, ff in enumerate(csv_files):

		csv_file = 'csv_all/%s' %ff

		with open(csv_file, 'r') as readFile:
			reader = csv.reader(readFile)
			lines = list(reader)

		fpr_LAP[i] = lines[0]
		tpr_LAP[i] = lines[1]
		AUC_LAP[i] = lines[2]
		fpr_NN[i] = lines[3]
		tpr_NN[i] = lines[4]
		AUC_NN[i] = lines[5]

	#LAP
	all_fpr_LAP = np.unique(np.concatenate([fpr_LAP[i] for i in range(len(csv_files))]))

	# Then interpolate all ROC curves at this points
	mean_tpr_LAP = np.zeros(len(all_fpr_LAP), dtype='S8')

	for i in range(len(csv_files)):
		mean_tpr_LAP += interp(all_fpr_LAP, fpr_LAP[i], tpr_LAP[i])

	# Finally average it and compute AUC
	mean_tpr_LAP /= len(csv_files)

	fpr_LAP["macro"] = all_fpr_LAP
	tpr_LAP["macro"] = mean_tpr_LAP
	AUC_LAP["macro"] = auc(fpr_LAP["macro"], tpr_LAP["macro"])

	#NN
	all_fpr_NN = np.unique(np.concatenate([fpr_NN[i] for i in range(len(csv_files))]))

	# Then interpolate all ROC curves at this points
	mean_tpr_NN = np.zeros_like(all_fpr_NN)

	for i in range(len(csv_files)):
		mean_tpr_NN += interp(all_fpr_NN, fpr_NN[i], tpr_NN[i])

	# Finally average it and compute AUC
	mean_tpr_NN /= len(csv_files)

	fpr_NN["macro"] = all_fpr_NN
	tpr_NN["macro"] = mean_tpr_NN
	AUC_NN["macro"] = auc(fpr_NN["macro"], tpr_NN["macro"])
	#plotting(fpr_NN, tpr_NN, roc_auc_NN) 
	#print roc_auc_LAP["macro"]
	
	plot_roc_curve(fpr_LAP["macro"], tpr_LAP["macro"], AUC_LAP, fpr_NN["macro"], tpr_NN["macro"], AUC_NN, 'test.png')
