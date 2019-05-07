from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Message
from .forms import FriendForm, MessageForm
from .forms import FindForm
from .forms import CheckForm
from django.core.paginator import Paginator

#初期表示
def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 5)
    params = {
            'title': 'TOP画面',
            'message':'',
            'data': page.get_page(num),
            }
        
    return render(request, 'hello/index.html', params)

# create
def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)#画面入力した値と対象テーブルをひとつの変数にまとめる。
        friend.save()
        return redirect(to='/hello')
    params = {
            'title': '新規メンバー登録',
            'form': FriendForm(),            
            }
    
    return render(request, 'hello/create.html', params)

#edit
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello/find/')
    params = {
            'title': 'メンバー情報更新画面',
            'id':num,
            'form':FriendForm(instance=obj),
            }
    return render(request, 'hello/edit.html', params)

#delete
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello/find/')
    params = {
            'title': 'メンバー削除画面',
            'id': num,
            'obj': friend,            
            }
    return render(request, 'hello/delete.html', params)

#find
def find(request, num=1):
    if (request.method == 'POST'):
        msg = request.POST['find']
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(name__contains=str)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    page = Paginator(data, 5)
    params = {
            'title': 'メンバー検索画面',
            'message': msg,
            'form': form,
            'data': page.get_page(num),
        }
    return render(request, 'hello/find.html', params)


#バリデーションチェック
def check(request):
    params = {
            'title': 'Hello',
            'message': 'check validation.',
            'form': CheckForm(),
            }
    if(request.method == 'POST'):
        form = CheckForm(request.POST)
        params['form'] = form
        if(form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)

#Message
def message(request, page=1):
    if(request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    
    params = {
            'title': 'コメント登録画面',
            'form':MessageForm(),
            'data':paginator.get_page(page),
            }
    return render(request, 'hello/message.html', params)

#msgedit
def msgedit(request, num):
    obj = Message.objects.get(id=num)
    if(request.method == 'POST'):
        message = MessageForm(request.POST, instance=obj)
        message.save()
        return redirect(to='/hello/message')
    params = {
            'title': '更新画面',
            'id':num,
            'form':MessageForm(instance=obj),
            'obj':obj,
            }
    return render(request, 'hello/msgedit.html', params)

#delete
def msgdelete(request, num):
    message = Message.objects.get(id=num)
    if(request.method == 'POST'):
        message.delete()
        return redirect(to='/hello/message')
    params = {
            'title': '削除画面',
            'id': num,
            'obj': message,            
            }
    return render(request, 'hello/msgdelete.html', params)



    