Entangle examples for Python 2.7+
=================================

This repository contains examples of using Entangle services in Python 2.7+.


Building
--------

To build the examples, make sure that you have `Entangle <https://github.com/entangle/entangle>`_ installed. Building should then be a simple case of cloning the repository and installing dependencies as follows:

::

   $ git clone --recursive git@github.com:entangle/example-py2.git
   $ cd example-py2
   $ virtualenv --distribute venv
   $ source venv/bin/activate
   $ pip install -r requirements.txt
   $ make


Examples
--------

A simple arithmetic service
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example is a simple arithmetic service which provides integer arithmetic. The ``arithmetic_client.py`` script connects to an arithmetic server on port 5555 and runs examples of using the arithmetic server.
