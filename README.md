# test
测试git使用
1.本地仓库初始化成git仓库
使用命令 git init

2.再本地仓库中设置远程地址
远程仓库地址可以在GitHub中复制
git remote add origin https://github.com/你的用户名/你的仓库名.git

3.将本地仓库内容推送到GitHub
低版本git初始化仓库后主分支名称master，最新版本git主分支名称已经改成了main，这时远程推送时会有报错：error: src refspec master does not match any

解决问题：
修改本地主分支名称
git branch -m master main

4.github验证身份

5.继续推送本地提交


