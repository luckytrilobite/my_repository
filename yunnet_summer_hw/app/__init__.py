# 初始化檔案

from flask import Flask

# 創建一個flask物件(網站主體
app = Flask(__name__) 

#從app資料夾import route檔案(將路由加進app物件)
from app import route