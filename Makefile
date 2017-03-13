 
install: 
	- pip uninstall pet
	- pip install .
	- pip install -e .
clean:
	- rm -rf ./**/*/__pycache__ ./*.egg-info ./build ./dist ./logs/* 
