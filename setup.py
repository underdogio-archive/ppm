import sys

from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
    name='ppm',
    version='0.1.0',
    description='The PyPA recommended tool for installing Python packages.',
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords='easy_install distutils setuptools egg virtualenv',
    author='The pip developers',
    author_email='python-virtualenv@groups.google.com',
    url='https://pip.pypa.io/',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ppm=ppm:main',
            'ppm%s=ppm:main' % sys.version[:1],
            'ppm%s=ppm:main' % sys.version[:3],
        ],
    },
)
