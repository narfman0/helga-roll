from setuptools import setup, find_packages
from helga_roll import __version__ as version


setup(
    name='helga-roll',
    version=version,
    description=('Roll dice or choose from set'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot roll dice',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/helga-roll',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_roll.plugin'],
    zip_safe=True,
    install_requires=[
        'helga',
    ],
    test_suite='tests.test_roll',
    entry_points=dict(
        helga_plugins=[
            'roll = helga_roll.plugin:roll',
        ],
    ),
)
