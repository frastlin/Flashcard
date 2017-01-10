from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ivona-speechcloud-sdk-python',
      version='0.1',
      description='Ivona SpeechCloud SDK',
      long_description=readme(),
      url='https://github.com/IvonaSoftware/ivona-speechcloud-sdk-python',
      author='Ivona Cloud Team',
      author_email='ivona-github@amazon.com',
      license='Apache License, Version 2.0',
      packages=['ivonaspeechcloud'],
      install_requires=[
          'requests==2.3.0',
          'six==1.6.1',
      ],
      include_package_data=True,
      zip_safe=False)