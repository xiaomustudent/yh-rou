import requests, time, re

sckey = 'I am serve酱 key'
#serve酱未开发

HEADERS = {
    'cookie': 'I am cookie',
    'Host' : 'yaohuo.me',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
def main(url,x):
    pagelist =  requests.get(url,headers=HEADERS)
    pagelist_html = pagelist.content.decode('utf-8')
    rou_ids = re.findall(r'.+?<img src="/NetImages/li.gif" alt="礼"/><a href="/bbs-(.+?).html.+?">',pagelist_html,re.DOTALL)
    # print(rou_ids)
    i = 0+ x -1
    for rou_id in rou_ids :
        introu_id = str(rou_id)
        reqtext = ["吃","吃了","吃吃吃","先吃再说","chi","chi le","吃","吃了","吃吃吃","先吃再说","chi","chi le","吃","吃了","吃吃吃","先吃再说","chi","chi le","吃","吃了","吃吃吃","先吃再说","chi","chi le"]
        data = {
            'face': "",
            'sendmsg': 0,
            'content': reqtext[i],
            'action': 'add',
            'id': introu_id,
            'siteid': 1000,
            'lpage': 1,
            'classid': 177,
            'sid': 'I am sid',
            'g': '快速回复'
        }
        req_url = 'https://yaohuo.me/bbs/book_re.aspx'
        req = requests.post(req_url,headers=HEADERS,data=data)
        req_html = req.content.decode('utf-8')
        repe = req_html.find('请不要发重复内容')
        if repe == 1 :
            data = {
                'face': "",
                'sendmsg': 0,
                'content': reqtext[i+1],
                'action': 'add',
                'id': introu_id,
                'siteid': 1000,
                'lpage': 1,
                'classid': 177,
                'sid': 'I am sid', 
                'g': '快速回复'
            }
            req = requests.post(req_url, headers=HEADERS, data=data)
        print('第%d个肉贴，帖子id为:%s'%(i+1,introu_id))
        print('回复的内容为:%s'%data['content'])
        i = i+1
        time.sleep(5)

   

if __name__ == '__main__':
    for x in range(1,8):
        url = "https://yaohuo.me/bbs/book_list.aspx?action=new&siteid=1000&classid=0&getTotal=2020&page=%d" %x
        print(x)
        main(url,x)
