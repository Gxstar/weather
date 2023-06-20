from flask import Flask,render_template,request
import requests
import view

app = Flask(__name__)

# 主页入口
@app.route('/')
def home(): 
    key='6c5dc70b8be20a22302470f4576304b4'
    if request.remote_addr=='127.0.0.1':
        ip='118.120.121.59'
    else:
        ip=request.remote_addr
    url='https://restapi.amap.com/v3/ip?ip='+ip+'&key='+key
    info=requests.get(url)
    wea={
        'weather': 'sun',
        'wind': 6,
        'wet': 15,
        'ip': ip
    }
    return render_template('index.html',wea=wea)



if __name__ == '__main__':
    app.debug=True
    app.run(use_reloader=False)

