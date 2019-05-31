#!/usr/bin/env python
#coding=utf-8
'''
需要python3环境。需要安装TextBlob模块。

请将需要翻译的srt文件命名为lines.srt，放在本py文件同一目录。srt文件内文样式为：

1
00:00:00,000 --> 00:00:02,000
Test

2
00:00:02,000 --> 00:00:04,680
Hello, Viv! Hello. She sounds like a monster.

请手动去除不符合的样式。尤其需要手动删除文末多余的空行。不允许存在文末空行。

最后将在本目录生成双语字幕 lines_bilingual.srt
'''
import os
from textblob import  TextBlob

#定义字符串翻译函数
def translation(text):
	blob = TextBlob(text)
	return str(blob.translate(to="zh-CN"))

#制造原始字幕列表
f=open('lines.srt','r')
lines=f.readlines()
f.close()
subtitles=[]
flag=1
for line in lines:
	if flag==3:
		subtitles.append(line)
	flag+=1
	if flag>4:
		flag=1
#字幕列表转为字符串，方便翻译函数调用		
text=''
for subtitle in subtitles:
	text=text+subtitle
	
#将翻译后的字符串写入临时文件
f=open('temp.txt','w')
f.write(translation(text))
f.flush()
f.close()

#将临时文件读取为列表
f=open('temp.txt','r')
translated=f.readlines()

#读取原始字幕
f = open("lines.srt", "r")
contents = f.readlines()
contents[-1]=contents[-1]+'\n'
f.close()

#将翻译内容保存到原始字幕当中去
i=j=0
origin_len=len(contents)
while i<=origin_len:
	if (i%4==3):
		contents.insert(i+j, translated[j]+'\n')
		j+=1
	i+=1
	


#结束保存
f = open("lines_bilingual.srt", "w")
contents = "".join(contents)
f.write(contents)
f.flush()
f.close()
#删掉临时文件
os.remove('temp.txt')