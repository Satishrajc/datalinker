from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
		name="datalinker",
		version="2.0.0",
		author="Satish Chougule",
		author_email="satishrajc@gmail.com",
		description="""Variable sharing mechanism between Python "
					fies and across the project/process""",
		long_description=long_description,
		long_description_content_type="text/markdown",
		url="https://github.com/Satishrajc/datalinker",
		py_modules=["datalinker", "test_1", "test_2"],
		package_dir={"":"src"},
		install_requires=[],
		setup_requires=[],
		classifiers=[
				"Programming Language :: Python :: 3",
				"License :: OSI Approved :: MIT License",
				"Operating System :: OS Independent",
				],
		python_requires='>=3.6',
)