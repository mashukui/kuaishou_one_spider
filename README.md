# kuaishou_one_spider
> 🔥快手数据采集器 - GUI界面开箱即用，提供日卡试用
>
> 🔧支持功能：✅关键词搜索作品 ✅评论筛选采集 ✅主页作品采集 ✅uid链接转换
>
> [👉🏻点这里下载最新版](https://github.com/mashukui/kuaishou_one_spider/releases/)

<p align="center">
<a href="README.md">简体中文 README</a> | <a href="README.en.md">English README</a>
</p>

# 一、开发背景与效果展示
## 1.1 开发初衷
我是[@马哥python说](https://github.com/mashukui)，一枚10年+程序猿，现全职独立开发。

快手作为国内头部短视频社交平台，凭借其独特的普惠流量分发机制和庞大的创作者生态，覆盖了从一二线到下沉市场的海量用户群体。无论是热点追踪、内容分析还是用户洞察，快手都蕴含着丰富的数据价值。

针对快手平台数据的独特性，我用python独立开发了一款工具“**爬快手聚合软件**”。这款软件将评论采集、达人主页作品采集、链接转换三大功能集于一身，打造一站式的快手数据采集方案。

## 1.2 适用场景
软件适用于以下场景：
- **获客截流**：通过目标行业、品牌热门作品下的评论区，精准定位潜在用户；
- **舆情分析**：采集快手话题数据，用于社媒舆情监控、品牌口碑研究等；
- **内容参考**：分析热门作品的内容风格与爆款话题，为创作方向提供数据支撑；
- **运营协作**：处理不同格式的链接/uid互转，方便跨工具、跨平台的数据流转。

## 1.3 效果展示
### 功能1-采集搜索作品及评论（指定关键词采集作品和评论）
运行界面：
![运行界面-采集搜索作品及评论](https://files.mdnice.com/user/32110/13464ab4-bbab-4f23-8de0-c54a298496f0.jpg)

采集到的作品数据，包括**12个字段**：关键词,页码,视频标题,话题标签,视频链接,点赞数,观看数,视频时长_秒,发布时间,作者昵称,作者uid,作者主页链接。
![结果数据-搜索作品](https://files.mdnice.com/user/32110/47514426-3972-4d2b-8f44-06321074ca95.png)
 
采集到的评论数据，包括**10个字段**：作品id,作品链接,页码,用户昵称,用户id,用户主页,评论时间,评论点赞数,评论级别,评论内容。
![结果数据-评论](https://files.mdnice.com/user/32110/3da2ce78-8520-4516-9d96-5762cd681a1b.png)

 
### 功能2-采集详情作品（指定作品链接采集作品详情）
运行界面：
![运行界面-采集作品详情](https://files.mdnice.com/user/32110/67a28f32-d288-43c2-9107-c01ebc53fbbb.jpg)

采集到的作品详情，包括**18个字段**：关键词,作品id,作品链接,视频标题,话题标签,作者昵称,作者uid,作者主页链接,发布时间,视频时长_秒,点赞数,观看数,评论数,收藏数,转发数,IP属地,封面链接,视频直链。
![结果数据-作品详情](https://files.mdnice.com/user/32110/7f6b8bc9-d409-4f25-aa60-ab62b74cf7df.png)
 
同时支持下载这些链接的视频mp4文件，方便归档，如下：
![视频文件-作品详情](https://files.mdnice.com/user/32110/bbdd074e-7ffa-4d2a-94ab-2133544ee26b.png)

 
### 功能3-采集主页作品（指定主页链接采集作品）
运行界面：
![运行界面-采集主页作品](https://files.mdnice.com/user/32110/f604b457-bf2a-42ae-b412-9518c2cb5d39.jpg)

采集到的主页作品数据包含**12个字段**：页码,作者昵称,uid,作者链接,视频标题,视频标签,视频链接,发布时间,视频时长,点赞数,收藏数,观看数。
![结果数据-主页作品](https://files.mdnice.com/user/32110/1bd49107-b206-4de2-9164-c51c9557fce6.png)

同时支持下载主页中的视频mp4文件，方便归档，如下：
![视频文件-主页作品](https://files.mdnice.com/user/32110/815900e6-6fc0-4891-ac10-f0e5ec20b298.png)

### 功能4-主页链接转快手号
运行界面：
![运行界面-主页链接转ks号](https://files.mdnice.com/user/32110/4649de6f-36e0-4140-bfaa-e800117e81f3.jpg)
 
结果数据：
![结果数据-主页链接转ks号](https://files.mdnice.com/user/32110/1e9da0e4-1426-44ea-b377-308735ff2009.png)
 
### 功能5-快手号转主页链接
运行界面：
![运行界面-ks号转主页链接](https://files.mdnice.com/user/32110/a2b7808a-3381-4ee6-82eb-5b6dc5bd1d2a.jpg)

结果数据：
![结果数据-ks号转主页链接](https://files.mdnice.com/user/32110/7448e10e-a262-4386-9259-4ef0bd985110.png)
 
### 功能6-app端作品链接转pc端作品链接
运行界面：
![运行界面-app端作品链接转pc端作品链接](https://files.mdnice.com/user/32110/3ae828eb-9afc-4dd7-a107-a8b507b4b909.jpg)
 
结果数据：
![结果数据-app端作品链接转pc端作品链接](https://files.mdnice.com/user/32110/f8b59751-21a1-4874-9535-1e1fe126fcfa.png)
 
以上是6个主要功能的介绍。

## 1.4 软件说明
使用前请留意以下几点：
```
1. Windows / Mac 均可直接运行，无需配置编程环境
2. 三大核心功能：① 关键词/作品链接采集评论 ② 主页链接采集作品 ③ uid与链接互转
3. 采用接口协议采集，非模拟浏览器等RPA方案，稳定性更高
4. 采集完成后，自动在当前文件夹生成 csv 结果文件
5. 每采集一页即自动保存一次csv，防止异常中断导致数据丢失（每页间隔 1~2s）
6. 运行过程记录详细日志，方便回溯排查
```

# 二、核心技术
## 2.1 模块分工
软件全部基于 Python 开发，各模块分工如下：
| 序号 | 模块 | 用途 |
| :--- | :--- |:--- |
|1| `tkinter` | 构建gui图形界面 |
|2| `requests` | 发送网络爬虫请求 |
|3| `json` | 解析接口返回的响应数据 |
|4| `pandas` | 清洗并保存csv数据结果 |
|5| `logging` | 记录运行日志 |

## 2.2 代码片段示例
发送请求并解析数据：
```python
# 发送请求
r = requests.get(url, headers=h1, params=params)
# 解析数据
json_data = r.json()
```
遍历评论内容字段：
```python
for data in json_data['rootCommentsV2']:
    # 评论内容
    content = data['content']
    content_list.append(content)
```
保存数据到 csv 文件：
```python
# 保存数据到DF
df = pd.DataFrame(
    {
        '作品id': video_id,
        '作品链接': 'https://www.kuaishou.com/short-video/' + video_id,
        '页码': page,
        '用户昵称': author_name_list,
        '用户id': author_id_list,
        '用户主页': author_link_list,
        '评论时间': create_time_list,
        '评论点赞数': like_count_list,
        '评论级别': comment_level_list,
        '评论内容': content_list,
    }
)
# 保存到csv
if os.path.exists(self.result_file2):  # 如果文件存在，不再设置表头
    header = False
else:  # 否则，设置csv文件表头
    header = True
df.to_csv(self.result_file2, mode='a+', index=False, header=header, encoding='utf_8_sig')
self.tk_show('视频[{}]第{}页已保存到csv: {}'.format(video_id, page, self.result_file2))
```
日志记录模块：
```python
def get_logger(self):
    logger = logging.getLogger(__name__)
    formatter = "[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s"
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        sh = logging.StreamHandler()
        log_formatter = logging.Formatter(formatter, datefmt="%Y-%m-%d %H:%M:%S")
        info_file_name = time.strftime("%Y-%m-%d") + ".log"
        case_dir = "./logs/"
        info_handler = TimedRotatingFileHandler(
            filename=case_dir + info_file_name,
            when="MIDNIGHT",
            interval=1,
            backupCount=7,
            encoding="utf-8",
        )
        logger.addHandler(sh)
        sh.setFormatter(log_formatter)
        logger.addHandler(info_handler)
        info_handler.setFormatter(log_formatter)
    return logger
```

# 三、使用指南
## 3.1 配置 Cookie
启动采集前，先用《cookie小工具》自动配置个人cookie：
![cookie小工具](https://files.mdnice.com/user/32110/0c966293-1037-4ab8-a53b-60da648341e5.jpg)

这样，就会自动写入软件目录下的 cookie.txt 文件，告别繁琐的手动获取过程。
## 3.2 登录软件
将 Cookie 配置好后，启动软件进入登录界面，点击登录完成身份认证。
## 3.3 开始采集
1. 登录成功，选择所需功能模块（搜索作品及评论采集 / 主页作品采集 / 链接转换）
2. 配置参数（关键词、时间范围、目标链接等）
3. 点击「开始执行」，实时查看采集进度
4. 采集完成，在当前文件夹查看 csv 数据文件或已下载的视频
## 3.4 演示视频
软件完整使用流程请参考演示视频：[【工具演示】爬快手聚合软件](https://www.bilibili.com/video/BV1psRfBkEot/)

# 四、付费说明
## 4.1 卡密说明
💰费用如下：
```python
日卡：使用期限1天，39元。适合试用等临时需求
月卡：使用期限1个月，149元。适合短期采集需求
季卡：使用期限3个月，399元。适合中期采集需求
年卡：使用期限1年，799元。适合长期采集需求
```
🔑开通入口：
```
https://mgnb.pro/product/kuaishou
```

## 4.2 一机一码
为防止软件被恶意转卖，采用一机一码机制，一个卡密只能在一台电脑运行、不可多电脑运行。

## 4.3 软件多开
一台电脑仅允许运行一个软件，不支持软件多开。

## 4.4 软件维护
软件由本人独立原创开发，长期维护更新，提供稳定运行。

# 五、软件获取
公众号"**老男孩的平凡之路**"，后台回复"**爬快手聚合软件**"获取最新版软件安装包。[或点这里直达下载](https://github.com/mashukui/kuaishou_one_spider/releases/)
<img width="1406" height="266" alt="二维码-公众号放底部v3" src="https://github.com/user-attachments/assets/0a2ce639-01ee-4061-a7a4-110b72bdd0ed" />

