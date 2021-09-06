# coding=utf-8

import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="rabbitmq2psqlwrite",
    version="1.0.0",
    author="Ramazan ÇETİN",
    author_email="ramazan.cetin0640@gmail.com",
    description="RabbitMQ logs to update DB row",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
