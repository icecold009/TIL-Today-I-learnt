# Speeding up Workflow with Git Aliases

Writing `git status` or `git commit -m ""` dozens of times a day adds up. Git aliases allow you to create shortcuts for your most-used commands.

### How to set them up
Run these in your terminal to map long commands to short letters:

```bash
# Shortcut for status
git config --global alias.st status

# Shortcut for a pretty log (shows a graph of commits)
git config --global alias.lg "log --graph --oneline --all"

# Shortcut for committing
git config --global alias.cm commit
