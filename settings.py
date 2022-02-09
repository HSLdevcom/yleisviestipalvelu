from os import getenv
from tornado.options import define

define("filename", default="yleisviesti-latest.json", help="the served file",
       type=str)
define("filepath", default="archive/", help="path for backup files", type=str)
