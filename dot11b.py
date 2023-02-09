# 802.11b PPDU classes

import numpy as np
from math import floor, ceil

# NOTES:
# - currently I'm mixing data types, using ints and numpy arrays to represent the fields
#   at this point in time, simply representing each PPDU field as a LIST makes the most sense
#   should be easy enough to generate the sub-lists and then concat them all together to form the main list (full PPDU)

# generic PPDU class
class PPDU:
    # declare the PPDU fields
    def __init__(self):
        self.sync             = None
        self.sfd              = None
        self.headerSignal     = None
        self.headerService    = None
        self.headerLength     = None
        self.headerChecksum   = None
        self.header           = None
        self.payload          = None
        self.ppdu             = None
        self.scrambledPpdu    = None

    # scramble
    @staticmethod
    def scramble(scramInitSeed, numIterations):
        print("hi")
        
    # checksum (CRC)
    @staticmethod
    def checksum(crcInitSeed, numIterations):
        # don't need init seed, can just hardwire all 1s from within this function
        print("hi")

    # calculate the payload length (in microseconds)
    @staticmethod
    def calcPayloadLengthUs(length, rate):
        return ceil((length*8)/rate)

    # determine the state of the length extension bit
    @staticmethod
    def lenExt(length, rate):
        return 0 if (ceil((length*8)/rate) - ((length*8)/rate) < 8/11) else 1

    # encode the rate 
    @staticmethod
    def calculateSignalHeader(payloadRate):
        if(payloadRate == 1):
            rate = int("0A", 16)
        elif(payloadRate == 2):
            rate = int("14", 16)
        elif(payloadRate == 5.5):
            rate = int("37", 16)
        elif(payloadRate == 11):
            rate = int("6E", 16)
        return rate
    
    # encode the lock clocks and length extension bits
    def calculateServiceHeader(self, payloadLenBytes, payloadRate):
        return ( (self.lenExt(payloadLenBytes, payloadRate) << 7) | int("00000100", 2) )
        

class LongPPDU(PPDU):
    def __init__(self, payloadLenBytes, payloadRate):
        self.sync             = np.ones(128)
        self.sfd              = int("F3A0", 16)   # NOTE: need to check that the SFD value is correct
        self.headerSignal     = self.calculateSignalHeader(payloadRate)
        self.headerService    = self.calculateServiceHeader(payloadLenBytes, payloadRate)
        self.headerLength     = self.calcPayloadLengthUs(payloadLenBytes, payloadRate)
        self.header           = None  # TODO: up to here
        self.headerChecksum   = None
        self.payload          = None
        self.ppdu             = None
        self.scrambledPpdu    = None


# include a modulator (BPSK/QPSK mapper etc) and a radio class (mixing with 2.4GHz LO)
