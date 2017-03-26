# from distutils.core import setup
from setuptools import setup


def readme():
    try:
        import pypandoc
        long_description = pypandoc.convert('README_en.md', 'rst')
    except(IOError, ImportError):
        long_description = open('README_en.md').read()

    return long_description


setup(
    name='pet',
    version='0.3.3',
    description='This program or lib can download torrent file through'
    + 'email account and send the torrent file to transmission web controller',
    long_description=readme(),
    download_url='https://github.com/drake-jin/pi-email-transmission/archive/0.3.3.tar.gz',
    url='http://github.com/drake-jin/pi-email-transmission',
    author='drakejin',
    author_email='dydwls121200@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
    ],
    include_package_data=True,
    keywords='torrent transmission rpc email download bittorrent utorrent',
    packages=['pet', 'pet/src', 'pet/src/controller', 'pet/test',
              'pet/utils', 'pet/utils/config'],
    # This is for develop yet, I will change this list
    entry_points={
        'console_scripts': [
            'pet=pet.__main__:main'
        ],
    },
    install_requires=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False


)


'''
        entry_points={
            'console_scripts': [
                'pet=pet.__main__:main'
            ],
        },

'''
