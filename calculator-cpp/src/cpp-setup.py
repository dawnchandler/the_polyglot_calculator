from setuptools import setup, Extension

# Compile *mysum.cpp* into a shared library
setup(
    ext_modules=[
        Extension('mysum', ['calculator.cpp'],),
        Extension('add', ['calculator.cpp'],),
        Extension('sub', ['calculator.cpp'],),
        Extension('mult', ['calculator.cpp'],),
        Extension('divide', ['calculator.cpp'],),
        Extension('power', ['calculator.cpp'],),
    ],
)
