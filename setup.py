import os
import setuptools

NAME = 'parrotizer'
DESCRIPTION = 'Turn text into a slackmoji-parrotized text'
VERSION = None

CONSOLE_SCRIPTS = [
    'parrotize=parrotizer:cli_print'
]

INSTALL_REQUIRES = [
]

EXTRAS_REQUIRE = {}

here = os.path.abspath(os.path.dirname(__file__))

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setuptools.setup(name=NAME,
                 version=about['__version__'],
                 description=DESCRIPTION,
                 url='https://github.com/bradsbrown/parrotizer',
                 author='Brad Brown',
                 author_email='brad@bradsbrown.com',
                 license='MIT',
                 entry_points={
                     'console_scripts': CONSOLE_SCRIPTS,
                 },
                 install_requires=INSTALL_REQUIRES,
                 packages=setuptools.find_packages(),
                 include_package_data=True,
                 zip_safe=False,
                 extras_require=EXTRAS_REQUIRE,
                 )

