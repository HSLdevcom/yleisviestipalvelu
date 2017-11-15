from tornado.options import define

define("port", default=8900, help="run on the given port", type=int)
define("filepath", default="archive/", help="path for backup files", type=str)
define("filename", default="yleisviesti-latest.json", help="the served file",
       type=str)
