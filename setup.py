from setuptools import setup, find_packages

setup(
    name='my-cli-app',
    version='0.1.0',
    description='A command-line interface application',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'my-cli=my-cli-app.cli:main',
        ],
    },
    install_requires=[
        # List your dependencies here
    ],
)