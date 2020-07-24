# import os.path
# from pathlib import Path
#
# wdr = "D:\Python Project\Location Analysis System"
#
# data_folder_dir1 = os.path.join(wdr, "file_storage", "temp")
# data_folder_dir2 = os.path.join("file_storage", "temp")
#
# file_to_open1 = os.path.join(data_folder_dir1, "location-lookup.csv")
# file_to_open2 = os.path.join(data_folder_dir2, "location-lookup.csv")
#
# print("Path", file_to_open1)
# print("Path", file_to_open2)
#
# f1 = open(file_to_open1)
# f2 = open(file_to_open2)
#
# #
# print("f1\n" + f1.readline())
# print("f2\n" + f2.readline())
#
# f3 = os.path.dirname(__file__)
# # data_folder_dir3 = os.path.join(f3, "/file_storage", "/location-lookup.csv")
# # f6 = open(data_folder_dir3)
# #
# # print("f3\n" + data_folder_dir3)
#
# f4 = os.path.abspath(f3)
# print("f4\n" + f4)
#
# d1 = "file_storage\\temp"
# d1 = os.path.join(d1, "location-lookup.csv")
# print(d1)
#
# data_folder6 = Path("file_storage/temp/")
#
# file_to_open6 = data_folder6 / "location-lookup.csv"
#
# print("Relative:", file_to_open6)
# file_to_open6 = os.path.abspath(file_to_open6)
# print("Absolute:", file_to_open6)
# # f = open(fil)
#
# #

import socket

ip = socket.gethostbyname('www.google.com')
print(ip)
