# Remember about color for root.
# Set it to red before git branch indication, then to green, and then to red again

# Add code here. 
_start='\[$(ppwd)\]$(if [ $(id -u) -eq 0 ]; then echo "$(tput setf 4)"; fi)'

# Add code for root here. No username for root.
_gitprompt_user='$(if [ $(id -u) -eq 0 ]; then echo "Empty. Add smth here."; else echo "\u@\h "; fi)'

# Add correct substitution to sed to remove asterisks.
_gitprompt_br=' $(git branch 2> /dev/null | sed "") '

_ending="\w> "

export PS1=$_start$_gitprompt_user$_gitprompt_br$_ending