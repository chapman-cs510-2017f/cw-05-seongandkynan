# CS510 CW 5

**Author(s):** **Seong Heon Lee and Kynan Barton**

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-05-seongandkynan.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-05-seongandkynan)

## Specification

1. With your **new** group of **two**, carefully read through this [Example docstring style guide](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) from Google. Google code may not be committed to the company repository without following this level of detail in docstrings. Similarly, skim over the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) that specifies proper coding style in Python for Google.
1. Critique the most recent classwork of your group member:
    * Open a Jupyter notebook: ```critique.ipynb```
    * Have one member of your group (the "reviewee") open the python code for their previous CW04 (i.e., the module, the test module, and the Juyter notebook). Have the other member (the "reviewer") constructively critique the code in a clearly labeled section of the critique Jupyter notebook. Use the following questions as a guideline: Is it clear how the code is organized? Is the code properly documented with both docstrings and supplementary comments according to industry standards? Can you follow the algorithm of the code, i.e., what it is doing, and how? Do you see any suggestions for how to improve the code? Are there test cases for the code? Do the tests verify correct functionality? Are there tests that would have been good to include but are missing? Is the Jupyter notebook a clear discussion of the problem, solution, and outline of the algorithm used in the code? On a scale of 0-100, the reviewer should rate the work produced by the reviewee. As the reviewer writes this critique and evaluation into the Jupyter notebook, the reviewer should discuss these questions and any issues that arise with the reviewee.
    * Repeat this exercise, but swapping roles of "reviewee" and "reviewer", and record the second critique in a new section of the notebook.
    * Note that in industry, code is typically reviewed in this fashion by fellow employees or bosses at regular intervals, for quality assurance. You are always liable for anything you commit to a repository. Moreover, constructive criticism is essential: do not demean your colleagues, dismiss their feedback, or engage in any behavior that could be construed as promoting a toxic environment. The end goal of such a process is to increase the quality of code being generated throughout the organization, so it is not to your advantage to allow bad coding practices to continue---that is, be vocal about things that could use improvement.
1. With your new partner, work through the [Python object slides](http://slides.com/profdressel/python-objects-overview) carefully. Be sure to use ```ipython3``` in a terminal to test how things work (or in a scratch Jupyter notebook). Discuss amongst yourselves anything that is new or unclear.
1. Create a python module ```cplane.py```. Create a new class ```ListComplexPlane``` that subclasses the abstract base class ```AbsComplexPlane``` provided in the ```abscplane.py``` module already in the repository. Provide implementations for the requested methods. As the implementation of the `plane` attribute, use a list of lists to represent the 2D grid needed to store the complex plane. Be sure to set all attributes properly during the ```__init__``` constructor, and initialize the plane immediately upon instantiation. Be careful to follow the Google style guidelines when completing your work.
1. Create a test module ```test_cplane.py``` that verifies that your implementation is correct.
1. In a Jupyter notebook ```cplane.ipynb``` provide a demonstration of how your class works (using small grids of points for clarity). Include a discussion about what an abstract base class helps a programmer do, and why it might be useful even though it doesn't do anything by itself. Discuss what tests you performed to verify correct functionality.
1. After your notebooks are complete, spell-checked, and professionally formatted, add and commit them to GitHub. Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having only one person from your edit the notebooks at a time, being sure to pull all changes before you start editing yourself.


## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**Seong Heon Lee and Kynan Barton**
