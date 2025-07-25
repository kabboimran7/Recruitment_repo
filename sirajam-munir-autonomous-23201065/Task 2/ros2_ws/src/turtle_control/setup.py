from setuptools import setup

package_name = 'turtle_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/bringup.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name_here',
    maintainer_email='your_email@example.com',
    description='ROS 2 turtle_control package with figure-eight driving and trace toggle service',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'figure8_driver = turtle_control.figure8_driver:main',
            'trace_toggle = turtle_control.trace_toggle:main',
        ],
    },
)
