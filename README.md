# 802.11b-model
A Python model to simulate the 802.11b DSSS/CCK PHY layer, both Tx and Rx.

## The Plan
- Start off with the 1/2Mbps Tx and Rx chains. 5.5/11Mbps CCK mode can follow after.
- Should be able to transmit bits/bytes from:
  - a text file containing string data (up to 4095 bytes as per the protocol's payload limit)
  - the command line, where the user enters arbitrary string data on the command line
- Include an interactive mode, where a terminal prompt pops up and the entire process is broken down into stages.The user should be able to hit enter to cycle through these stages. Various plots and terminal output should be given at each stage to show what's happening.
- Simulate the channel with varying levels of AWGN, which gets superposed with the transmitted signal. Also simulate the effect of narrowband interference/jamming to see how robustly the spread-spectrum signal can tolerate the effects of this noise.

### Bugs/Progress
- ...

### Simulation Stages
- Generating PPDU: annotate the PPDU sections, show the scrambled and unscrambled PPDU (maybe without the SYNC+SFD?)

(WIP)...
- Barker code 'mapping'
- DBPSK/DQPSK mapping
- Some kind of filtering??? (Barker-matched filter etc...)
- Radio stage (show waveform segment and spectral output)
- Receiver... (TODO)

### User Guide
TODO...
