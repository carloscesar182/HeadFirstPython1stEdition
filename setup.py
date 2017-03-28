# Import the setup function from Python´s distribution utilities
from distutils.core import setup

"""On the left side are the setup function´s argument names.
On the right side, your module´s metadata with de setup function´s arguments."""
setup(
    name='nester',
    version='1.2.0',
    py_modules=['nester'],
    author='carloscesar182',
    author_email='carloscesar182@gmail.com',
    url='https://github.com/carloscesar182',
    description='A simple printer of nested files'
)