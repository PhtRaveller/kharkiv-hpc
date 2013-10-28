# Remember about color for root.
# Set it to red before git branch indication, then to green, and then to red again

# Add code here. 
_start='\[$(ppwd)\]$(if [ $(id -u) -eq 0 ]; then echo "\[$(tput setaf 1; tput bold)\]\h:"; else echo "\u@\h:"; fi)'

# Add correct substitution to sed to remove asterisks.
_gitprompt_br='\[$(tput setaf 2; tput bold)\]$(git branch 2> /dev/null | sed "s|* | (|;s|$|) |")'

_ending="\[$(tput sgr0)\]\w> "

export PS1=$_start$_gitprompt_br$_ending
