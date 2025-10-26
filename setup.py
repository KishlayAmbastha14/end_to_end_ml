from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
  """this functions will return the list of requiremnts"""
  requirements=[]
  with open(file_path) as f:
    requirements = f.readlines()

    requirements = [req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  
  return requirements


setup(
  name="MLproject",
  version='0.0.1',
  author="Kishlay",
  author_email="kishlaykumar078@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)
