import feedparser, datetime

# 로컬 테스트 시 ssl 인증서 문제 해결용
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# rss 추출
feed = feedparser.parse("https://seongbindb.tistory.com/rss")

# README 양식
markdown_text = """
###  🐱 github stats  

<div id="main" align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=peterica&count_private=true&show_icons=true&theme=radical"
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=peterica&layout=compact"   
        style="height: auto; margin-left: 20px; margin-right: 20px; padding: 10px;"/>
</div>

<br>

### 📕 Latest Blog Posts   

"""

# 최근 블로그 추가
for i in feed['entries'][:10]:
    markdown_text += f"<a href =\"{i['link']}\"> {i['title']} </a> <br>"
    # print(i['link'], i['title'])

# print(markdown_text)
f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
