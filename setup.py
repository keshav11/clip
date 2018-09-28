from setuptools import setup

setup(
    name='clip',
    packages=['clip'],
    version="0.1.1",
    author='Keshav Gupta',
    license='MIT',
    entry_points={
        'console_scripts': ['clip=clip.clip:main']
    }
)
