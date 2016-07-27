# -*- coding: UTF-8 -*-
import smtplib

from email.mime.text import MIMEText
mail_host="smtp.163.com"  #设置服务器
mail_user="godblesshuang"    #用户名
mail_pass="jxbm_163"   #口令
mail_postfix="163.com"

def send_mail(receiver,sub,content):
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content,_subtype='html',_charset='utf8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = receiver
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, receiver, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail("huangyl_chn@163.com","SDCS jobs news","<a href=\"http://sdcs.sysu.edu.cn/?p=6185\">北京航天长峰科技工业集团有限公司广东分公司实习生招聘</a> 2016-07-21"):
        print "发送成功"
    else:
        print "发送失败"