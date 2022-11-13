# 版本控制

## 什么是版本控制

版本控制是一种字啊开发的过程中用于管理我们对文件、目录或工程等内容的修改历史，方便查看更改历史记录，备份以便恢复以前的版本的软件工程技术。

- 实现跨区域多人协同开发
- 追踪和记载一个或者多个文件的历史记录
- 组织和保护你的源代码和文档
- 统计工作量
- 并行开发、提高开发效率
- 追踪记录整个软件的开发过程
- 减轻开发人员的负担，节省时间，同时降低认为错误

简单来说就是用于管理多人协同开发项目的技术。

## 常见的版本控制工具

Git SVN CVS……

## 常用的 Linux 命令

1. cd ：改变目录
2. cd .. :回退到上个目录，直接 cd 进入默认目录
3. pwd ：显示当前所在的目录路径
4. ls(ll) ：都是列出当前目录中的所有文件，只不过 ll 列出的内容更为详细。
5. touch ：新建一个文件 如 touch index.js 就会在当前目录下新建一个 index.js 文件
6. rm ：删除一个文件，rm index.js 就会把 index.js 文件删除
7. mkdir ：新建一个目录，就是新建一个文件夹
8. rm -r ：删除一个文件夹，rm -r demo 删除 demo 文件夹
9. mv ：移动文件 mv index.js demo index.js 是我们要移动的文件 demo 是目标文件夹
10. reset ：重新初始化终端/清屏
11. history ：查看命令历史
12. help ：帮助
13. exit ：退出
14. #表示注释

## Git 配置

查看配置 `git config -l`
查看不同级别的配置文件

```
#查看系统config
git config --system --list
#查看当前用户（global）配置
git config --global --list
```

Git 相关的配置文件：

1. Git\etc\gitconfig ：
   Git 安装目录下的 gitconfig --system 系统级

2. C:\Users\Administrator\ .gitconfig  
   只适用于当前登录用户的配置 --global 全局

### 设置用户名与邮箱（用户标识，必要）

当安装 Git 后首先要做的事情是设置你的用户名和 email 地址。

```
git config --global user.name "用户名"
git config --global user.email "邮箱"
```

### Git 基本理论

Git 本地有三个工作区域：工作目录（working directory ） 暂存区（Stage/Index） 资源库（Repository 或 Git Directory），如果在加上远程的 git 仓库（Remote Directory）就可以分为四个工作区域。

- Workspace：工作区，就是平时存放项目代码的地方
- Index/Stage：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息
- Repository：仓库区（或本地仓库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中 HEAD 指向最新放入仓库的版本
- Remote：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换

