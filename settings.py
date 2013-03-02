# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'

SITENAME = "遠方"
AUTHOR = 'Guominzhi'

DISQUS_SITENAME = 'guominzhi'
GITHUB_URL = 'https://github.com/Guo-min-zhi'
SITEURL = 'http://guo-min-zhi.github.com'
GOOGLE_ANALYTICS = 'UA-36075477-1'
#TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_CLOUD_STEPS = 4
FEED_RSS = 'feeds/all.rss.xml'
#DEFAULT_ORPHANS=3
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY ='Archives, life'
OUTPUT_PATH = '.'

PATH = 'md-blog'

THEME='./pelican-themes/tuxlite_tbs'

LINKS = (
		('天堂皓月', 'http://hackecho.com/'),
		('shikailun的日志', "http://vicdory.com/"),
		)

SOCIAL = (
		('github', 'https://github.com/Guo-min-zhi'),
		('weibo', 'http://weibo.com/ericdream'),
		)
