from setuptools import find_packages,setup
from typing import List 


def get_req(file_path:str) -> List[str] :
    "This funtion will return the list of requirements"
    
    requirements = []
    with open(file_path, "r") as file :
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]


        if "-e ." in requirements:
            requirements.remove("-e .")
    
    return requirements

setup(
name = "MLProject",
version= "0.0.1",
author="anukul03",
author_email="anukul03@gmail.com",
packages=find_packages(),
requires=get_req('requirements.txt')

)






