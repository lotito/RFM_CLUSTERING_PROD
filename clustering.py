import LoadingFile as EM
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys
import os

class RfmClustering ( object ):
# Charging  the xls file

# Constructor
    def __init__ ( self):
        self.nb_cls = ""
# End of constructor
    def DoKmeans ( self ):
        self.nb_cls = int(input("Select your clusters number : "))
