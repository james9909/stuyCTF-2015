#!/bin/bash

flag=""
cd notsvn
for i in {1..9}; do
    flag=$(cat git_isnt_svn)$flag
    git checkout HEAD~1 &> /dev/null
done
git checkout master &> /dev/null
git stash pop &> /dev/null
flag=$flag$(cat git_isnt_svn)
git stash &> /dev/null
echo $flag

# When we unzip the zipped files, we can see that there is a .svn folder. The problem is
# Not SVN, and its contents look like a .git folder, so if we change .svn to .git, we
# discover a lot of things, namely the commits. If we view the commits and the changes,
# it spells out the flag. However, it is not complete, and looking a little bit
# shows that there are stashed changes. If we apply the stash, using 'git stash pop',
# we get the rest of the flag.

# stuy{ro11_b4ck_c0mm1t5}
