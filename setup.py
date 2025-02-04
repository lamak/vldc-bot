from setuptools import setup


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements_:
        for install in requirements_:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name='vldc-bot',
    version='0.1',
    packages=[''],
    url='https://github.com/egregors/vldc-bot',
    license='MIT',
    author='Vadim Iskuchekov (@egregors)',
    author_email='root@egregors.com',
    description='The official VLDC bot',
    install_requires=requirements(),
)
