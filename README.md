# seabornWrapper
Package to wrap seaborn plotting functions to support simple syntax and flexibility with common parameters


## Helpful tips for creating a package:
-Create all necessary files: 
<br> PackageName (outer directory)
<br> --->LICENSE, setup.py
<br> --->PackageName (inner directory)
<br> -------->__init__.py
<br> -------->functions.py
<br> -------->moreFunctions.py
<br> -------->evenMoreFunctions.py
    
## Install your package locally
#### run in the terminal from your package directory with the setup.py file: pip install . 

## Import your package and ensure that it works as desired
#### you can run this in python: from PackageName import functions as fns
#### you can also run fns.function_that_is_in_the_functions_file()

## Build your package to create a dist directory that contains files needed for others to pip install your package
#### pip install build
#### python -m build


## Upload your project to: https://test.pypi.org/, this is the testing page for PyPi, which stores the necessary code for others to simply "pip install yourPackage"
#### pip install twine
#### python -m twine upload --repository testpypi dist/*

## pip install your package from the testing site, remember to first run pip uninstall yourPackage
#### pip install -i https://test.pypi.org/simple/ seabornWrapper


## pip install your package and test it out, if it is good to poductionalize, upload your project to: https://pypi.org/
#### python -m twine upload --repository pypi dist/*

#### use --skip-existing after pypi to only install new version files from the dist folder. if you make any changes, you need to change the version number befroe uploading.

## From anywhere in the world, simply type pip install yourPackage and get access to your useful code 

## Other Helpful Resources:
[TowardsDataScience Post and Video for Package Creation](https://towardsdatascience.com/how-to-package-your-python-code-df5a7739ab2e)
<br> [Tutorial for Creating a Package](https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html)


