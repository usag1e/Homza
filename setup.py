from setuptools import setup

setup(name='Homza',
      version='0.1',
      description='Get the content of tech news websites and get data out of them',
      url='https://github.com/usag1e/Homza/',
      author='The Nalyze Team',
      author_email='team@nalyze.net',
      license='custom',
      packages=['nalyzer_core'],
      install_requires=[
	'couchdb',
	'couchdbkit',
	'restkit',
	'python-dateutil==2.4.0',
	'pydash',
	'python-nmap'
      ],
      zip_safe=False)
