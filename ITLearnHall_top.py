# -*-coding: utf-8-*-
# !/usr/bin/env python
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


@app.route('/top', methods=["post"])
def top():
    # x轴数据，可以从数据库，文件，或者随机函数产生
    x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # y轴数据，可以从数据库，文件，或者随机函数产生
    y = [820, 932, 901, 934, 1290, random.randint(1, 1000), random.randint(1, 1000)]
    return jsonify({"x": x, "y": y})


@app.route('/top_echarts')
def top_echarts():
    """
    jquery给echarts给图表赋值
    :return:
    """
    return render_template('top_echarts.html')


@app.route('/dt/top', methods=["post"])
def dt_top():
    # x轴数据，可以从数据库，文件，或者随机函数产生
    x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    # y轴数据，可以从数据库，文件，或者随机函数产生
    y = [820, 932, 901, 934, 1290, random.randint(1, 1000), random.randint(1, 1000)]
    return jsonify({"x": x, "y": y})



@app.route('/dt_echarts')
def dt_echarts():
    """
    定时echarts动态图
    :return:
    """
    return render_template('dt_echarts.html')


@app.route('/')
def index():
    """
    首页
    :return:
    """
    item = {"categories": 123}
    return render_template('index.html', item=item, alarm={"alarm": 100, "fault": 100},
                           y={"company": 100, "dtuCnt": 100, "plcCnt": 100, "dataCnt": 100, "alarm": 100})


if __name__ == '__main__':
    # app.jinja_env.variable_start_string = '[['
    # app.jinja_env.variable_end_string = ']]'
    app.run()
