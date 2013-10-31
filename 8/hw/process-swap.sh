#!/usr/bin/sh

# Check whether we have enough arguments (exactly one)
# If no - exit with status 1
if [ $# -ne 1 ]
then
    echo "Wrong number of arguments"
    exit 1
fi

# $1 contains first command line argument, in our case it should be process ID
PID=$1

# Accumulator for swap scape
SUM=0

# Get command line which started process.
# STDERR is dropped, so if no such process, PCL will be empty
PCL=$(cat /proc/$PID/cmdline 2> /dev/null)

# Check whether process with PID actually exists and is readable
# We use -z key for test command, which checks is string has zero length.
# If we cannot read process info - exit with status 2
if [ -z $PCL ]
then
    echo "I cannot find process with ID $PID.\
Either there is no such process, or you do not have permissions\
to inspect it (unlikely, since cmdline and smaps have 444 permissions)."
    exit 2
fi

# Let's grab swap data
# grep Swap /proc/$PID/smaps returns strings which contain swap data
# Then we use sed -r 's|\s+| |' to remove multiple spaces
# Now we can use cut command to get numeric field with swap space for current mapping
for i in $(grep Swap /proc/$PID/smaps | sed -r 's|\s+| |' | cut -f 2 -d ' ')
do
    # We accumulate swap volume for each mapping in SUM
    let SUM=$SUM+$i
done

echo "Total swap space used by process $PID ($PCL): $SUM kB"