from setuptools import setup, find_packages

setup(name='davis',
      packages=['davis', 'davis.misc', 'davis.dataset', 'davis.measures'],
      package_dir={'':'python/lib'},
      include_package_data=False,
      package_data={'': ['data/*']},
      version='0.0.1',
      install_requires=[],)
