from flask import Flask,render_template,redirect,url_for
from flask_wtf import FlaskForm
from wtforms.fields import RadioField,SubmitField
import random
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

class TrainForm(FlaskForm):
    model = RadioField('模型', validators=[DataRequired()])
    method = RadioField('方法',validators=[DataRequired()])
    submit = SubmitField()

@app.route('/',methods=['POST','GET'])
def train():
    train_form = TrainForm()
    train_form.model.choices = [('1','模型1'),('2','模型2'),('3','模型3')]
    train_form.method.choices = [('1','方法1'),('2','方法2'),('3','方法3')]
    if train_form.validate_on_submit():

        model_choice = train_form.model.data
        method_choice = train_form.method.data
        model_method=[]
        model_method.append(model_choice)
        model_method.append(method_choice)

        return redirect(url_for('train_result', model_method=model_method))

    return render_template('index.html',form=train_form)

@app.route('/train_result/<model_method>')
def train_result(model_method):
    #model_method=[模型序号,方法序号]
    print(model_method)

    result_dic={}

    # 得到结果数据

    # 判断结果是分类还是回归
    result_dic['type']='分类'

    if(result_dic['type']=='回归'):
        result_dic['train_loss'] = [8.8, 8.6, 5.4, 6.2, 3.6, 4.2, 3.8, 2.1, 1.1]
        result_dic['accuracy'] = 0.7
        result_dic['precision'] = 0.83
        result_dic['recall'] = 0.71
        return render_template('train_result.html', result=result_dic)
    elif (result_dic['type'] == '分类'):
        class_number = 3
        result_dic['heatmap']=[]
        #每[行,列,数量]代表预测值
        for i in range(class_number):
            for j in range(class_number):
                result_dic['heatmap'].append([i,j,random.randint(1,100)])
        result_dic['class_number'] = class_number
        print(result_dic)
        result_dic['accuracy'] = 0.7
        result_dic['precision'] = 0.83
        result_dic['recall'] = 0.71
        print(result_dic)
        return render_template('train_result.html', result=result_dic)

if __name__ == '__main__':
    app.run()
