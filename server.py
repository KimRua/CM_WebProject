from flask import Flask, render_template, request, send_file, session
from flask_cors import CORS
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import os
import WebPage
import MetaClass

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = "werlasdfsd"


# ------------------------------------파일 업로드-------------------------------------
class FileForm(FlaskForm):
    files = FileField(validators=[FileRequired('업로드할 파일을 넣어주세요')])

@app.route('/upload', methods=['GET', 'POST'])
def main_page():
    form = FileForm()
    try:
        userID = session['user']
    except:
        userID = "로그인 해 주세요"
    if form.validate_on_submit():
        WebPage.FileManager.save(form)
        return render_template('check.html', pwd=os.getcwd() + "\\uploads", userID=userID)
    infos = WebPage.FileManager.Trim()
    return render_template('home.html', form=form, infos=infos, userID=userID)

@app.route('/down/<path:filename>')
def down_page(filename):
    return send_file('uploads/' + filename, attachment_filename=filename, as_attachment=True)

@app.route('/del/<path:filename>')
def delete_page(filename):
    WebPage.FileManager.remove(filename)
    return "<script>location.href = \"/upload\";</script>"


# ------------------------------------인공지능 질의응답-------------------------------------
@app.route('/AI', methods=['GET', 'POST'])
def AI():
    if (request.method == 'GET'):
        return render_template('AI.html', string="무엇이 우리를 움직이게 만들까요?")
    elif (request.method == 'POST'):
        jsonArray = WebPage.question.AI_F(request.form['input'])
        return render_template('AI.html', string=str(jsonArray))


# ------------------------------------로그인, 로그아웃-------------------------------------    
@app.route('/login', methods=['GET', 'POST'])
def Login():
    if (request.method == 'GET'):
        return render_template('Login.html')
    elif (request.method == 'POST' and 'loginId' in request.form and 'loginPw' in request.form):
        a, userID = WebPage.database.check(request.form['loginId'], request.form['loginPw'])
        if a == None:
            return "<script>location.href = \"/login\";alert('아이디 혹은 비밀번호가 틀립니다.');</script>"
        else:
            session['user'] = userID
            return "<script>location.href = \"/upload\";</script>"
        
@app.route('/logup', methods=['GET', 'POST'])
def Logup():
    if request.method == 'GET':
        return render_template('Logup.html')
    elif request.method == 'POST':
        Certified = WebPage.database.logup(
            request.form['loginId'], request.form['loginPw'], request.form['auth'])
        if Certified == True:
            return "<script>location.href = \"/login\";</script>"
        elif Certified == False:
            return "<script>location.href = \"/logup\";alert('중복 아이디 or 인증코드 오류');</script>" 
        


# ------------------------------------페이지 라우팅-------------------------------------   
@app.route("/")
def home_page():
    return render_template('CM_Main.html')
@app.route('/introduction')
def introduction():
    return render_template('sub_ex.html')
@app.route('/procect')
def procect():
    return render_template('SubCareer.html')
@app.route('/team')
def team():
    return render_template('Sub_profile.html')
@app.route('/qna')
def qna():
    return render_template('AI.html')


# ------------------------------------챗봇 스킬 서버-------------------------------------   
@app.route('/lunch' , methods=['GET', 'POST'])
def skill():
    return WebPage.skillServer.lunchInfo()

@app.route('/getguide' , methods=['GET', 'POST'])
def getguide():
    return WebPage.skillServer.GetGuideInfo()

@app.route('/setguide' , methods=['GET', 'POST'])
def setguide():
    return WebPage.skillServer.SetGuideInfo()


# ------------------------------------메타클래스-------------------------------------   
MetaClass.setUp(app)
@app.route("/metaclass/test")
def index():
    return render_template("index.html")

# -------------------------------------Recycle--------------------------------
#Recycle.setUp(app)
# ------------------------------------메인함수-------------------------------------  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)