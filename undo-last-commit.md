# How to Undo the Last Commit (But Keep Your Work)

Sometimes I commit too early, or I realize I left a typo in the code. This command "undos" the commit but keeps all my changes staged and ready to be edited.

### The Command
```bash
git reset --soft HEAD~1
