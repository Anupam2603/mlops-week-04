#! bin/bash

echo "Controlling the version of data and model"


# Adding data and model to version control file
dvc add data ./models/model.joblib

#Adding all the changes to git
git add .

#Comming the changes
git commit -m "Trained with version $1 dataset"

#Tagging the commit
git tag a "$1" -m "Trained with version $1 dataset"

#Pushing to a remote storage (Data and Model)
dvc push

#Pushing the changes to remote direcotry on Github
git push -u origin ${2}
