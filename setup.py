import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ML_tools", # Replace with your own username
    version="0.0.7",
    author="Pablo N. Marino",
    author_email="pablo-n-m@hotmail.com",
    description="Tools for managing small Machine Learning projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pablonm3/ML_tools",
    packages=setuptools.find_packages(),
    install_requires=[
        "slackclient==2.9.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)