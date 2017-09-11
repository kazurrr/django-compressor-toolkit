from setuptools import setup, find_packages

import compressor_additional_compilers


setup(
    name='django-compressor-additional-compilers',
    version=compressor_additional_compilers.__version__,
    description='Set of add-ons for django-compressor',
    long_description=(
        'Simply enable SCSS and ES6 in your Django project. '
        'Read more on `project\'s GitHub page '
        '<https://github.com/kazurrr/django-compressor-toolkit>`_.'
    ),
    url='https://github.com/kazurrr/django-compressor-toolkit',
    author='Karol Masuhr',
    author_email='karol@masuhr.pl',
    license='MIT',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'django-compressor>=1.5'
    ],
    extras_require={
        'test': [
            'django~=1.8',
            'pytest~=3.0',
            'pytest-django~=3.0',
            'pytest-cov~=2.4',
            'pytest-pythonpath~=0.7'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
