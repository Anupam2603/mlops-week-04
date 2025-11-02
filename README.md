## Sequence to execute codes

# Local Setup
- Run `local_setup.sh`

# git and dvc repository setup 
- Run `git_setup.sh`
- Run `dvc_setup.sh`

# Local Development Run
- Run `local_run.sh` 

# Version Controlling
- Run `version_control.sh`

# Folder & File Structure

- `data`:  has the dataset on which the model will be trained.
- `test`: contains test script and test dataset.
- `local_setup.sh`: set up the virtual env in local repository ".week_02" and install the necessary libraries.
- `local_run.sh`:  It will start running the code. Download the dataset, on which the model will be trained. Run a python script to   
                  train a  model, and measure the accuracy score and store the score in a file with "output.txt".
- `train.py`: Python script for training the model.
- `git_setup.sh`: Bash script for setting up the git repository.
- `dvc_setup.sh`: Bash script for setting up the dvc repository.
- `version_control.sh`: Bash script for version control.
- `requirements.txt`: Contains the information of necessary libraries to perform given task.
- `README.md`: Contains the information of project with all the infromation to run the code and folder and file structure..
