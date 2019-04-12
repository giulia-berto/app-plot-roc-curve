#!/bin/bash
#PBS -k o
#PBS -l nodes=1:ppn=16,walltime=00:05:00

echo "setting miniconda path..."
unset PYTHONPATH
export PATH=/N/u/gberto/Karst/miniconda2/bin:$PATH

measures=`jq -r '.measures' config.json`

arr_meas=()
arr_meas+=(${measures})
num_ex=$((${#arr_meas[@]} - 2))

mkdir csv_all;
for i in `seq 1 $num_ex`; 
do 
	measure=${arr_meas[i]//[,\"]}
	id_meas=$(jq -r "._inputs[$i].meta.subject" config.json | tr -d "_")
	cp ${arr_meas[i]//[,\"]} csv_all/${id_mov}_output_FiberStats.csv;
done

echo "Computing ROC curves"
mkdir images;
python plot_roc.py

if [ -z "$(ls -A -- "images")" ]; then    
	echo "Computation failed."
	exit 1
else    
	echo "Computation done."
fi
