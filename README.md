# R CookieCutter

CBiB's template for R projects.


## Installation
```sh
pip install cookiecutter
```

Or with conda: 
```sh
conda install -c conda-forge cookiecutter
```
>*Note:* If you are using conda, I advise you to install cookiecutter in your base environment.
##  Usage
First, create a new github repo, do not check `Initialize this repository with a README`.

Then we will call cookiecutter in order to download the template:
```sh
cookiecutter https://github.com/EdgarLefevre/cbib_python_template.git
```

Next, the software will ask you some questions:
- *project_name* : the name of the project
- *main_file* : the name of the main file
- *src_dir* : name of the source directory
- *results_dir* : name of the results directory
- *github_username* : your github username
- *author* : the name of the author
- *mail* : the email of the author
- *description* : a description of the project
- *year* : the year of the project
- *tests* : if you want to generate tests folder
- *doc* : if you want to generate documentation folder
- *rmarkdown* : if you want to use rmarkdown
- *project_slug* : the slug of the project (type enter, in the next versions you will not see this prompt)
- *example* : if you want to generate an example for documentation and tests.



Once everything is created, run git commands:
```sh
cd <project_name>
git init
git remote add origin git@github.com:YOURNAME/YOURREPO.git
git add *
git commit -am "First commit"
git push -u origin master
```
## Architecture

![Folder structure](imgs/folder_structure.png)