# Create a virtual environment (project is the name of the venv that im gonna give)

conda create -n project python=3.8 -y
conda activate project

# install the requirements

pip install -r requirements.txt

# git commands

git init
git add .
git commit -m "small description"
git push origin main

# dvc commands

After each stage add necessary things to dvc.yaml and : dvc init , dvc repro , dvc dag

# commands to run python scripts from command line (run stage01.py file)

python stage01.py

# commands to check the python files from command line

python
--Now import necessary file and execute , for ex
from src.utils.allutils import \*
read_yaml('config/config.yaml')

# Integration of MLFLOW
