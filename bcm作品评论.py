from requests import Session
# 使用session，调用登录api后将自动在以后的请求中携带cookie
session = Session()
name = input("请输入用户名:")
password_ = input("请输入账号密码:")
# 这段代码属于是账号登陆代码，你第一次登陆后session会自动携带cookie，可以自行删掉，并对其修改
# pid是指用于记录登录的bcm平台，这里默认为社区，可以从bcm的官网js中获取
login_data = {'pid': '65edCTyg',
              'identity': name,
              'password': password_}
res_login = session.post(
    'https://api.codemao.cn/tiger/v3/web/accounts/login', json=login_data)

# 判断是否登录成功
if res_login.status_code == 200:
    print("登录成功")
    aaa = input("请输入作品id")
    awa = input("请输入内容")
    data = {
        'content': awa,
        'emoji_content': ""
    }
    aw_a = session.post("https://api.codemao.cn/creation-tools/v1/works/"+aaa+"/comment",json=data)
    print(aw_a.text)
else:
    print("登录失败/不存在此账号")
