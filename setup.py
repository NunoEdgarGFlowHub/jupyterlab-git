"""
Setup Module to setup Python Handlers (Git Handlers) for the Git Plugin.
"""
import setuptools

setuptools.setup(
    name='jupyterlab_git',
    version='0.1.1',
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
        'psutil'
    ],
    package_data={'jupyterlab_git': ['*']},
)
