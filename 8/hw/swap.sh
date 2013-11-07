#!/bin/bash

# Accumulator for total swap used
TOTAL_SWAP=0

# Iterate over PIDs
for pid in $(ls -d /proc/[0-9]* | cut -d / -f 3)
do
    # Initialize accumulator for current PID
    SUM=0
    # Iterate over mappings
    for sw in $(grep Swap /proc/$pid/smaps 2> /dev/null | sed -r 's|\s+| |' | cut -f 2 -d ' ')
    do
        SUM=$(( $SUM + $sw ))
    done
    # Add swap used by current PID to total swap accumulator
    TOTAL_SWAP=$(( $TOTAL_SWAP + $SUM ))
# Echo swap usage by current PID
echo "PID $pid: $(cat /proc/$pid/comm 2> /dev/null) Swap used: $SUM kB"
done
# Echo total swap usage
echo "Total swap used: $TOTAL_SWAP kB"