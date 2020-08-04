"""
Implementation of Econometric measures of 
connectness and systemic risk in finance and 
insurance sectors by M.Billio, M.Getmansky, 
Andrew Lo, L.Pelizzon
"""

import numpy as np
import pandas as pd 
from ..Data.data import Data
from sklearn.decomposition import PCA

class Connectedness:
    """
    Class computes the interconnections in 
    financial sectors
    """
    
    def __init__(self, start, end):
        self.returns = Data(start, end).preprocess_data()
    
    def compute_pca(self):
        pass
