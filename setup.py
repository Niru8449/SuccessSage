# Responsible for creating the machine learning application as a package
from setuptools import find_packages, setup
from typing import List
# find_packages automatically finds out all the packages that are available  in the directory


def get_requirements(file_path:str) -> List : 
    '''
    the function will return the list of requirements
    necessary for the implementation of the package
    '''

    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements : 
            requirements.remove(HYPEN_E_DOT)

    return requirements

'''
-e . is written in requirements.txt  so that : 
If we want the setup.py to run whenever we are
trying to install requirements from requirements.py
'''

setup (
    name = 'datascienceproject',
    version = '0.0.1',
    author = "Nirupama",
    author_email = 'nirupamasinghab12@gmail.com',
    packages = find_packages(),
    # install_requires = ["numpy", "pandas", "seaborn"]
    install_requires = get_requirements('requirements.txt')
)

# Whenever setup.py .... find_packages is running, it will search for how many folders have __init__.py file....
# Then it will consider src as a package itself and then it will try to build it

