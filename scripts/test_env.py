def test_tensorflow():
    import tensorflow as tf
    assert tf.__version__ is not None, "TensorFlow is not installed"

def test_pandas():
    import pandas as pd
    assert pd.__version__ is not None, "Pandas is not installed"

def test_scikit_learn():
    import sklearn
    assert sklearn.__version__ is not None, "Scikit-learn is not installed"

def test_statsmodels():
    import statsmodels
    assert statsmodels.__version__ is not None, "Statsmodels is not installed"