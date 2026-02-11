import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn"])

import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt

print(sklearn.__version__)

df = pd.read_csv('../data/dataset.csv')
print(df.head())