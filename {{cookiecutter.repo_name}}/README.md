# {{ cookiecutter.package_name }}

## Introduction

{{ cookiecutter.project_description }}

## Installation

bla bla

## Usage

bla bla

## Contribute

bla bla

## Citation

When citing this repository on your publications please use the following **bibtex** citation:

```
@misc{
    {{ cookiecutter.package_name }},
    author = {{{ cookiecutter.author }}},
    title = {{{ cookiecutter.package_name }} - {{ cookiecutter.project_description }}},
    year = {{% now 'local', '%Y' %}},
    publisher = {GitHub},
    journal = {GitHub Repository},
    howpublished = {\url{https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.package_name }}}},
}
```

### This repository has been generated using [pypackage-cookie](https://github.com/alvarobartt/pypackage-cookie) made with love by @alvarobartt
