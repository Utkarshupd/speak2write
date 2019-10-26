from setuptools import setup

with open("README.md", 'r') as f:
  long_description = f.read()


setup(
  name = 'speak2write',        
  packages = ['speak2write'],   #same as name
  version = '1.0',      
  license='MIT',        # https://help.github.com/articles/licensing-a-repository
  description = long_description,   # Give a short description about your library
  author = 'Utkarsh Dixit',                   
  author_email = 'utkarshupd@gmail.com',      
  url = 'https://github.com/Utkarshupd/speak2write',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Utkarshupd/speak2write.git',    
 
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
