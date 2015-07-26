from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name="pad4pi",
	version="1.0.0",
	description="Interrupt-based matrix keypad library for Raspberry Pi",
	long_description=readme(),
	url="https://github.com/brettmclean/pad4pi",
	author="Brett McLean",
	author_email="brettrmclean@gmail.com",
	license="LGPLv3",
	packages=["pad4pi"],
	install_requires=[
		"RPi.GPIO"
	]
	)
