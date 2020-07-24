from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
		name="datalinker",
		version="0.0.2",
		author="Satish Chougule",
		author_email="satishrajc@gmail.com",
		description="Data sharing mechanism between the Python files across the process",
		long_description=long_description,
		long_description_content_type="text/markdown",
		url="https://github.com/Satishrajc/datalinker",
		py_modules=["datalinker", "test_1", "test_2"],
		package_dir={"":"src"},
		classifiers=[
				"Programming Language :: Python :: 3",
				"License :: OSI Approved :: MIT License",
				"Operating System :: OS Independent",
				],
		python_requires='>=3.6',
)