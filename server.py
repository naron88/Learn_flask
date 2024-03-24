from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return 'index page'



app.run(debug=True) #debug=True는 코드 수정 후 저장, 웹 새로고침 시 동적으로 보이게 함