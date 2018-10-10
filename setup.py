from setuptools import setup

setup(name='taskly',
      version='0.1',
      description='CLI from Google Tasks',
      url='http://github.com/decaruju/taskly',
      author='decaruju',
      license='MIT',
      packages=['taskly'],
      install_requires=[
          'google-api-python-client',
      ],
      entry_points = {
          'console_scripts': ['taskly=taskly:main'],
      },
      zip_safe=False)