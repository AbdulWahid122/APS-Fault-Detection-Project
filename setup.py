from setuptools import find_packages,setup

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e."

def get_requirements()->list[str]:

    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        requirement_list=requirements_file.readlines()
        requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
        
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
        
#for requirement_name in requirement_list, That means requirement_name is just a variable name you are assigning to each item of the list one by one.

setup(
    name="aps_fault_detection",
    version="0.0.1",
    author="Wahid",
    author_email="xyz@gmail.com",
    packages=find_packages(),  
    install_requires=get_requirements(),
)   

#find packages will check that which file is containing python packages and how it is identify it is because of the presence of __init__.py file
# which we will create inside the folder having source code, here it is sensor folder which contains source code.
#each folder where __init__.py file is present will be considered as packages.

#install_requires task is to provide libraries names that is required for the project.

#we have to replace \n from each line in making def get_requirements(), because there is a \n present in requirements.txt as a new line but it is not visible.

#we want to read requirements.txt as return string that is required libraries in the form of a list.

#we are replacing \n with nothing because it is not a part of a list.

# -e. is required if you want to store source code as a library.