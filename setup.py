from setuptools import setup, find_packages

setup(
    name='gauthuserinfo',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'gauthuserinfo = gauthuserinfo.gauthuserinfo:main'
        ]
    }
)
