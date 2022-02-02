from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return render_template("kontakt.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect('/mypage/contact')

@app.route('/mypage/me')
def me():
    return render_template("omnie.html")