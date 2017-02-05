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