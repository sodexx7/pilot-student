## 进入编程世界的第一课

这里是存放学习反馈（*Voice of Readers*）的地方，你的感想、心得或者抱怨都可以写好放在这个目录下。

学习过程中的一些想法 start 20200206

* p1-2-structure-1
    1. 同类型的数据之间才可以发生一些运算，如数字之间可以加减乘除；字符串之间可以尽心拼接，判断是某字符串是否属于另一个字符串；布尔之间可以进行逻辑运算；

    2. 有关程序中变量概念的深化
        1. 变量是对数据的抽象，用来存放数据
        2. 具体的基本数据可以根据函数typeof()判断是否是某一数据类型，变量只要被赋值后，也可以判断是哪一种数据类型，并且可以根据赋值语句改变变量指引的具体值，从而可以改变变量的数据类型
        3. 删除变量命令 del 变量名
        4. python支持多个变量同时赋值，Java则只支持单个变量赋值
        5. 与之相比，java是强变量，python是弱变量，为变量赋值之前，不需要为变量指定类型，同时js也是弱变量，赋值之前，不需要指定变量类型

* p1-3-structure-2.
    1. 操作符与函数 操作符与函数 是同类型数据之间交互的方式
        1. 精度损失：**补充：整数乘以浮点数，如果结果为浮点数，则有精度损失，如100*0.18= 18 10*0.18= 1.7999** 经测试，该情况在Java中也存在
        2. Python中大小操作符不仅可以用来比较数值类型的数据，也可以用来比较字符串等其他类型的数据，而Java中仅仅可以比较数值类型的数据
        3. [小数在计算机里是以一种近似值的方式存在的](https://www.taowong.com/blog/2018/07/10/principle-of-computer-float-num.html)
        4. 需了解浮点表示误差和规避方法
            * 转换成整数运算
            * 使用函数 保证在一定误差之内
    2. 函数
        * python函数可以返回多个值
        * pthon使用缩进来表示函数代码块，Java中使用大括号来表示的   

* p1-4-structure-3
    1. 逻辑真值与假值 最终能给出一个逻辑真值或假值的东西都叫做逻辑判断，分为如下几类：
        * bool类型的变量或值
        * 大小操作符的比较结果
        * 返回布尔值的函数
        * 上述三种通过逻辑运算符组合起来
        * 万物皆可为bool值，因为 Python 提供了一组规则来判断一个值“相当于”逻辑真还是假，这种定义是在所谓“合理类比”和方便性的基础上做出的，可用函数bool()来判断。可据此提高代码的可读性与简洁性
        * Python 中的几乎任何值都能转换为布尔值 True 或 False，bool() 函数可以告诉我们特定值对应的是逻辑真还是假。

* p1-5-structure-4
    1. 循环与迭代的定义，让我感觉到提出一个定义或者概念的力量。
    2. 列表[]   中的每个数据都可以是任意类型，并且是有序排列的
    3. 迭代器(Iterator) range  **相比较于其他语言，其本身的特色？,此处关联for循环的本质是什么** 
    4. python 没有++表达式？？
* p1-7-oo-1
    1. 软件开发的根本困难在于管理软件系统的复杂度。

* p1-9-oo-3
    1. python 新创建一个对象时，采用调用函数的方式，如f(param1,param2)<f为类名>,其默认会执行其类里面的初始方法__init__(self,param1,param2),而对应Java里面 则是 new f()d 形式，构造时，默认执行构造器方法。**不过Java构造时，可以有多个不同参数的构造器，Python中不知道有没有**
    2. python集成父类采用这种形式:class Cat(Animal): 其中Cat为父类，而Java中采用 extends implements 形式。
    3. Python中以__开头和结尾的方法或者变量，外部最好不要依赖这些方法或者变量。Python也不像Java和C++无私有成员一说。
    4. 彻底搞懂字符集及编码标准，可以多看看这一章，pilot-student/p1-a-string.ipynb
* p1-a-string
    1. [Python str方法](https://docs.python.org/3/library/stdtypes.html#string-methods)
    2. [Python中对UniCode的支持](https://docs.python.org/3/howto/unicode.html) 
    3. str方法都不会改变原来的字符串对象，而是把处理结果作为一个新的字符串返回，我们可以将其赋值给另一个变量然后使用。如capitalize()，upper() 和 lower()，rjust()，ljust() 和 center()，判断字符串是不是具有某种特征：
        * isalpha() 判断字符串里是不是都是字母；
        * isdigit() 判断字符串里是不是都是数字；
        * islower() isupper() 判断字符串是不是全小写或者全大写字母
    4. str后面可能很有用的方法

* p2-1-function-def
    1. [PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
    2. 一个函数可以有多个带缺省值的参数，但有一个限制：所有这些带缺省值的参数只能堆在参数表的最后




TODO
1. [str方法官方文档](https://docs.python.org/3.5/library/stdtypes.html#string-methods)
2. **加强对官方文档的阅读** 如[Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)   
3. 字符与字符的内容有时间可以多看看，发掘下Python里面本身的一些内容
4. 梳理Python语言本身的特性 相比较于其他语言。
