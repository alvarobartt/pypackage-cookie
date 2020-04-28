# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

import pytest

import {{ cookiecutter.package_name }}


def sample_tests():
    params = [
        {
            'value': True
        },
        {
            'value': False
        }
    ]

    for param in params:
        assert {{ cookiecutter.package_name }}.sample_function(value=param['value'])


if __name__ == "__main__":
    sample_tests()
