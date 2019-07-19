#!/usr/bin/env python

from __future__ import division
import os
import numpy as np
import csv
from scipy import interp
from sklearn.metrics import auc
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import json


def plot_roc_curve(fpr_LAP, tpr_LAP, AUC_LAP, fpr_NN, tpr_NN, AUC_NN, tract_name):
   	plt.figure()
   	lw = 1
   	plt.plot(fpr_LAP, tpr_LAP, color='y', lw=lw, label='auc_LAP = %0.2f' %AUC_LAP)
	plt.plot(fpr_NN, tpr_NN, color='g', lw=lw, label='auc_NN_DR_MAM = %0.2f' %AUC_NN)
	plt.plot([0, 1], [0, 1], color='r', lw=lw, linestyle='--')
	plt.xlim([0.0, 1.0])
 	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
  	plt.title('Receiver Operating Characteristic %s' %tract_name)
   	plt.legend(loc="lower right", fontsize='medium')
   	plt.savefig('images/roc-auc_curve_%s.png' %tract_name)
    plt.savefig('roc-auc_curve_%s.pdf' %tract_name)
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
		#data = read_csv(csv_file)

		M = len(lines[0])
		N = len(lines[3])

		fpr_LAP[i] = np.array([np.float(lines[0][j]) for j in range(M)])
		tpr_LAP[i] = np.array([np.float(lines[1][j]) for j in range(M)])
		AUC_LAP[i] = np.float(lines[2][0])
		fpr_NN[i] = np.array([np.float(lines[3][j]) for j in range(N)])
		tpr_NN[i] = np.array([np.float(lines[4][j]) for j in range(N)])
		AUC_NN[i] = np.float(lines[5][0])

	#LAP
	all_fpr_LAP = np.unique(np.concatenate([fpr_LAP[i] for i in range(len(csv_files))]))

	# Then interpolate all ROC curves at this points
	mean_tpr_LAP = np.zeros_like(all_fpr_LAP)

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
	
	with open('config.json') as f:
	    data = json.load(f)
	tract_name = data["_inputs"][2]["tags"][0].encode("utf-8")
	
	plot_roc_curve(fpr_LAP["macro"], tpr_LAP["macro"], AUC_LAP["macro"], fpr_NN["macro"], tpr_NN["macro"], AUC_NN["macro"], tract_name)
