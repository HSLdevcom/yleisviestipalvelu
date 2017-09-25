from tornado.options import define, options

define("port", default=8900, help="run on the given port", type=int)
define("filename", default="yleisviesti-latest.json", help="the served file", type=str)
define("filepath", default="archive/", help="path for backup files", type=str)
