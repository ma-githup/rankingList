from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
# Create your views here.

# 连接redis，实现有序集合
conn = get_redis_connection('default')

# 添加服务器
class AddServer(View):
    def get(self,request):
        return render(request,'Add.html')

    def post(self,request):
        name = request.POST.get('name')
        score = request.POST.get('score')

        if not all([name,score]):
            return render(request,'Add.html',{'code':4000,'mes':'输入不可为空'})
        # 输入的分数必须由数字组成且有范围
        if not score.isdigit() or int(score) not in range(1,10000001):
            return render(request,'Add.html',{'code':4001,'mes':'分数只能是数字且只能在1~10000000之间'})

        # redis实例
        conn.zadd('rankList',{name:int(score)})
        return render(request,'Add.html',{'code':2000,'mes':'添加成功'})

# 展示排名
class ShowRank(View):
    def get(self,request):

        name = '客户端5'  # 模拟当前用户为  “客户端5”
        start = int(request.GET.get('start',1)) # 查询任何名次段
        end = int(request.GET.get('end',0))

        rankList = conn.zrevrange('rankList',start-1,end-1,withscores=True)  # redis中排名默认从0开始，需进行处理
        rankList = list(map(lambda x:{'rank':conn.zrevrank('rankList',x[0]) + 1,'name':x[0],'score':int(x[1])},rankList))

        rank = conn.zrevrank('rankList',name) + 1
        score = conn.zscore('rankList',name)
        cli = {'rank':rank,'name':name,'score':int(score)}
        return render(request,'Show.html',locals())