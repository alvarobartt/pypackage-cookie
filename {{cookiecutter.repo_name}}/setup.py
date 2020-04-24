# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from setuptools import setup, find_packages
import io


def readme():
    with io.open('README.md', encoding='utf-8') as f:
        return f.read()

def requirements():
    reqs = list()
    with io.open('requirements.txt', encoding='utf-8') as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name='{{ cookiecutter.package_name }}',
    version='{{ cookiecutter.package_version }}',
    packages=find_packages(),
    url="https://www.github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}",
    download_url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.package_version }}.tar.gz',
    license='{{ cookiecutter.license }}',
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.author_email }}',
    description='{{ cookiecutter.package_name }} — {{ cookiecutter.short_description }}',
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=requirements(),
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
    python_requires='>=3',
    project_urls={
        'Bug Reports': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/issues',
        'Source': 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
        'Documentation': 'https://{{ cookiecutter.package_name }}.readthedocs.io/'
    },
)