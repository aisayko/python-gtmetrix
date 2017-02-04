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