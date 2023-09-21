import os
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from config import SECRET_KEY
from config import UPLOAD_PATH

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH  # 適切なアップロードフォルダのパスに変更

class UploadForm(FlaskForm):
    file = FileField('CSVファイルを選択', validators=[DataRequired()])
    submit = SubmitField('アップロード')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data

        # サンプルデータの読み込み
        df = pd.read_csv(file)

        # データの可視化
        plt.hist(df['some_column'])

        # プロットを画像として保存
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)

        # 画像をBase64でエンコード
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('result.html', plot_url=plot_url)
    return render_template('upload.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
