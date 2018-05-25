# code-snippets-python

## 为什么要收集这些代码

下次用起来方便。

## 环境配置

### 安装 Conda

Linux

```
$ wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
$ bash Miniconda2-latest-Linux-x86_64.sh
```

macOS

```
$ wget https://repo.continuum.io/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
$ bash Miniconda2-latest-MacOSX-x86_64.sh
```

### 创建和启动虚拟环境

下载代码，并创建虚拟环境

```
$ git clone git@github.com:binderclip/code-snippets-python.git

$ conda env create -f code-snippets-python/environment.yml
$ source activate cspy2
```

### 之后更新虚拟环境

开发环境导出：

```
$ conda env export | grep -v "^prefix: " > environment.yml
```

线上对应更新：

```
$ conda env update -f environment.yml
```

## todo

- [Welcome to the Click Documentation — Click Documentation (5.0)](http://click.pocoo.org/5/)
