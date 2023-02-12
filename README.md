# 802.11b-model
A Python model to simulate the 802.11b DSSS/CCK PHY layer, both Tx and Rx.

## The Plan
- Start off with the 1/2Mbps Tx and Rx chains. 5.5/11Mbps CCK mode can follow after.
- Should be able to transmit bits/bytes from:
  - a text file containing string data (up to 4095 bytes as per the protocol's payload limit)
  - the command line, where the user enters arbitrary string data on the command line
- Include an interactive mode, where a terminal prompt pops up and the entire process is broken down into stages.The user should be able to hit enter to cycle through these stages. Various plots and terminal output should be given at each stage to show what's happening.
- Include screenshots of the matplotlib plots in the README

### Bugs/Progress
- ...

### User Guide
TODO...

### Development Notes
- The amount of AWGN in the channel should be user input in dBm.
- Could try to model transmission distance as well (user input parameter)
  - could model this by simply reducing the signal strength -> ie figure out the reduction factor as a function of distance of a typical signal and set this to the signal strength as seen by the receiver. Signal strength vs distance has got to be a pretty well defined function ~ 1/r or 1/r^2 etc
- Simulate the channel with varying levels of AWGN, which gets superposed with the transmitted signal. Also simulate the effect of narrowband interference/jamming to see how robustly the spread-spectrum signal can tolerate the effects of this noise.
