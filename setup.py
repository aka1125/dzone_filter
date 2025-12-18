from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'dzone_filter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aka',
    maintainer_email='akayuusaku91@gmail.com',
    description='a package for dzone_filter',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'filter_node = dzone_filter.filter_node:main',
            'test_publisher = dzone_filter.test_publisher:main',
        ],
    },
)
