import sys

from setuptools import setup

sys.path.append('.')
import sizechart_editor


setup(
    name='Size Chart Editor',
    version=sizechart_editor.__version__,
    author='Balazs Kulcsar',
    author_email='kulcsarb@gmail.com',
    description='Size Chart Editor application + API',
    packages=['sizechart_editor'],
    install_requires=[
        'aiohttp',
        'aiohttp-swagger',
        'yoyo-migrations',
        'psycopg2',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'sizechart_editor=sizechart_editor.app'
        ]
    }
)