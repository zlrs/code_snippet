# code_snippet
代码片段的备忘录

## 三元表达式
在C系语言中，三元表达式的形式如下：
// 如果条件为真，则返回这为x，否则为y
`result = condition ? x : y`

而在python中三元表达式的语法如下：
`result = x if condition else y`

看起来有点别扭，实际上还可以这样写：

`result = (x, y)[condition]` # condition为真时返回y, 假时返回x
```python
In [50]: print((1,0)[True])
0

In [51]: print((1,0)[False])
1
```

作者：nummy
链接：https://www.jianshu.com/p/fcad6f70feec
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

