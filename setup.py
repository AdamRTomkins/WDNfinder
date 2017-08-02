from distutils.core import setup
import setuptools
 
setup(name = "WDNfinder",
      version = "0.2",
      description = "A library for finding the minimal driver nodes of a network",
      author = "Chu Yanshuo, edited by Adam Tomkins",
      author_email = "a.tomkins@sheffield.ac.uk",
      url='https://github.com/AdamRTomkins/WDNfinder',
      packages=[],
      install_requires=[
          'networkx>= 1.1.0'
      ],
      setup_requires=[],
      tests_require=[]
      )
