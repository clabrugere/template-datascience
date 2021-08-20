import subprocess
import sys
import re
import os


repo_name_regex = r"^[_\-a-zA-Z0-9]+$"
repo_name = "{{ cookiecutter.repo_name }}"
initiate_repo = "{{ cookiecutter.initiate_repo }}"
create_conda_env_config = "{{ cookiecutter.create_conda_env_config }}"
conda_env_config_file = f"{repo_name}-env.yml"

if not re.match(repo_name_regex, repo_name):
    print(f"ERROR: {repo_name} is not a valid repository name.")
    sys.exit(1)

if create_conda_env_config == "no" and os.path.isfile(conda_env_config_file):
    os.remove(conda_env_config_file)

try:
    if initiate_repo == "yes":
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "*"], check=True)
        subprocess.run(["git", "commit", "-m", "initial commit"], check=True)

except subprocess.CalledProcessError as e:
    print(e.output)
    sys.exit(1)
