1 git bash使用

git 密码：th0210

首先 
1、git clone 网址

或者 git init 作为本地库

2、git add .或者filename

添加文件

3、git commit -m""

添加信息

4、git push origin master 

传送到远程库

5、git pull  

下载库

6、git log

查看历代信息

7 忽略文件夹

首先新建一个1.gitignore文件，使用`mv 1.gitignore .gitignore`重命名

在里面添加忽略项，每行一个，注意，如果是文件夹，不仅要写

/bin

还要写

/bin/

用来忽略文件夹内的东西

8出现冲突，无法上传

首先pull再push，但是这样会更新到github上的版本，

#下一步准备测试只add .再Pull再commit

注，这样不可以，工作区会删

9checkout恢复

如果修改了某个文件想改回来，因为没有commit，所以只要用git checkout -- filename

注意filename与--之间是有空格的

10git reset恢复

git reset 版本号可以恢复到那个版本，但是可能会出现与github上冲突的情况

值得注意的是git 本地与github上是保持一致的，即使是冲突pull时也会有相关信息。

11如果出现无法提交

首先尝试pull然后尝试git mergetool最后尝试add等重新push操作

因为网站上git只允许多commit记录，不允许缺

12出现无法Pull但是想直接pull网上的代码

git stash
git pull
git stash pop

或者放弃本地修改，直接覆盖之

git reset --hard
git pull

13所以现在能够做到恢复历史版本的方式

1首先reset到想要的版本

2复制改变的文件到旁边的文件夹

3Pull，可能会出现冲突，但是利用12解决

4复制回来，add并且commit

2python dataform
