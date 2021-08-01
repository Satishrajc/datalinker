from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="datalinker",
    version="2.1.1",
    author="Satish Chougule",
    author_email="satishrajc@gmail.com",
    packages=find_packages(include=['datalinker']),
    description="""Variable sharing mechanism between Python
                fies/folders and across the project/process""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Satishrajc/datalinker",
    keywords=['DATA SHARING', 'VARIABLE SHARING', 'VARIABLE SHARING', 'SHARING' 'SHARABLE'],
    py_modules=["datalinker"],
    package_dir={"": "src"},
    install_requires=['deprecation', ],
    setup_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
