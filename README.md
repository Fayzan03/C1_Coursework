# dual_autodiff

The **dual_autodiff** package is a Python package designed to perform automatic differentiation using dual numbers.

## Features

Add features here, mention Cython implementation, etc.

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