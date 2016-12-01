from distutils.core import setup, Extension

setup(name='cfibonacci', version='1.0',  \
      ext_modules=[Extension('cfibonacci', ['cfibonacci.c'])])