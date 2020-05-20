#numpy函数库基础
* numpy函数库的安装和测试
		遇到问题：命令提示符显示pip版本过低   
		！[](https://github.com/Bonnie0126/machine-learning/raw/master/1.numpy/图1.png)
		升级pip时尝试输入以下命令，均未成功
		！[](https://github.com/Bonnie0126/machine-learning/raw/master/1.numpy/图2.png)
* 调用mat()函数
		1、调用mat()函数将数组转为矩阵  
```Python
>>> randMat=mat(random.rand(4,4))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mat' is not defined
>>> randMat = mat(random.rand(4,4))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mat' is not defined
```
		2、需定义函数（更正错误并注释）
```Python
>>> from numpy import* #将numpy函数库中的所有模块引入当前的命名空间
>>> random.rand(4,4) #构造一个4×4的随机数组
array([[0.15508613, 0.68014446, 0.80366549, 0.84995359],
       [0.24729068, 0.8957386 , 0.11832487, 0.9225267 ],
       [0.50419145, 0.57983692, 0.16539937, 0.95869132],
       [0.59709478, 0.87602441, 0.72855879, 0.73231783]])
>>> randMat = mat(random.rand(4,4)) #调用mat函数将数组转为矩阵
>>> randMat.I #.I实现矩阵求逆运算
matrix([[  3.99841146,   3.03528513,  -2.79130492,  -2.55738292],
        [-33.24932947, -18.19987656,  25.26105156,  15.39271712],
        [ 54.19781438,  30.8000216 , -42.46529405, -23.94401833],
        [-13.42372787,  -8.69647452,  11.58044672,   6.54639084]])
```
		3、矩阵逆运算 报错(拼写错误)
```Python
>>> invRandMat = randMat.I #存储逆矩阵
>>> randNat*invRandMat #矩阵乘法  生成单位矩阵
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'randNat' is not defined
下方已解决报错问题
>>> randMat*invRandMat
matrix([[ 1.00000000e+00,  8.88178420e-16, -1.77635684e-15,
          0.00000000e+00],
        [-1.77635684e-15,  1.00000000e+00, -1.33226763e-15,
          0.00000000e+00],
        [ 1.77635684e-15,  2.66453526e-15,  1.00000000e+00,
         -8.88178420e-16],
        [ 0.00000000e+00, -8.88178420e-16, -2.66453526e-15,
          1.00000000e+00]])
```
		4、求误差值 生成单位矩阵
```Python
>>> myEye=randMat*invRandMat
>>> myEye - eye(4) #求误差值 eye(4)生成4×4单位矩阵
matrix([[ 0.00000000e+00,  8.88178420e-16, -1.77635684e-15,
          0.00000000e+00],
        [-1.77635684e-15,  8.88178420e-16, -1.33226763e-15,
          0.00000000e+00],
        [ 1.77635684e-15,  2.66453526e-15, -3.55271368e-15,
         -8.88178420e-16],
        [ 0.00000000e+00, -8.88178420e-16, -2.66453526e-15,
         -2.66453526e-15]])
```