![alt流程](https://mmbiz.qpic.cn/mmbiz_png/uJDAUKrGC7Ksu8UlITwMlbX3kMGtZ9p0NJ4L9OPI9ia1MmibpvDd6cSddBdvrlbdEtyEOrh4CKnWVibyfCHa3lzXw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

本地的三个区域确切的说应该是 git 仓库中 HEAD 指向的版本：

![altHEAD指向的版本](https://mmbiz.qpic.cn/mmbiz_png/uJDAUKrGC7Ksu8UlITwMlbX3kMGtZ9p0icz6X2aibIgUWzHxtwX8kicPCKpDrsiaPzZk04OlI2bzlydzicBuXTJvLEQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

- Directory :使用 Git 管理的一个目录，也就是一个仓库，包含我们的工作空间和 Git 的管理空间。
- Workspace ：需要通过 Git 进行版本控制的目录和文件，这些目录和文件组成了工作空间。
- .git ：存放 Git 管理信息的目录，初始化仓库的时候自动创建。
- Index/Stage ：暂存区，或者叫待提交更新区，在提交进入 repo 之前，我们可以把所有的更新放在暂存区。
- Local Repo ：本地仓库，一个存放在本地的版本库；HEAD 会只是当前的开发分支（branch）。
- Stash ：隐藏，是一个工作状态保存栈，用于保存/恢复 workspace 中的临时状态。

#### 工作流程

git 的工作流程一般是这样的：

1. 在工作目录中添加，修改文件；
2. 将需要进行版本管理的文件放入暂存区域；
3. 将暂存区域的文件提交到 git 仓库。

因此，git 管理的文件有三种状态：modified（已修改），staged（已暂存），committed（已提交）

![alt工作流程图](https://mmbiz.qpic.cn/mmbiz_png/uJDAUKrGC7Ksu8UlITwMlbX3kMGtZ9p09iaOhl0dACfLrMwNbDzucGQ30s3HnsiaczfcR6dC9OehicuwibKuHjRlzg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

### git 项目搭建

#### 创建工作目录与常用指令

工作目录（workspace）一般就是你希望 Git 帮助你管理的文件夹，可以是你项目的目录，也可以是一个空目录，建议不要有中文。
![alt命令](https://mmbiz.qpic.cn/mmbiz_png/uJDAUKrGC7Ksu8UlITwMlbX3kMGtZ9p0AII6YVooUzibpibzJnoOHHXUsL3f9DqA4horUibfcpEZ88Oyf2gQQNR6w/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

#### 本地仓库搭建

创建本地仓库的方法有两种：一种是创建全新的仓库，另一种是克隆远程仓库。

1. 创建全新的仓库，需要用 GIT 管理的项目的根目录执行：

```
# 在当前目录新建一个git代码库
$ git init
```

2. 执行后可以看到，仅仅在目录多出了一个.git 目录，关于版本等的所有信息都在这个目录里面。

#### 克隆远程仓库

1. 另一种方式是克隆远程目录，由于是将远程服务器上的仓库完全镜像一份至本地！

```
# 克隆一个项目和它的整个代码历史（版本信息）
$ git clone [url]
```

2. 去 Gitee 或者 github 上克隆一个测试！

### Git 文件操作

#### 文件的四种状态

版本控制就是对文件的版本控制，要对文件进行修改、提交等操作，首先要知道文件当前在什么状态，不然可能会提交了现在还不想提交的文件，或者要提交的文件没提交上

- untracked :未跟踪，此文件字啊文件夹中，但并没有加入到 git 库，不参与版本控制，通过 git add 状态变为 staged
- unmodify ：文件已经入库，未修改，即版本库中的文件快照内容与文件夹中完全一致，这种类型的文件有两种去除，如果它被修改，而变为 modified。如果使用 git rm 移出版本库，则成为 untracked 文件
- modified ： 文件已修改，仅仅是修改，并没有进行其他的操作，这个文件也有两个去处，通过 git add 可进入暂存 staged 状态，使用 git checkout 则丢弃修改过，返回到 unmodify 状态，这个 git checkout 即从库中取出文件，覆盖当前修改！
- staged：暂存状态，执行 git commit 则将修改同步到库中，这时库中的文件和本地文件又变为了一致，文件为 Unmodify 状态。执行 git reset HEAD filename 取消暂存，文件状态为 Modified

#### 查看文件状态

可以通过以下命令可以查看文件的状态

```
#查看指定文件状态
git status [filename]

#查看所有文件状态
git status

#添加所有文件到暂存区
git add .

# 提交暂存区中的内容到本地仓库
git commit -m "消息内容"
```

#### 忽略文件

有些时候我们不想把某些文件纳入版本控制中，比如数据库文件，临时文件，设计文件等
在主目录下建立“.gitignore”文件，此文件有如下规则：

1. 忽略文件中的空行或以井号（#）开始的行将会被忽略。
2. 可以使用 Linux 通配符。例如：星号（\*）代表任意多个字符，问号（？）代表一个字符，方括号（[abc])代表可选字符范围，大括号({string1,string2,……})代表可选的字符串等。
3. 如果名称的最前面有一个感叹号（！），表示例外规则，将不被忽略。
4. 如果名称的最前面是一个路径分隔符（/），表示要忽略的文件在此目录下，而子目录中的文件不忽略。
5. 如果名称的最后面是一个路径分隔符（/），表示要忽略的是此目录下改名称的子目录，而非文件（默认文件或目录都忽略）。

```
# 为注释
*.txt  #忽略所有 .text结尾的文件，这样的话上传就不会被选中！
！lib.txt  #但lib.txt除外
/temp   #仅忽略根目录下的TODO文件，不包括其他目录temp
build/   #忽略build/目录下的所有文件
doc/*.txt  #会忽略doc/notes.txt  但不包括doc/server/arch.txt
```
##  GIT分支
git分支中常用指令：
```
# 列出所有本地分支
git branch

# 列出所有远程分支
git branch -r

# 新建一个分支，但依然停留在当前分支
git branch [branch-name]

# 新建一个分支，并切换到该分支
git checkout -b [branch]

# 合并指定分支到当前分支
$ git merge [branch]

# 删除分支
$ git branch -d [branch-name]

# 删除远程分支
$ git push origin --delete [branch-name]
$ git branch -dr [remote/branch]
```
