March 25, 2017 -- ssteinerX
---------------------------
Refactored and simplified tests while making them more thorough.

Updated tests to run under [tox](https://tox.readthedocs.io/en/latest/) and 
separated the inherited runtime environment from the tests.

Tests currently pass on all the environments in which the project is 
supposed to run: 2.7, 3.5, and 3.6.

Updated docs to show how to run tests and how to work in development mode for
anyone who wants to contribute to the project.

February 4, 2017 -- ssteinerX
-----------------------------
Add setup.cfg and rearrange setup.py to use current pytest conventions and pytest-runner plugin

Remove Bitdeli badge from README.md, [Bitdeli acquired and shut down](https://www.linkedin.com/in/villetuulos)

	> Bitdeli was powered ... [Ville Tuulos] was the CEO.
	> Bitdeli was acquired by AdRoll in June 2013.

February 3, 2017 -- ssteinerX
-----------------------------
Create add-unit-tests branch to add some unit tests in anticipation of
full Python 3.x compatibility.

Add this CHANGES.md file to keep track of changes for detail beyond commit messages.

Add specific Python versions to setup.py.

Add test class and associated test_* support items to setup.py.

Add version constraints to install_requires to ensure Python 3 compatible
versions of dependencies.

Update .gitignore to skip .cache/, .eggs/, and .idea (PyCharm) files.

Add tests module at root level to contain test suite.
