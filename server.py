from ast import keyword
from asyncio.windows_events import NULL
from gettext import NullTranslations
from flask import Flask, redirect, render_template, request, jsonify, url_for
import util

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    return render_template('app.html')


@app.route('/download', methods=['POST','GET'])
def download():
    if (request.method=="POST"):
        url=request.form['url']
        title = util.title(url)
        thumbnail = util.thumbnail(url)
        keyword = util.keyword(url)
        # util.download(url)
        return f'<h1>{title}</h1><div><a href={thumbnail} download><img src={thumbnail} float="center" style="width:640px;height:360px;"></div></a><label for="Keywords"><h2>Keywords:</h2></label><h3><textarea id="w3review" name="w3review" rows="4" cols="50">{keyword}</textarea></h3><br><br>'
    else:
        return render_template('app.html')        

if __name__ == "__main__":
    app.run(debug=True)