### 构造第一个分类器
```python
Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import kNN
>>> group,labels = kNN.createDataSet()
>>> group
array([[1. , 1.1],
       [1. , 1.1],
       [0. , 0. ],
       [0. , 0.1]])
>>> labels
['A', 'A', 'B', 'B']
>>> kNN.classify([0,0],group,labels,3)
'B'
>>>
```
* 出现NameError
```python
>>> reload(kNN)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reload' is not defined
>>> def reload():
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
```
* 以上问题原因：
	1、python3将reload内置函数移到了imp标准库模板中
	2、需运行from imp import进行导入
* 解决后：
```python
>>> from imp import reload
>>> reload(kNN)
<module 'kNN' from 'D:\\360Downloads\\Software\\GitHub\\machine-learning\\2.KNN\\kNN.py'>
>>> datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\360Downloads\Software\GitHub\machine-learning\2.KNN\kNN.py", line 39, in file2matrix
    returnMat[index,:]=listFromLine[0:3] #得到特征变量
ValueError: could not convert string to float: '40920   8.326976    0.953952    3'
>>>
```