# coding: UTF-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)


TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

SITENAME = "遠方"
AUTHOR = 'Guominzhi'
DATE_FORMATS = {
  'en': '%a, %d %b %Y',
}

DISQUS_SITENAME = 'guominzhi'
GITHUB_URL = 'https://github.com/Guo-min-zhi'
SITEURL = 'http://guo-min-zhi.github.com'
GOOGLE_ANALYTICS = 'UA-36075477-1'
#TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_CLOUD_STEPS = 4
FEED_RSS = 'feeds/all.rss.xml'
#DEFAULT_ORPHANS=3
DEFAULT_PAGINATION = 6
DELETE_OUTPUT_DIRECTORY = True
DEFAULT_CATEGORY ='Archives'
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

ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
STATIC_PATHS = ['static',]
