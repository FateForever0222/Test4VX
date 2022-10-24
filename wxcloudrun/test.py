import os,execjs
def test2():
    #读取js文件
    current_path = os.path.dirname(__file__)
    with open(current_path+'\getUrl.js',encoding='utf-8') as f:
        js = f.read()
    print(js)
    #通过compile命令转成一个js对象
    docjs = execjs.compile(js)
    
    #调用function
    res = docjs.call('main')
    print(res)
    res=docjs.eval('location')
    
    print(res)
te="'baidu.com'"
print(te[1:-1])