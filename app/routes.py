from flask import render_template, flash, redirect
from app import app
from app.forms import GraphForm

@app.route('/')
@app.route('/index')
def login():
    form = GraphForm()
    return render_template('index.html', form=form)

@app.route('/handle', methods=['POST'])
def handle():
    form = GraphForm()
    if form.validate_on_submit():
        flash('request parameters: p1={}, p2={},  p3={}'.format(
            form.para1.data, form.para2.data, form.para3.data))
        # 使用form.form.para1.data就能取到para1的值，然后可以调用具体计算过程
        # 使用flash(...) 是将数据绑定到前端的页面，你不需要绑定的话可以不flash
        # 你可以将生成的图片放入result.html中
    return render_template('result.html')




