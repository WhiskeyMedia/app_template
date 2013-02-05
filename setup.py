from os.path import join, dirname
from setuptools import setup


VERSION = (0, 0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README.rst'))
long_description = f.read().strip()
f.close()

install_requires = [
    'Django',
    'ella>=3.0.3',
]
test_requires = [
    'nose',
    'coverage',
]

setup(
    name = 'PACKAGE_NAME',
    description = "PACKAGE_NAME",
    url = "https://github.com/ella/PACKAGE_NAME/",
    long_description = long_description,
    version = __versionstr__,
    author = "ella",
    author_email = "ella.project@gmail.com",
    packages = ['APP_NAME'],
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,

    test_suite='test_APP_NAME.run_tests.run_all',
    test_requires=test_requires,
)
