# coding=utf-8

import setuptools

setuptools.setup(
    name="rabbitmq2psqlwrite",
    version="1.0.2",
    author="Ramazan ÇETİN",
    author_email="ramazan.cetin0640@gmail.com",
    description="RabbitMQ listen and read data change database",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    url="https://github.com/mantis-software-company/rabbitmq2psqlwrite",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Testing",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['aiopg', 'aio_pika'],
    python_requires=">3.6.*, <4",
    packages=['rabbitmq2psqlwrite'],
    scripts=['bin/rabbitmq2psqlwrite']
)
