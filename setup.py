setup(
    name='BRS_Assignment_Pokemon',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pyyaml',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'BRS_Assignment_Pokemon = BRS_Assignment_Pokemon.__main__:main',
        ],
    },
    author='Basil Afzal',
    author_email='basil.afzal@gmail.com',
    description='BRS Assignment - Basil Afzal, 2024',
    license='MIT',
