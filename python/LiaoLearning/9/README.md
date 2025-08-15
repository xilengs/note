## 模块
为了编写可维护的代码，把函数分组，分别放到不同的文件里。

在python里，一个.py文件就是称之为一个模块

使用模块提高了代码的可维护性，还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以在不同的模块中。

为了避免模块名冲突，python又引入了按目录来组织模块的方法，称之为包。

每个包目录下都会有一个**__init__.py**的文件，这个文件<mark>必须存在</mark>,否则python就会把这个目录当成是普通目录，而不是一个包。
__init__.py可以是空文件，也可以有python代码。

- mycompany\
  - web\
      - \_\_init__.py
      - utils.py
      - www.py
  - \_\_init__.py
  - abc.py
  - utils.py

文件www.py的模块名就是mycompany.web.www,两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils
