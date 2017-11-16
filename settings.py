from os import getenv
from tornado.options import define

define("port", default=getenv('PORT', 8900), help="run on the given port",
       type=int)
define("filename", default="yleisviesti-latest.json", help="the served file",
       type=str)
define("filepath", default="archive/", help="path for backup files", type=str)
