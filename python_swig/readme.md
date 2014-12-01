
>要点1：
将swig接口文件编译成与pyhton对于的c文件  
        
        swig -python mytest.i

>要点2：
将c文件编译成pyd文件
    
        python setup.py build

>要点3：
使用makefile编译

        cd api
        mingw32-make
这样在当前目录就会生成一个_mytest.pyd和mytest.py 这两个文件共同构成一个完整的python库   


> 如何测试

        python test.py
