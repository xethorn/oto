from setuptools import find_packages
from setuptools import setup


setup(
    name='Oto',
    version='0.0.1',
    url='https://github.com/xethorn/oto',
    author='Michael Ortali',
    author_email='github@xethorn.net',
    description=(
        'Standardize communication between the different layers of an '
        'application.'),
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: Alpha',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],)
