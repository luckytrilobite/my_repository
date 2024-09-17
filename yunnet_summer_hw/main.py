# 啟動後端

from flask import Flask
from app import app

# 如果這個檔案在運行
if (__name__ == '__main__'):
    # 啟動網站 監聽所有網路的5000port
    app.run(host="0.0.0.0",port=5000)  