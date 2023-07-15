================
tic-tac-toe
================


.. image:: https://img.shields.io/pypi/v/tic-tac-toe.svg
        :target: https://pypi.python.org/pypi/tic-tac-toe

.. image:: https://img.shields.io/travis/GiovanniBruno22/tic-tac-toe.svg
        :target: https://travis-ci.com/GiovanniBruno22/tic-tac-toe

.. image:: https://readthedocs.org/projects/tic-tac-toe/badge/?version=latest
        :target: https://tic-tac-toe.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

A tic-tac-toe made in python 3 using QtGui5.


* Free software: MIT license
* Documentation: https://tic-tac-toe.readthedocs.io.


Features
--------

* Play a game of tic-tac-toe against another player locally.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/GiovanniBruno22/tic-tac-toe/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

tic-tac-toe could always use more documentation, whether as part of the
official tic-tac-toe docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/GiovanniBruno22/tic-tac-toe/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `tic-tac-toe` for local development.

1. Fork the `tic-tac-toe` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/tic-tac-toe.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv tic-tac-toe
    $ cd tic-tac-toe/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   ::

    $ flake8 tic-tac-toe

   To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags
