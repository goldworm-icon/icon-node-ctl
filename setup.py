import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iconnodectl",
    version="0.0.1",
    author="goldworm",
    author_email="goldworm@iconloop.com",
    description="ICON Node controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goldworm-icon/icon-node-ctl",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'iconnodectl=iconnodectl.main:main'
        ]
    }
)
