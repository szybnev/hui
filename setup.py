
from setuptools import setup

setup(
  name = 'hui',
  packages = ['hui'],     
  version = '0.1.1',
  license='MIT', 
  author = 'Slonser',
  author_email = 'slonser@slonser.info',
  url = 'https://github.com/slonser/hui',
  download_url = 'https://github.com/Slonser/hui/archive/v_01.tar.gz',
  keywords = ['HTML', 'hui', 'HTML GUESSER', "HTML identifier"],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  package_data={'': ['generated_payloads.json','results_parsers/*.json']}
  )