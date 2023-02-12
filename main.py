# main 802.11b model code

import numpy as np
import dot11b

# include an argument parser (give a usage example etc)
# DSSS/CCK switchable via cmd line argument

if __name__ == "__main__":
    LongPPDU = dot11b.LongPPDU(2, 1)
    print(LongPPDU.sync)
    print('-----------------')
    print(LongPPDU.sfd)
    print('-----------------')
    print(LongPPDU.headerSignal)
    print('-----------------')
    print(LongPPDU.headerService)
    print('-----------------')
    print(LongPPDU.headerLength)
    print('-----------------')

""" stages:
1- header generation
2- header scrambling
3- (WIP)...
- Barker code 'mapping'
- DBPSK/DQPSK mapping
- Some kind of filtering??? (Barker-matched filter etc...)
- Radio stage (show waveform segment and spectral output)
- Receiver... (TODO)

"""