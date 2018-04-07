# AnalystTaoBao

* __Author__ : Jacky Wei
* __Version__  ：0.0.1.20180404_Base

目录：
3.[爬虫](#3)


## 1.综述
+ __基于爬取淘宝网部分商品的信息进行数据挖掘__
+ __基于Hadoop计算平台生态进行数据处理与分析。__

__1. 项目包括以下目标：__
- 商品各个属性与价格的关系
- 商品各个属性与销量的关系
- 数据可视化
- 探究商品开展活动时价格的变动情况

__2. 项目包含两个部分的工作：___
- 构建针对淘宝网部分商品的爬虫，爬取范围：
    1. 女装：
        - 32个类目
        - 每个类目3000件商品
        - 每件商品36个属性
        - 共计96000件商品
        - 共计3456000个属性值
    2. 珠宝：
        - 22个类目
        - 每个类目3000件商品
        - 每件商品31个属性
        - 共计66000件商品
        - 共计2046000个属性值
        
        （以平均每个属性值10个Byte估算，每日数据量大约50MB，10个月总数据量大约10GB）
    
    3. 商品可爬取的属性项：
        - 商品名称
        - 价格
        - 淘宝价
        - 月售出量
        - 收藏数
        - 累计评论数
        - 带图评论数
        - 商品追评数
        - 商品好评数
        - 商品差评数
        - 是否有优惠券
        - 优惠券额度
        - 发货地
        - 是否包邮
        - 是否开展活动
        - 活动名称
        - 上市年份(女装)
        - 上市季节(女装)
        - 衣服类目(女装)
        - 风格(女装)
        - 二级风格(女装)
        - 库存数
        - 卖家信用
        - 半年内动态评分：宝贝与描述相符
        - 半年内动态评分：卖家的服务态度
        - 半年内动态评分：物流服务的质量
        - 商铺最近一周好评
        - 商铺最近一周中评
        - 商铺最近一周差评
        - 商铺最近一月好评
        - 商铺最近一月中评
        - 商铺最近一月差评
        - 商铺最近半年好评
        - 商铺最近半年中评
        - 商铺最近半年差评
        - 爬取日期

- 进行数据挖掘工作
    1. 数据抽样
    2. 数据预处理
    3. 数据探索
    4. 挖掘建模
    5. 对需求、目标进行解答
    
## 2.数据存储设计

## <span id="3">3.爬虫设计</span>

## 4.挖掘算法设计

## 5.版本命名规范
    例：  1.0.3.20180506_Base
    1：主版本号，整体架构发生改变、模块功能有较大改变时修改
    0：次版本号，模块功能局部发生改动、改动造成与以前版本不兼容时修改
    3：修订版本号，Bug修复、功能小幅度变化时修改
    20180506：日期版本号，一旦当日发生变动则需修改
    _Base：阶段版本号，取值包括Base、Alpha、Beta、RC、Release
            Base：功能尚未实现，基础架构阶段
            Alpha：初级版本，此阶段以实现软件功能为主
            Beta ：测试版本，已经消除了严重错误
            RC：相当成熟的版本，与预发布版本相差无几
            Release：发布版本，开发阶段的最终版本
    
    


        