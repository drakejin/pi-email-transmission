 install: 
	- pip uninstall pit
	- pip install .
	- pip install -e .
	- python setup.py install
clean:
	- rm -rf ./**/*/__pycache__ ./*.egg-info ./build ./dist ./logs/* 
