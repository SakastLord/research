"""
Class to procure data needed for research
"""

import numpy as np 
import yfinance as yf 

class Data:
    """
    Class used to obtain data from yahoo finance for 
    Hedge funds, insurance, banks and broker/dealers
    """
    def __init(self, start: str, end: str):
        """Constructor used to initialize start and end period

        Args:
            start (str): Start date in format YYYY-MM-DD
            end (str): End date in format YYYY-MM-DD
        """
        self.start = start 
        self.end = end 
    
    def get_prices(self, col: str = 'Adj Close'):
        """get adjusted close price from yahoo finance

        Args:
            col (str, optional): the type of price. Defaults to 'Adj Close'.
        """
        # store bank tickers
        bnk_tkr = \
            """JPM, BAC, WFC, FITB, USB, TFC, PNC, BK, STT, SCHW,
               COF, GS, HSBC, FINN, MS, TD, ALLY, KEY, BMO
               RY, MUFG, AMP, SAN, BCS, CFG, UBS, NTRS, MTB,BNP,
               MTB, FRC, CS, SYF, BBVA, CIT, TCF, EWBC, MFG, FHN,
               FNB, WTFC, CFR, TCBI, PACW, CATY, CADE, BOH, FHB, C
               """
        # store hedge fund tickers
        insurance_tkrs = \
            """PGR, AIG, MET, ZFSVF, THG, 
               BHF, RDN, ANAT, RLI, MMC, 
               PRU, AFL, CI, UNH, TRV,
               NFS, LBH, ERIE, HIG, ALIZY
            """
        # store broker/dealer info
        broker_tkrs = ''

