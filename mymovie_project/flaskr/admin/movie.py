#
# # -*- coding:utf_8 -*-
# import requests
#
# # weather = requests.get("https://movie.douban.com/trailers")
# # header = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:61.0) Gecko/20100101 Firefox/61.0"}
# # weather = requests.get("https://movie.douban.com/trailers",headers = header)
# #
# # weather.encoding="utf8"
# #
# # print(weather.text)
# # from .import admin
# from flaskr.admin import model
# from flaskr import db
# from bs4 import BeautifulSoup
# #
# with open("newmovie.html",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,features="lxml")
#
# # print(soup.select("li[class='poster']") )
# # print(soup.select("a img") )
#
#
# # w = soup.select("div[class='trailer'] a img")
# # for item in w:
# #     print(item.attrs.get("alt",None))       #-----属性里面的class
# #     print(item.attrs.get("src", None))
#
#
#
# r = soup.select("li img")
# for item in r:
#     title = type(item.attrs.get("alt",None))
#     print(title)       #-----属性里面的class
#     logo = type(item.attrs.get("src", None))
#     print(logo)  # -----属性里面的class
#
#     preview = model.preview(title=title, logo=logo)
#     db.session.add(preview)
#     db.session.commit()
#
