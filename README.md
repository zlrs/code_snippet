# code_snippet
代码片段的备忘录

## 三元表达式
在C系语言中，三元表达式的形式如下：
`result = condition ? x : y  // 如果条件为真，则返回这为x，否则为y`

而在python中三元表达式的语法如下：
`result = x if condition else y`

下面这种写法利用了元组：
`result = (x, y)[condition]  # condition为真时返回y, 假时返回x` 
```python
In [50]: print((1,0)[True])
0

In [51]: print((1,0)[False])
1
```
这之所以能正常工作，是因为在Python中，True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据。
上面的例子没有被广泛使用，而且Python玩家一般不喜欢那样，因为没有Python味儿(Pythonic)。这样的用法很容易把真正的数据与True/False弄混。

另外一个不使用元组条件表达式的缘故是因为在元组中会把两个条件都执行，而 if-else 的条件表达式不会这样。

参考
- https://www.jianshu.com/p/fcad6f70feec
- https://eastlakeside.gitbooks.io/interpy-zh/content/ternary_operators/ternary_operators.html
