python 与 c/c++ 混合编程之 cython
=================================

####1. 什么是Cython
**`[Cython] is a programming language that makes writing C extensions for the Python language as easy as Python itself.`**
Cython是一门编程语言，用它可以为python语言写C扩展，写法就和写python一样容易。它的目的是想成为python的一个替代解决方案，拥有高效、面对对象、函数式编程，动态等特性。它的主要特色就是静态声明变量；cython的源码会翻译成完美的c/c++代码和python的扩展模块。利用cython的python程序将会拥有c的执行效率和python的编程效率。

####2.windows下使用mingw32编译安装cython

    git clone  git@github.com:cython/cython.git
    cd cython
    python setup.py install

如果没有安装vs运行环境，一般会出现‘error:Unable to find vcvarsall.bat’的错误

如何利用mingw32 解决这个问题

+ 在Python的安装目录：Python27\Lib\distutils 下新建一个文件，文件名为：distutils.cfg   

        [build]
        compiler = mingw32
        [build_ext]
        compiler = mingw32

然后，我们重新回到Cython文件下，运行安装命令

        python setup.py install

这样即可安装成功

####3. cpython demo
**windows上编译失败，还需要解决**
[demo](http://blog.perrygeo.net/2008/04/19/a-quick-cython-introduction/)