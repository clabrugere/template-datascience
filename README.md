# Template datascience

A simple python project template for datascience using cookiecutter. It provides a standard structure that can be adapted depending on the specific needs of the project.

## Usage

Navigate to a local directory where you want to store the project repository and execute the command:

```
cookiecutter https://github.com/clabrugere/template-datascience
```

Follow the few prompts to fill the basic information about your project:
- ```project_name``` is the name of your project, it can contain spaces, numbers, underscores and hyphens only.
- ```description``` type a short description of the project that will be put in the readme file.
- ```repo_name``` is the project name in lowercase with spaces replaced by "-" by default, but you can type another name.
- ```initiate_repo``` to whether or not initiate the git repository.
- ```author_name``` to be put in the licence file. It is you or the organisation you represent.
- ```open_source_license``` type of licence. Currently three are supported: MIT, BSD-3-clause and No licence.

Note that the repository name is checked at the end to make sure it contains only numbers, underscores or hyphens. If the check fails, the project will not be created.

### Project structure

Running the command will create the project structure in the current working directory:
- ```data/``` contains all the data files used or generated by the project:
	- ```data/raw/``` the original data dumps.
	- ```data/iterim/``` the itermediate datasets that are expensive to generate.
	- ```data/processed/``` the final canonical datasets for modeling.
	- ```data/results/``` results generated by the models.
- ```notebooks/``` contains all the development and presentation notebooks. They can be named using a standard convention such as ```<step #>-<step name>-<task name>.ipynb```, for example ```01-EDA-Data_quality.ipynb```.
- ```reports/``` contains the generated reports and figures.
- ```src/``` contains all the core code (default structure, you might want to adapt it depending on your project):
	- ```src/data``` code to fetch or generate the raw and interim datasets.
	- ```src/features``` code to generate the final canonical datasets.
	- ```src/models``` code implementing the models.

LICENCE, README.md and .gitignore files will be automatically created.

### Manage your environments

Once you have the basic project's strucure, it is recommend to create a dedicated python environment for your project. If you are using conda to manage environments, create a new environment (where {{repo_name}} is the name of the repository oyu just created):

```
conda env create -f {{repo_name}}-env.yml
```
activate the new environment:
```
conda activate {{repo_name}}
```
create a new python kernel for this environment:
```
python -m ipykernel install --user --name {{repo_name}}
```
return the base environment where jupyter is installed:
```
conda deactivate
```

It will create a minimalist conda environment for datascience that you can further extend depending on your project's needs, that will be visible from jupyter when you want to create new notebooks. It contains the following packages:
  - python 3.8
  - ipykernel
  - numpy
  - pandas
  - scikit-learn 
  - plotly

## Requirements

- cookiecutter

## License

[MIT](LICENSE)