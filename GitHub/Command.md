```
ssh-keygen -t rsa -C "youremail@example.com"
ssh -T git@github.com

git config --global user.name "your name"
git config --global user.email "your_email@youremail.com"

git init #把当前目录变成Git可以管理的仓库
git add/rm <file>
git commit -m "Comments"
git log --pretty=oneline	#查看提交历史，以便确定要回退到哪个版本
git log --graph	#查看分支合并图
git reflog	#查看命令历史，以便确定要回到未来的哪个版本
git reset --hard commit_id	#HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭
git status
git diff HEAD -- <file>	#查看工作区和版本库里面最新版本的区别
git checkout -- <file>	#丢弃工作区的修改
git reset HEAD <file>	#


git remote	#查看远程库的信息
git remote -v	#显示更详细的信息
git remote add origin git@github.com:Kindonia/MyPython.git	#关联一个远程库
git remote add origin https://github.com/Kindonia/MyPython.git	#关联一个远程库[http协议]
git remote rm origin	#删除远程 Git 仓库

#双关联
git remote add github git@github.com:michaelliao/learngit.git
git remote add gitee git@gitee.com:liaoxuefeng/learngit.git

git pull origin <name> --allow-unrelated-histories	#从远程仓库中获得数据，可以合并两个独立启动仓库的历史
git push github master
git push gitee master
git push origin <name>:<name>
git push -u origin <name>	#第一次推送master分支的所有内容

git clone git@github.com:Kindonia/MyPython.git	
git clone https://github.com/Kindonia/MyPython.git

git checkout -b dev	#创建dev分支，然后切换到dev分支 PS:checkout命令加上-b参数表示创建并切换
git switch -c dev	#创建并切换到新的dev分支
git branch dev	#创建dev分支
git checkout dev	#切换到dev分支
git switch master	#切换到dev分支
git merge dev	#把dev分支的工作成果合并到master分支上
git merge --no-ff -m "merge with no-ff" dev	#--no-ff参数，表示禁用Fast forward
git branch	#查看当前分支
git branch -d dev	#删除dev分支
git branch -D <name>	#强行删除没有被合并过的分支
git branch --set-upstream-to=origin/dev dev	#设置dev和origin/dev的链接
/*
分支策略
+---------------------+------------------------+----------	master
↘------+-------+----↗-----------+--------+--↗----------	dev
 ↘----↗------------------------↗-----------------------	work1
  ↘---------↗--------------------------↗---------------	work2

在实际开发中，我们应该按照几个基本原则进行分支管理：
首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，
再把dev分支合并到master上，在master分支发布1.0版本；
你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。

*/

git stash	#把当前工作现场“储藏”起来，等以后恢复现场后继续工作
git stash list	#查看缓存工作列表
git stash apply	#恢复工作，恢复后，stash内容并不删除，你需要用git stash drop来删除
git stash pop	#恢复的同时把stash内容也删了

git cherry-pick 4c805e2	#复制一个特定的提交到当前分支
git rebase	#把分叉的提交历史“整理”成一条直线，看上去更直观。缺点是本地的分叉提交已经被修改过了

git tag <name>	#打标签
git tag	#查看所有标签
git tag <name> <commit id>	#给历史提交的工作打标
git show <tagname>	#查看标签信息
git tag -a v0.1 -m "version 0.1 released" 1094adb	#创建带有说明的标签，用-a指定标签名，-m指定说明文字
git tag -d v0.1	#删除标签
git push origin <tagname>	#推送标签
git push origin --tags	#一次性推送全部尚未推送到远程的本地标签
git push origin :refs/tags/v0.9	#如果标签已经推送到远程，要删除远程标签就麻烦一点，先从本地删除,然后，从远程删除。

git config --global color.ui true	#让Git显示颜色，会让命令输出看起来更醒目
#忽略特殊文件
#在Git工作区的根目录下创建一个特殊的.gitignore文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。
#官方配置文件：https://github.com/github/gitignore
git check-ignore	#检查忽略文件规则
git add -f App.class	#强制添加到Git
#添加例外 把指定文件排除在.gitignore规则外的写法就是!+文件名

#自定义别名
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.last 'log -1'	#让其显示最后一次提交信息
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

#GUI: [SourceTree](https://www.sourcetreeapp.com/)
```
