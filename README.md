### C1 Coursework

This is my repository for the C1 coursework.

The report for this project is in pdf format and is located in the `report` directory.

# dual_autodiff

The **dual_autodiff** package is a Python package designed to perform automatic differentiation using dual numbers.

## Features

- **Dual class:** Core attributes and methods. It is used to create dual numbers and implement arithmetic operations on them as well as some common mathematical functions.

## Installation

Ensure you have Python 3.9 or higher. You will need Python 3.10 or 3.11 to install the Cython wheels. 
You can install the Python package from within the root directory of the repository by running:

```bash
pip install -e .
```

This will also install the required dependencies (numpy).

To install the Cythonized version of the package, navigate to the **Cython project folder** `dual_autodiff_x` and run:

```bash
pip install -e .
```

Alternatively, you can install directly from the wheels, located in the `dual_autodiff_x/wheelhouse` directory. 


## Usage

A quick example of how to use the package is shown below.

```python
import dual_autodiff as df 
x=df.Dual(2,1)
print(x.sin())
y=df.Dual(3,4)
print(x+y)
```

For a more detailed introduction, see the tutorial notebook located in the `docs/Tutorial` directory. Please also refer to the documentation for more information. 

## Documentation

To build the documentation, navigate to the `docs` directory and run:

```bash
make html
```

The documentation will be located in the `docs/_build/html` directory. Open the `index.html` file in a web browser to view the documentation.

## Testing

To run the tests for the Python package, run the following command from the root directory:

```bash
pytest -s tests/*
```

To check the Cython package is correctly installed, you can open the `cython_test.ipynb` notebook located in the root directory and run the cells in there.

### How to run the Jupyter Notebooks

You will need to install the required packages to run the Jupyter notebooks in this repository. A simple way to guarantee that the notebooks will run is to create a new conda environment using the `environment.yml` file provided.

Clone this GitLab repository to your local machine.
```bash
git clone https://gitlab.developers.cam.ac.uk/phy/data-intensive-science-mphil/assessments/c1_coursework/fm565.git
```
Create a conda environment by running:
```bash
conda env create -f environment.yml
```
in the root directory of this repository.

This will create a new conda environment called `C1Coursework`. This will install the necessary packages for this project, listed in the `requirements.txt` file.

Activate the environment by running:
```bash
conda activate C1Coursework
```

This may automatically create a Jupyter Kernel for the new environment. If not, you can create a kernel manually e.g.
```bash
python -m ipykernel install --user --name C1Coursework --display-name "C1Coursework (Python 3.11)"
```
You should now be able to run the notebooks in this repository.

To deactivate the conda environment, run `conda deactivate`.