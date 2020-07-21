import logging,os

class logger:
    logg = logging.getLogger()
    fh = logging.FileHandler(logg)
    sh = logging.StreamHandler()