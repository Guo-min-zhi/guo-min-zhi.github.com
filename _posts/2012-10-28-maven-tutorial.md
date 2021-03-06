---
layout: post
title: Maven Tutorial
categories: [maven, java]
tags: [maven, java]
---

如何在windows环境下快速搭建maven项目：

### 1. 下载maven

解压到C:\Program Files\apache-maven-2.2.1

### 2. 配置Maven环境

环境变量 -> 系统变量 -> 新建 -> M2_HOME (C:\Program Files\apache-maven-2.2.1)

环境变量 -> 系统变量 -> 找到Path -> 编辑 -> ;C:\Program Files\apache-maven-2.2.1

然后，打开命令提示符(cmd)，检查Maven环境是否配置成功：

![maven]({{ site.url }}/assets/img/mvn.png)

### 3.  修改Maven仓库

Maven仓库用于存放我们在项目中用到的所有jar包，其配置在conf目录下的settings.xml文件中。

![maven1.png]({{ site.url }}/assets/img/mvn1.png)

一般情况下使用默认的目录即可，如果想更改目录，直接修改<localRepository>标签中的内容即可。

### 4. 创建Maven项目

使用cmd进入相应的文件目录下，直接输入命令即可。

创建普通项目：mvn archetype:generate -DgroupId=com.maven.test -DartifactId=hello -DpackageName=com.maven.test -Dversion=1.0

创建web项目：mvn archetype:generate -DgroupId=com.maven.test -DartifactId=mywebapps  -DarchetypeArtifactId=maven-archetype-webapp -Dversion=1.0

### 5. 编译项目

在命令提示符下，进入我们创建的项目目录，mvn clean compile，进行编译。使用mvn eclipse:eclipse 生成eclipse的目录结构。

### 6. 导入eclipse

打开eclipse工具，需要先配置一下maven仓库的路径：

Window -> Preferences -> Java  -> Build Path -> Classpath Variables -> New -> Name : M2_REPO -> Path : C:\Users\Guo\.m2\repository

我的仓库路径是默认的。

***

接着import一下项目就可以了。