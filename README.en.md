# 🔥 Kuaishou Data Collector - GUI, Ready to Use, Free Trial Available

[![Download Latest Version](https://img.shields.io/badge/Download-Latest_Release-brightgreen)](https://github.com/mashukui/kuaishou_one_spider/releases/)

[简体中文](README.md) | **English**

---

Hi, I'm [@Mage Python Talk](https://github.com/mashukui), a 10+ year software engineer, now working full-time as an independent developer.

Kuaishou is one of China's leading short-video social platforms, known for its unique inclusive traffic distribution mechanism and vast creator ecosystem, covering users from first-tier cities to lower-tier markets. Whether it's trend tracking, content analysis, or audience insights, Kuaishou holds rich data value.

To harness this data, I built **"Kuaishou One Spider"** — a Python-based desktop tool that integrates three core data collection functions: **keyword search & comment collection**, **creator homepage post collection**, and **UID/link conversion**, providing an all-in-one data acquisition solution for Kuaishou.

---

## 🎯 Use Cases

- **Customer Acquisition** — Identify potential customers from comment sections under hot posts in target industries or brands
- **Sentiment Analysis** — Collect Kuaishou topic data for social media monitoring, brand reputation research, etc.
- **Content Research** — Analyze trending content styles and viral topics for content strategy
- **Operations Collaboration** — Convert between different link/UID formats for cross-tool and cross-platform data workflows

---

## ✨ Features

### 1️⃣ Keyword Search & Comment Collection

Search posts by keyword, then scrape comments at scale.

**Collected fields (10):**

| Field | Description |
|-------|-------------|
| Video ID | Unique identifier of the post |
| Video Link | Direct link to the video |
| Page | Pagination number |
| Username | Commenter's nickname |
| User ID | Commenter's unique ID |
| User Profile | Commenter's homepage link |
| Comment Time | Timestamp of the comment |
| Likes | Like count on the comment |
| Comment Level | Thread level (top-level/reply) |
| Comment Content | The comment text |

> Each page auto-saves to CSV (1-2s interval), preventing data loss on unexpected interruptions.

---

### 2️⃣ Creator Homepage Post Collection

Enter a creator's homepage link to scrape all their posts.

**Collected fields (12):**

| Field | Description |
|-------|-------------|
| Page | Pagination number |
| Author Name | Creator's nickname |
| UID | Creator's unique ID |
| Author Link | Creator's profile link |
| Video Title | Title of the post |
| Video Tags | Topic/hashtag labels |
| Video Link | Direct link to the post |
| Publish Time | When it was posted |
| Duration | Video length in seconds |
| Likes | Like count |
| Favorites | Favorite/bookmark count |
| Views | View count |

✅ Also supports **downloading video MP4 files** from the homepage for offline archiving.

---

### 3️⃣ Post Detail Scraper

Dive deeper into individual posts for richer metadata.

**Collected fields (18):**

| Field | Description |
|-------|-------------|
| Keyword | Search keyword |
| Video ID | Unique post identifier |
| Video Link | Direct post link |
| Video Title | Title of the post |
| Topic Tags | Hashtags associated |
| Author Name | Creator's nickname |
| Author UID | Creator's unique ID |
| Author Profile | Creator's homepage link |
| Publish Time | When it was published |
| Duration | Video length in seconds |
| Likes | Like count |
| Views | View count |
| Comments | Comment count |
| Favorites | Favorite count |
| Shares | Share count |
| IP Location | Content IP location |
| Cover Image | Cover image URL |
| Video Direct Link | Direct video file URL |

✅ Also supports **downloading the video MP4 file** for each post.

---

### 4️⃣ UID / Link Conversion

Convert between different Kuaishou link formats and UIDs — useful when handling links from various sources.

| Input | Output |
|-------|--------|
| kuaishou.com/profile/xxxx | User UID |
| kuaishou.com/short-video/xxx | Video ID |
| Share link | Standard format |
| UID | Profile link |

---

## 🖥️ System Requirements

- **Platform**: Windows / macOS
- **Python Environment**: Not required — no setup needed
- **Network**: Internet connection required

---

## 🚀 Quick Start

1. **Download** the latest release from the [Releases page](https://github.com/mashukui/kuaishou_one_spider/releases/)
2. **Configure Cookie** using the built-in Cookie Tool (automatic — no manual copying needed)
3. **Launch** the app, click **Login** to authenticate
4. **Select a module**: Search & Comment / Homepage Scraper / Link Converter
5. **Set parameters** (keyword, time range, target link, etc.)
6. Click **Start** and watch the real-time progress
7. Done! Check the CSV file or downloaded videos in current folder

### Cookie Setup (One-Time)

The software includes a **Cookie Tool** that automates cookie retrieval — no more manual header hunting. It writes your cookie directly to `cookie.txt` in the software directory.

![Cookie Tool](https://camo.githubusercontent.com/f42d0c66a0ebdcb2c5786dcf88edda87e7dc2324c41a67206e76df43ebfd769d/68747470733a2f2f66696c65732e6d646e6963652e636f6d2f757365722f33323131302f30633936363239332d313033372d346162382d613533622d3630646136343833343165352e6a7067)

---

## 🧩 Technical Architecture

Built entirely in Python with the following modules:

| Module | Purpose |
|--------|---------|
| `tkinter` | GUI interface |
| `requests` | HTTP requests |
| `json` | API response parsing |
| `pandas` | Data cleaning & CSV export |
| `logging` | Activity logging |

### Key Code Snippets

**Send request & parse data:**

```python
r = requests.get(url, headers=h1, params=params)
json_data = r.json()
```

**Iterate comment data:**

```python
for data in json_data['rootCommentsV2']:
    content = data['content']
    content_list.append(content)
```

**Save to CSV:**

```python
df = pd.DataFrame({
    'Video ID': video_id,
    'Video Link': 'https://www.kuaishou.com/short-video/' + video_id,
    'Page': page,
    'Username': author_name_list,
    'User ID': author_id_list,
    'User Profile': author_link_list,
    'Comment Time': create_time_list,
    'Likes': like_count_list,
    'Comment Level': comment_level_list,
    'Comment Content': content_list,
})
if os.path.exists(self.result_file2):
    header = False
else:
    header = True
df.to_csv(self.result_file2, mode='a+', index=False, header=header, encoding='utf_8_sig')
```

**Logging configuration:**

```python
def get_logger(self):
    logger = logging.getLogger(__name__)
    formatter = "[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s"
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        sh = logging.StreamHandler()
        log_formatter = logging.Formatter(formatter, datefmt="%Y-%m-%d %H:%M:%S")
        info_file_name = time.strftime("%Y-%m-%d") + ".log"
        info_handler = TimedRotatingFileHandler(
            filename="./logs/" + info_file_name,
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

---

## ⚠️ Important Notes

1. **Windows / Mac** — both supported, no programming environment required
2. Uses **API-based** data collection (not browser simulation / RPA), resulting in higher stability
3. Auto-saves CSV after each page — prevents data loss from unexpected interruptions (1-2s interval between pages)
4. Detailed logs recorded during runtime for troubleshooting
5. **One device, one license** — each activation code works on a single machine only
6. Only **one instance** allowed per computer (no multi-instance)

---

## 💰 Pricing

| Plan | Duration | Price | Best For |
|------|----------|-------|----------|
| 🟢 **Daily** | 1 day | **¥39** | Trial / one-time use |
| 🔵 **Monthly** | 1 month | **¥149** | Short-term projects |
| 🟠 **Quarterly** | 3 months | **¥399** | Medium-term needs |
| 🔴 **Yearly** | 1 year | **¥799** | Long-term usage |

🔑 **Purchase & Activate:** [https://mgnb.pro/product/kuaishou](https://mgnb.pro/product/kuaishou)

> License mechanism: One activation code binds to one computer (device-locked) to prevent unauthorized resale.

---

## 📹 Demo Video

Watch the full workflow here: [【Tool Demo】Kuaishou One Spider](https://mp.weixin.qq.com/s/bqP01MKMjP9oazzW0gkh0Q)

---

## 📦 Download

> **Official WeChat Account**: Follow "老男孩的平凡之路" and reply "爬快手聚合软件" to get the latest version.
>
> Or download directly from: [GitHub Releases](https://github.com/mashukui/kuaishou_one_spider/releases/)

![QR Code](https://private-user-images.githubusercontent.com/228842838/590187614-5723e3c6-6c6f-4fc0-8adf-320e72d8c05b.png)

---

## 📄 License

This software is developed and maintained by [@马哥python说](https://github.com/mashukui). Regular updates and long-term support provided.

---

*Built with ❤️ by an indie developer. For questions or feedback, open an issue or reach out via the official WeChat account above.*
