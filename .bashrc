# .bashrc
source ~/.git-prompt.sh
source ~/.git-completion.bash
. ~/.git-prompt.sh
. ~/.git-completion.bash
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi


# GIT bash integration
export GIT_PS1_SHOWDIRTYSTATE=1

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
#PS1="\h\w "
PS1="\\h\w\$(__git_ps1 '(%s)') \$ "

GIT_PROMPT_ONLY_IN_REPO=1
source ~/.bash-git-prompt/gitprompt.sh
