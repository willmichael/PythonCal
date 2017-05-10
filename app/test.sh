#!/bin/bash
echo "running"
python setup.py py2app -A
open ./dist/PythonCal.app/Contents/MacOS/PythonCal
