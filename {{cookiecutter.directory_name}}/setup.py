from setuptools import setup

setup(name='{{ cookiecutter.repo_name }}',
      version='cookiecutter.version',
      packages=['{{ cookiecutter.repo_name }}]',
      entry_points={
          'console_scripts': [
              '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.__main__:{{ cookiecutter.function_name}}'
          ]
      },
      )
