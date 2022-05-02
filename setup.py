import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bgu",
    version="0.0.1",
    author="Brett Graves",
    author_email="alienbrett648@gmail.com",
    description="Personal utilities",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alienbrett/bgu",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
