# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements(filename):
    reqs = list()
    with io.open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='{{ cookiecutter.package_name }}',
    version='{{ cookiecutter.version }}',
    packages=find_packages(),
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    download_url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.version }}.tar.gz',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    description='{{ cookiecutter.package_name }} — {{ cookiecutter.project_description }}',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(filename='requirements.txt'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: {{ cookiecutter.license }}",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"
    ],
    extras_require={
        "docs": requirements(filename='docs/requirements.txt'),
        "tests": requirements(filename='tests/requirements.txt'),
    },
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
        'Source': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
        'Documentation': 'https://{{ cookiecutter.package_name }}.readthedocs.io/'
    },
)