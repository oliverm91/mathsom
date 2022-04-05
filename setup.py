from setuptools import setup

setup (
    name='numericsom',
    version='0.0.1',
    description='Personal package for numerical problems',
    author='Oliver Mohr B',
    author_email='oliver.mohr.b@gmail.com',
    url='https://github.com/oliverm91/',
    packages=['numericsom'],
    install_requires=[
        'numpy', 
        'scipy',
    ],
)
