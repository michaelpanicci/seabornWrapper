from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Wrapper for seaborn plotting methods with focus on pandas groupby'
LONG_DESCRIPTION = """Wrapper for seaborn plotting methods with focus on pandas groupby, 
specifically adding the ability to create the desired groupby and easily add data labels"""

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="seabornWrapper", 
        version=VERSION,
        author="Micahel Panicci",
        author_email="<mapanicci@gmail.com.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['seaborn','plotting','wrapper'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Data Professionals",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)