from distutils.core import setup, Extension

setup(name='cFibonacciModule', version='1.0',  \
      ext_modules=[Extension('cFibonacci', ['cFibonacci.c'])])