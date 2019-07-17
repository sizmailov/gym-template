Add new contest
###############

1. Copy 101 folder and rename it to ``<contest name>``
2. Add ``add_subdirectory(<contest name>)`` to the end of main ``CMakeLists.txt``
3. Reload CMake Project

You are likely need one active contest, so comment out other contests.


Add new problem
###############

1. Create main.cpp in subfolder of the contest
2. Reload CMake Project


Add problem tests
#################

1. Add ``input.*`` and corresponding ``expected.*`` to a problem folder

To run all test for the problem build ``<contest name>.<problem name>.tests`` target

Tests require python 3.6+ interpreter.


**Warning:**  Output of the program compared line by line ignoring leading and trailing space characters.
