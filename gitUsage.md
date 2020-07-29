

## Git
### 保存单个文件的变动并应用
```shell
# To "stash" a particular file/dir only:

git diff path/to/dir > stashed.diff
git checkout path/to/dir

# Then afterwards
git apply stashed.diff
```
https://stackoverflow.com/questions/3040833/stash-only-one-file-out-of-multiple-files-that-have-changed-with-git/3041055#3041055



