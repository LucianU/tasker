from setuptools import setup, find_packages

setup(name='tasker',
      version='0.1',
      packages=find_packages(),
      package_data={'tasker': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'tasker': ['bin/*.pyc']},
)


