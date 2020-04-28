# {{ cookiecutter.package_name }}

## Introduction

{{ cookiecutter.project_description }}

## Installation

In order to get this package working you will need to **install it via pip** (with a Python3.5 version or higher) on the terminal by typing:

``$ pip install {{ cookiecutter.package_name }}``

Additionally, **if you want to use the latest version instead of the stable one**, you can just use the following command:

``$ pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git@developer``

**The developer branch ensures the user that the most updated version will always be the working and fully operative** so as not to wait until the stable release on the master branch comes out (which eventually may take some time depending on the amount of issues to solve).

## Documentation

You can find the **complete developer documentation** at: https://{{ cookiecutter.package_name }}.readthedocs.io/, hosted on [Read the Docs](https://readthedocs.org/) and generated using [sphinx](https://www.sphinx-doc.org/en/master/) with the theme [sphinx_rtd_theme](https://github.com/readthedocs/sphinx_rtd_theme) which is the standard Read the Docs theme for sphinx.

## Usage

So as to use this Python package, a sample piece of code is presented below:

```python
import {{ cookiecutter.package_name }}

{{ cookiecutter.package_name }}.sample_function()
```

So on, the previous piece of code outputs the following line:

```{r, engine='python', count_lines}
"This is a sample function"
```

## Contribute

As this is an open source project it is **open to contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas**. There is an open tab of [issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/issues) where anyone can open new issues if needed or navigate through them in order to solve them or contribute to its solving. Remember that **issues are not threads to describe multiple problems**, this does not mean that issues can't be discussed, but so to keep a structured project management, the same issue should not describe different problems, just the main one and some nested/related errors that may be found.

## Citation

When citing this repository on your publications please use the following **BibTeX** citation:

```
@misc{
    {{ cookiecutter.package_name }},
    author = { {{ cookiecutter.author }} },
    title = { {{ cookiecutter.package_name }} - {{ cookiecutter.project_description }} },
    year = { {% now 'local', '%Y' %} },
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}}}
}
```

### This repository has been generated using [pypackage-cookie](https://github.com/alvarobartt/pypackage-cookie) made with love by @alvarobartt
