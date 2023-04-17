from flask import Flask, request,render_template,redirect,url_for,send_file
import smtplib
from email.message import EmailMessage
import ssl
import smtplib

from flask import stream_with_context

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        email_sender = 'encilyugo@gmail.com' 
        email_password = 'bjerdubfeauvfvpa' 
        email_receiver = 'liubai1211@126.com' 
        subject = 'New email address submitted'
        email = request.form['email'] 
        name=request.form['name'] 
        message=request.form['message'] 
        body = f"You received a message from portfolio, email address: {email} , name:{name} ,message: {message}"
       

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
        return redirect(url_for('home', _anchor='contact', send=True))
    else:
        send = request.args.get("send")
        return render_template("index.html",send=send)


def download_pdf():
    file_path = 'static/pdfs/Enci_Lyu_CV.pdf'
    return send_file(file_path, attachment_filename='Enci_Lyu_CV.pdf', as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
