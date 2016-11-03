try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='eSSP3',
    version='2.0.1',
    description='Basic eSSP library for python 3',
    author='SMontoya',
    author_email='samuelmontoyag@gmail.com',
    url='https://github.com/smontoya/eSSP_P3',
    packages=['eSSP3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    license='?',
    install_requires=['pyserial'],
)
