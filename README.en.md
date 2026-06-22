# kuaishou_one_spider

> 🔥 Kuaishou data collection tool / Kuaishou crawler GUI, supporting keyword video collection, comment collection, video detail collection, creator profile video collection, video download, CSV export, and link conversion.
>
> 💡 Supports Windows/macOS with no Python environment required. This repository is used for software introduction, release distribution, usage documentation, and issue feedback. The complete source code is not publicly available.
>
> [⬇️Download Latest Release](https://github.com/mashukui/kuaishou_one_spider/releases/) | [🎬Video Demo](https://www.bilibili.com/video/BV1psRfBkEot/) | [💳Purchase Access](https://mgnb.pro/product/kuaishou)

<p align="center">
  <a href="README.md">简体中文 README</a> | <a href="README.en.md">English README</a>
</p>

## 👋 Overview

`kuaishou_one_spider` is a desktop GUI tool designed for Kuaishou data collection scenarios. It combines keyword video collection, comment collection, video detail collection, creator profile video collection, and link conversion into one client. Users do not need to install or configure a Python environment. Download the client, log in, and start using it.

It is suitable for the following scenarios:

| Scenario | Description |
| --- | --- |
| ✅ Lead generation | Collect potential leads from comments under industry, brand, or competitor-related videos |
| ✅ Public opinion analysis | Collect keyword-related videos and comments for hot event tracking, propagation analysis, and reputation analysis |
| ✅ Content research | Analyze popular videos, topic tags, interaction data, and viral content directions |
| ✅ Kuaishou operations | Convert profile links, Kuaishou IDs, uids, and video links between different formats, and archive collected data |

## ⚙️ Features

| Feature | Description | Output |
| --- | --- | --- |
| ✅ Keyword video collection | Search Kuaishou videos by keyword and collect basic video data | CSV |
| ✅ Comment collection | Collect comments from keyword search results or specified video links | CSV |
| ✅ Video detail collection | Collect video details from video links and support video download | CSV, video files |
| ✅ Creator profile video collection | Collect video lists from creator profile links and support video download | CSV, video files |
| ✅ Link and uid conversion | Convert between profile links, Kuaishou IDs, uids, and video links | CSV |
| ✅ Incremental saving | Save data to CSV after each page to reduce data loss caused by interruptions | CSV |
| ✅ Runtime logs | Record runtime logs for troubleshooting | logs files |

## 🚀 Quick Start

1. Open [Releases](https://github.com/mashukui/kuaishou_one_spider/releases/) and download the latest version.
2. Extract the package and run the client for your operating system.
3. Use the built-in cookie helper to configure your cookie.
4. Log in to the software account.
5. Select a collection module and enter a keyword, video link, or profile link.
6. Click "Start" and wait for the collection task to finish.
7. Check the CSV files, video files, and log files in the software directory.

## 💻 Supported Platforms

| Platform | Support |
| --- | --- |
| Windows | Supported. Download and run the Windows client |
| macOS | Supported. Download and run the macOS client |

## 🖼️ Screenshots

### Keyword Video and Comment Collection

Keyword video and comment collection interface:

![Keyword video and comment collection interface](https://files.mdnice.com/user/32110/13464ab4-bbab-4f23-8de0-c54a298496f0.jpg)

Search video result:

![Search videos result](https://files.mdnice.com/user/32110/47514426-3972-4d2b-8f44-06321074ca95.png)

Comment collection result:

![Comments result](https://files.mdnice.com/user/32110/3da2ce78-8520-4516-9d96-5762cd681a1b.png)

### Video Detail Collection

Video detail collection interface:

![Video detail collection interface](https://files.mdnice.com/user/32110/67a28f32-d288-43c2-9107-c01ebc53fbbb.jpg)

Video detail collection result:

![Video detail result](https://files.mdnice.com/user/32110/7f6b8bc9-d409-4f25-aa60-ab62b74cf7df.png)

Automatically downloaded video files:

![Video detail downloaded files](https://files.mdnice.com/user/32110/bbdd074e-7ffa-4d2a-94ab-2133544ee26b.png)

### Creator Profile Video Collection

Creator profile video collection interface:

![Creator profile video collection interface](https://files.mdnice.com/user/32110/f604b457-bf2a-42ae-b412-9518c2cb5d39.jpg)

Creator profile video collection result:

![Creator profile video result](https://files.mdnice.com/user/32110/1bd49107-b206-4de2-9164-c51c9557fce6.png)

Automatically downloaded creator profile video files:

![Creator profile video downloaded files](https://files.mdnice.com/user/32110/815900e6-6fc0-4891-ac10-f0e5ec20b298.png)

### Link and uid Conversion

Convert a profile link to a Kuaishou ID:

![Convert profile link to Kuaishou ID](https://files.mdnice.com/user/32110/4649de6f-36e0-4140-bfaa-e800117e81f3.jpg)

![Profile link to Kuaishou ID result](https://files.mdnice.com/user/32110/1e9da0e4-1426-44ea-b377-308735ff2009.png)

Convert a Kuaishou ID to a profile link:

![Convert Kuaishou ID to profile link](https://files.mdnice.com/user/32110/a2b7808a-3381-4ee6-82eb-5b6dc5bd1d2a.jpg)

![Kuaishou ID to profile link result](https://files.mdnice.com/user/32110/7448e10e-a262-4386-9259-4ef0bd985110.png)

Convert a mobile app video link to a PC video link:

![Convert app video link to PC video link](https://files.mdnice.com/user/32110/3ae828eb-9afc-4dd7-a107-a8b507b4b909.jpg)

![App video link to PC video link result](https://files.mdnice.com/user/32110/f8b59751-21a1-4874-9535-1e1fe126fcfa.png)

## 📊 Output Fields

The software generates different CSV files based on the selected collection module. Since there are many fields, the main field groups are shown first. You can expand the sections below to view the full field lists.

### Search Video Data

- Collection info: keyword, page
- Video info: video title, topic tags, video link, video duration, published time
- Author info: author nickname, author uid, author profile link
- Interaction data: likes, views

<details>
<summary>View full search video fields</summary>

Keyword, page, video title, topic tags, video link, likes, views, video duration in seconds, published time, author nickname, author uid, author profile link

</details>

### Comment Data

- Collection info: video id, video link, page
- Commenter info: user nickname, user id, user profile
- Comment info: comment time, comment likes, comment level, comment content

<details>
<summary>View full comment fields</summary>

Video id, video link, page, user nickname, user id, user profile, comment time, comment likes, comment level, comment content

</details>

### Video Detail Data

- Collection info: keyword, video id, video link
- Video info: video title, topic tags, published time, video duration, IP location, cover link, direct video link
- Author info: author nickname, author uid, author profile link
- Interaction data: likes, views, comments, favorites, shares

<details>
<summary>View full video detail fields</summary>

Keyword, video id, video link, video title, topic tags, author nickname, author uid, author profile link, published time, video duration in seconds, likes, views, comments, favorites, shares, IP location, cover link, direct video link

</details>

### Creator Profile Video Data

- Collection info: page
- Author info: author nickname, uid, author profile link
- Video info: video title, video tags, video link, published time, video duration
- Interaction data: likes, favorites, views

<details>
<summary>View full creator profile video fields</summary>

Page, author nickname, uid, author link, video title, video tags, video link, published time, video duration, likes, favorites, views

</details>

## 🛠️ Technical Notes

The software is developed in Python. Core modules include:

| Module | Purpose |
| --- | --- |
| tkinter | GUI interface |
| requests | API requests |
| json | Response parsing |
| pandas | CSV export |
| logging | Runtime logging |

The software collects data through interface requests and does not rely on browser automation or RPA-style operations. During collection, results are saved by page by default. The request interval is usually about 1-2 seconds, which helps control the collection pace and reduce data loss caused by unexpected interruptions.

## 💰 Pricing

| Plan | Duration | Price | Recommended Usage |
| --- | --- | --- | --- |
| Day pass | 1 day | 39 CNY | Trial use or small one-time tasks |
| Monthly pass | 1 month | 149 CNY | Short-term collection needs |
| Quarterly pass | 3 months | 399 CNY | Medium-term collection needs |
| Yearly pass | 1 year | 799 CNY | Long-term stable use |

Purchase page: [https://mgnb.pro/product/kuaishou](https://mgnb.pro/product/kuaishou)

## 🔐 License and Activation Rules

- The software uses a one-device-one-license mechanism. One license key can only be used on one computer.
- Only one software instance is allowed on a single computer. Multiple concurrent instances are not supported.
- The software is maintained by the author, and future versions will be published through GitHub Releases.

## ❓ FAQ

### Do I need to install Python?

No. The software is packaged as a desktop client. Download the version for your operating system and run it directly.

### What is the cookie used for?

The cookie allows the software to access platform data under your current account session. Please use your own account cookie and keep related files secure.

### Will collected data be lost if the task is interrupted?

The software saves CSV files by page instead of waiting until the whole task is complete. If the task is interrupted, data from completed pages is usually still preserved in the result files.

### Where are result files saved?

By default, result files are saved in the software directory. CSV files, video files, and log files are generated by feature module.

### How much data can it collect?

The actual amount of data depends on the keyword, account status, platform API response, network environment, and collection frequency. It is recommended to set a reasonable collection range and request interval.

### What should I do if an error occurs?

Check the log files under the `logs` directory first. When reporting an issue, please provide:

- Software version
- Operating system
- Feature module used
- Keyword, profile link, or video link entered
- Error screenshot
- Log content around the time when the error occurred

## ⚠️ Compliance Statement

This software is intended only for lawful data analysis, learning, research, and authorized business scenarios. Users are responsible for complying with the target platform's terms of service, privacy policy, and applicable laws and regulations.

Do not use this software for:

- High-frequency, malicious, or destructive requests
- Unauthorized collection, distribution, or sale of sensitive personal information
- Activities that infringe the lawful rights of platforms, creators, or users
- Any other behavior that violates laws, regulations, or platform rules

Users are solely responsible for risks and liabilities caused by improper use.

## 📦 Get the Software

- GitHub Releases: [https://github.com/mashukui/kuaishou_one_spider/releases/](https://github.com/mashukui/kuaishou_one_spider/releases/)
- WeChat official account: `老男孩的平凡之路`
- Reply in the WeChat official account: `爬快手聚合软件`

<img alt="WeChat official account QR code" src="https://github.com/user-attachments/assets/0a2ce639-01ee-4061-a7a4-110b72bdd0ed" />
