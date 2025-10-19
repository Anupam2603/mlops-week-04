#! bin/bash
#Setting up the dvc repository

dvc init

#Setting up the remote storage
dvc remote add -d remote gs://mlops-week-04-graded-assignment