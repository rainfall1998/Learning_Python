from pywebio.input import input, FLOAT,input_group, NUMBER, select
from pywebio.output import put_text, put_code
import pywebio as pw
### utils tools
from datetime import date,timedelta
import time
def checkAge(age):
    if age>50:
        return 'think about retirement ?'
    elif age>35:
        return 'do you have a job ?'
    elif age>18:
        return 'you are in a age full of probability'
    elif age>0:
        return 'you are catched, go home now!'
def set_now_ts(set_value):
    set_value(int(time.time()))

def select_date(set_value):
    with pw.popup('Select Date'):
        pw.put_buttons(['Today'], onclick=[lambda: set_value(date.today(), 'Today')])
        pw.put_buttons(['Yesterday'], onclick=[lambda: set_value(date.today() - timedelta(days=1), 'Yesterday')])


def outputType1(content):
    voce = '\n\n\n\tNo thing is ture ,and every thing is permitted\n\nwhen other men blindly follow the truth，remember:  \n\n'
    voce += '\t\t\t\tNothing is ture\n\nwhen other men are limited by of laws，remember:  \n\n\t\t\tEverything is permitted'
    voce += '\n\n\n'
    pw.output.put_table([['url:www.127.1.2.1'],
    [pw.output.span(voce, col=2)],]  # 'E' across 2 columns
    , header=[pw.output.span('\tmessage\t', row=2), content])  # 'A' across 2 rows

### try function
def bmi():
    height = input("请输入你的身高(cm)：", type=FLOAT)
    weight = input("请输入你的体重(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]

    for top, status in top_status:
        if BMI <= top:
            put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
            break


def basic_try():
    info = input_group("User info",[
    input('Input your name', name='name'),
    input('Input your age', name='age', type=NUMBER)
    ])
    print(info['name'], info['age'])

def text_input():
    info = input(label='Input your age', type=NUMBER, validate=checkAge)#, name='age', required=True)#, help_text='input your name, and get result')
    # pw.output.put_row([None,pw.output.put_column([ None,None,None,None,None, put_code('permission passed'),None]),None])# size='40% 10px 60%'
    content = 'your age is %s,  permission passed ! '%str(0-info+18)
    outputType1(content)
if __name__ == '__main__':
    text_input()