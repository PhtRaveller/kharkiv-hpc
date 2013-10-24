#!/usr/bin/sh

# $1..$9 ${10}.. are used a positional arguments
# $# is the curent number of arguments
# $@ are all arguments at once. Note difference between $@ and "$@"
# Try to call this script with some parameters

# Loop over positional arguments
echo "Using explicit for-loop:"
for arg in "$@"; {
    echo $arg
}

echo "Using explicit for-loop without quoting:"
for arg in $@; {
    echo $arg
}

# Positional arguments are implicitly used in this loop
echo "Using implicit for-loop:"
for arg
do
    echo $arg
done

# Note command substitution and test brackets
echo -e "\nTesting who you are:"
if [ $(id -u) -eq 0 ]
then
    echo "You're a root"
else
    echo "You're ordinary user with ID $(id -u)"
fi

# Using classical if clause. Note semicolon before then
echo -e "\nLooking, whether we have git repo here:"
if git branch &> /dev/null; then
    echo "We have repo here, branch is $(git branch | sed 's#* ##')"
else
    echo "We have no repo here. Strange."
fi