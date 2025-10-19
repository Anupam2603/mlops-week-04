#! bin/bash



echo "Creating the virtual enviroment and installing all dependencies."

#Creating virtual environmnet.
if [ -d ".Week_04" ]
then
	echo ".Week_04 library exists.Activating virtual environment and intalling dependencies using pip"
else
	echo "Creating .Week_04 directory"
	python3 -m venv .Week_04
fi 

# Activate virtual environment
source .Week_04/bin/activate

# upgrade the pip
pip install --upgrade pip

# Installing dependencies
pip install -r requirements.txt