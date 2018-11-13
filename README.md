# jap2chs_color_classfier

## 中日传统颜色的分类器

[中国传统颜色](http://zhongguose.com)（526种颜色）

[日本传统颜色](http://nipponcolors.com)（250种颜色）

首先使用爬虫分别爬取了中日传统颜色的16进制码(~~比Rgb代码好爬~~)存入文件，然后使用py读取文件将其转换为rgb(list),最后变为numpy的向量。

分割日200+中500= 训练集

日50+中26 = 测试集

---

首次尝试：logistic 回归

结果：训练集0.71428573的准确率，测试集0.34210527多的准确率, __弃__

---

### 二次尝试：网络模型如下：

<img src="https://i.loli.net/2018/11/12/5be979e44da2c.png"/>

<center>  
    <h3>2层线性修正(relu)1层sigmoid</h3>
</center>

#### 结果：

<img src="https://i.loli.net/2018/11/12/5be97cd796fe0.png"/>