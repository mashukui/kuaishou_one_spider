import csv
import datetime
import json
import os
import random
import sys
import threading
import time
import requests
from tkinter import messagebox


class KuaishouPostSpider:
    """快手用户主页作品采集模块

    负责：
    1. 遍历用户链接列表
    2. 分页获取用户发布的视频列表
    3. CSV输出和可选视频下载
    """

    def __init__(self, user_link_list, top_num, down_tag, txt_msglist, logger):
        self.txt_msglist = txt_msglist
        self.logger = logger
        self.describe = []
        self.cookie = self.get_cookie()
        self.user_link_list = user_link_list
        self.top_num = int(top_num)
        self.down_tag = down_tag
        self.wait_sec = self.get_config_pub()
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.result_file = '快手博主视频_{}.csv'.format(now)

    def tk_show(self, context):
        self.logger.info(context)
        self.txt_msglist.delete('1.0', 'end')
        self.describe.append(context)
        self.txt_msglist.insert('insert', '\n'.join(self.describe))
        self.txt_msglist.see("end")

    def _safe_showerror(self, title, message):
        try:
            if threading.current_thread() is threading.main_thread():
                self.txt_msglist.bell()
                messagebox.showerror(title, message)
            else:
                self.txt_msglist.after(0, lambda: (self.txt_msglist.bell(), messagebox.showerror(title, message)))
        except Exception as e:
            self.logger.error(f'[safe_showerror] {e}')

    def _safe_showinfo(self, title, message):
        try:
            if threading.current_thread() is threading.main_thread():
                self.txt_msglist.bell()
                messagebox.showinfo(title, message)
            else:
                self.txt_msglist.after(0, lambda: (self.txt_msglist.bell(), messagebox.showinfo(title, message)))
        except Exception as e:
            self.logger.error(f'[safe_showinfo] {e}')

    def _reset_session(self):
        self.session = requests.Session()

    def _request(self, url, method='GET', headers=None, params=None, data=None, timeout=30):
        return None

    def trans_date(self, v_timestamp):
        timeArray = time.localtime(v_timestamp / 1000)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def get_cookie(self):
        """[专有代码已移除] 从 cookie.txt 读取cookie"""
        return ""

    def get_config_pub(self):
        try:
            with open('config_pub.json', 'r') as file:
                text = json.load(file)
            wait_sec = text['wait_sec']
            if wait_sec < 1:
                self.tk_show('\n等待时长需至少1秒，请重新配置！')
                exit(1)
            self.tk_show(f'\n读取config_pub成功, 等待间隔是:{wait_sec}s')
        except Exception as e:
            wait_sec = ''
            self.tk_show('\n读取config_pub失败！请检查config_pub.json')
            self.tk_show(str(e))
            exit(1)
        return wait_sec

    def init_csv(self, csv_header):
        with open(self.result_file, 'a+', encoding='utf_8_sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)
        self.tk_show('csv初始化完成')

    def down_ks_video(self, v_dir_name, video_url, video_id):
        """[专有代码已移除] 下载快手视频文件"""
        pass

    def get_user_post(self):
        """[专有代码已移除] 采集用户主页作品列表"""
        self.tk_show('\n[专有代码已移除] 用户作品采集功能需要专有实现')
        self._safe_showinfo('提示', '用户作品采集功能需要专有实现，未包含在本开源版本中')
