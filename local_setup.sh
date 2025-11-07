#! bin/bash



echo "Creating the virtual enviroment and installing all dependencies."

#Creating virtual environmnet.
if [ -d ".mlops" ]
then
	echo ".mlops library exists.Activating virtual environment and intalling dependencies using pip"
else
	echo "Creating .mlops directory"
	python3 -m venv .mlops
fi 

# Activate virtual environment
source .mlops/bin/activate

# upgrade the pip
pip install --upgrade pip

# Installing dependencies
pip install -r requirements.txt