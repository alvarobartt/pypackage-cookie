<h1 align="center">Python Package Cookie</div>
</br>
<div align="center">
  <img src="https://i.pinimg.com/originals/ac/a4/95/aca4951fa1d8d6da682821bc467ea6ce.png" alt="cookie-monster" height="300px" hspace="20">
</div>

## Features

This cookie provides the following features:

* A complete Python package skeleton including all the main standards used while creating and uploading a proper Python package.
* [Pytest](https://docs.pytest.org/en/latest/) for testing Python package functions.
* [Travis-CI](https://travis-ci.org/) continuous integration so as to test that the package works properly after each commit.
* Integration with [Codecov](https://azure.microsoft.com/es-es/services/devops/pipelines/) so as to get to know which source code lines are hitted and which of them are missed.
* Additionally, other CI tools such as [Azure Pipelines](https://azure.microsoft.com/es-es/services/devops/pipelines/) or [Github Actions](https://github.com/features/actions).
* [sphinx](https://www.sphinx-doc.org/en/master/) automatic developer documentation generated from function docstrings, reStructuredText & Markdown files, which can lated be hosted on [ReadTheDocs](https://readthedocs.org/).
* and much more that will be progressively included...

## Installation

Firstly, you will need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter) using pip from a Python3.5 version or higher since **this cookie recipe just works on Python3.5+**; use the following command:

``pip install cookiecutter``

So as **to create your own cookie from this recipe you will need to clone this repository** using the following command:

``git clone https://github.com/alvarobartt/pypackage-cookie``

Once it is properly cloned, from the working directory, you will need to **pass the cloned cookie as an argument to the cookiecutter entry point** as it follows:

``cookiecutter /path/to/pypackage-cookie``

This command will launch the **cookiecutter prompt into your terminal**, which will ask you some configuration options as specified in the cookie recipe for you to select the most suitable ones according to your needs.

**So as to bake this cookie, the cookiecutter prompt will ask you to select between the following ingredients** (configuration) in case you want to name your cookie (project), for example, lets suppose that your project will be named `awesome_cookie` its configuration will be:

```
author [Alvaro Bartolome del Canto]: Cookie Monster
email [alvarobartt@example.com]: cookiemonster@sesamestreet.com
github_username [alvarobartt]: cookie-monster
project_name [Python Package]: awesome-cookie
project_description [This project is a sample Python Package]: This is an awesome cookie!
repo_name [awesome_cookie]: 
package_name [awesome_cookie]: 
pypi_username [cookie-monster]: 
version [1]: 
Select license:
1 - MIT License
2 - BSD License
3 - ISC License
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - WTFPL License
7 - None
Choose from 1, 2, 3, 4, 5, 6, 7 [1]: 1
```

When this process is finished, automatically a directory named as specified in `repo_name` will be created containing the following files and directories:

``awesome_cookie/  docs/  LICENSE  MANIFEST.in  README.md  requirements.txt  setup.cfg  setup.py  tests/``

**Congratulations! You already baked your own pypackage-cookie!**

## Usage

**Once the cookie is completely baked, you can take it off the oven!** So on, from the `repo_name` previously created directory, you can install it using pip by typing: ``pip install .`` and modify it as you need to in order to fit your needs.

**Now you are completely free to eat your cookie!**

### Share your cookie

**If you baked a nice cookie from the provided recipe, it will be a shame if you did not share it with other people...** Since it is a Python package, in order to upload it to PyPI so that every user can download and install it, you will need to:

* Go to your Github repo URL and access the tab called `Releases`.
* Then, click the button `Draft a new release` so as to **create a new project release version**. (Note that the version number of the release should be the same as specified on the `version` attribute, which will need to be updated before drafting every new release at https://github.com/alvarobartt/pypackage-cookie/blob/master/%7B%7Bcookiecutter.repo_name%7D%7D/setup.py).
* Once the release is created, you need to be placed on the project's directory root, where the `setup.py` file is.
* Before uploading it, you will need to create a new ZIP file from source code, which will be done using: ``python setup.py sdist``. The previous command will create the new ZIP file under the `dist/` directory.
* In order to **upload it to PyPI**, you will need to install `twine` which is an utility for publishing Python packages using the command: ``pip install twine``
* Once installed, you need to cd into the recently generated `dist/` directory.
* Finally, you will just need to upload it to PyPI using the following command: ``twine upload /path/to/package-version.zip`` and access with your PyPI credentials.

**Thanks for sharing your cookie!**

### Test the oven

**A really important step when baking cookies is to test that the oven works properly so as to bake better cookies!** So on, referring to the CI tools, you will need to set them up so as to work as expected when commiting to the repository so as to ensure that your package is working as expected.

* __Travis-CI__: sign in with Github, then grant Travis access to your public repositories, select the current repository and run the created build so as to test that everything works as expeceted.
* __Azure Pipelines__: sign in with Github and grant access to your public repositories, just like when setting up Travis-CI, create a new organization and then a new project inside (you can name them both as you prefer) and then create a new pipeline from Github YAML where you just need to select the `azure-pipelines.yml` file which was created while baking the cookie.
* __Github Actions__: from your Github project website, just go to the tab `Actions` and setup the workflow that is created under `.github`, where you just need to select it and run it.

**Always make sure that the oven is clean and fully operative...**

### Generate the cookie recipe

**So as not to forget about how you made the cookie, you should generate its recipe.** As already mentioned, the HTML docs using ReadTheDocs template are included in the project, so that the user can easily generate the developer documenation.

This means that once the package fits the needs of the user, the documentation needs to be generated so as to keep a proper tracking and structure of the project, since it will ease a lot not just the user's tasks but any other open source user while trying to understand your project in order to use it or contribute to it.

To generate the latest version of the docs, after writting and formatting all the required docstrings properly, you will just need to cd into the `docs/` directory and execute the following command:

``make clean & make html``

which will remove the current documenation and generate a new one. Additionally, note that you can make changes on every reStructuredText or Markdown file placed under the `docs/` directory, since as you may see, it is the information that will be shown in the HTML generated documentation.

**When baking cookies recipe is the key, so that any other person can bake it and/or understand its process!**

## Cookie recipe created by...

<table>
  <tr>
    <td align="center"><a href="https://github.com/alvarobartt"><img src="https://avatars3.githubusercontent.com/u/36760800?s=460&v=4" width="100px;" alt=""/><br/><sub><b>Álvaro Bartolomé</b></sub></a><br/><a title="Code">💻</a> <a title="Documentation">📖</a><a title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

## Want more cookies?

You can find a **curated collection of self made cookies** at [cookie-jar](https://github.com/alvarobartt/cookie-jar)

## You don't like this cookie? You don't like the chef/chefs?

If you don't like neither the cookie neither the chef (or chefs), to each his own... here we do not judge you (just a little), here you have a list of some **similar cookie recipes you may like**:

- [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
- [kragniz/cookiecutter-pypackage-minimal](https://github.com/kragniz/cookiecutter-pypackage-minimal)
- [ardydedase/cookiecutter-pypackage](https://github.com/ardydedase/cookiecutter-pypackage)
- [elgertam/cookiecutter-pipenv](https://github.com/elgertam/cookiecutter-pipenv)
- [conda/cookiecutter-conda-python](https://github.com/conda/cookiecutter-conda-python)

## You want to become a chef too?

Maybe after seeing this cookie recipe your inner chef spirit came out and you decided to become a chef, well, we already thought this may happen, so here you have a list of **useful links on your way to become a real chef** (well, not a real one just a programming chef somehow):

- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [Getting to know Cookiecutter!](https://cookiecutter.readthedocs.io/en/1.7.0/tutorial1.html)
- [Additional Tutorials](https://cookiecutter.readthedocs.io/en/latest/tutorials.html)
