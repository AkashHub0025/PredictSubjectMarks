from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function return list of required plugins
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","" ) for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
name='PredictSubjectScore',
version='0.0.1',
author='akash',
author_email='akashthapa0025@gmail.com',
packages=find_packages(),
install_require=get_requirements('requirements.txt')
)