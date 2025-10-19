#! bin/bash

echo "Executing the code for perforing Week_04's task."

if [ -d ".Week_04" ]
then
	echo ""
else
	echo "No virtual environment. Please run local_setup.sh"
	exit 1
fi

gsutil cp "gs://mlops-week-04-graded-assignment/${1}/data.csv" ./data

#Executing the code.
python train.py

