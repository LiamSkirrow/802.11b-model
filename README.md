# 802.11b-model
A Python model to simulate the 802.11b DSSS/CCK PHY layer, both Tx and Rx.

## The Plan
- Start off with the 1/2Mbps Tx and Rx chains. 5.5/11Mbps CCK mode can follow after.
- Should be able to transmit bits/bytes from:
  - a text file (up to 4095 bytes as per the protocol's payload limit)
  - the command line, where the user enters arbitrary data on the command line in a string format
- Include an interactive mode, where a terminal prompt pops up and the entire process is broken down into stages, and the user can hit enter to cycle through these stages. Various plots and terminal output should be given at each stage to show what's happening. 
- Simulate the channel with varying levels of AWGN.

### Bugs/Progress:
- ...
