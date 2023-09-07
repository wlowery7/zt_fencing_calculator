# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:02:36 2023

@author: bacon
"""

from cx_Freeze import setup, Executable

build_options = {
    'packages': ['selenium', 'bs4', 'os', 'time'],  # Add other required packages here
    'excludes': [],
    'include_files': ['C:\\Users\\bacon\\chrome_driver\\chromedriver-win64\\chromedriver.exe'],  # Replace with the actual path
}

exe = Executable(
    script="Fencing Calculator.py",  # Replace with the name of your script
    icon='zt_logo.ico',  # Replace with the path to your icon file
    base=None,
)

setup(
    name="Fencing Calculator",
    version="1.0",
    description="",
    executables=[exe],
    options={
        'build_exe': build_options,
    }
)