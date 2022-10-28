# 创建应用实例
import os
from wxcloudrun import app


# 启动Flask Web服务
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)