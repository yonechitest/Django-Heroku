from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Message
from .forms import FriendForm, MessageForm, placeForm
from .forms import FindForm
from .forms import CheckForm
from .models import place
from .models import purpose
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
        main_place = request.POST['main_place']
        place1 = request.POST['place1']
        place2 = request.POST['place2']
        place3 = request.POST['place3']
        place4 = request.POST['place4']
        place5 = request.POST['place5']
        place6 = request.POST['place6']
        place7 = request.POST['place7']
        place8 = request.POST['place8']
        place9 = request.POST['place9']
        place10 = request.POST['place10']
        placewrap = place(main_place=main_place, place1=place1, place2=place2, place3=place3, place4=place4, place5=place5,\
                        place6=place6, place7=place7, place8=place8, place9=place9, place10=place10)
        placewrap.save()
    else:
        msg = 'search words...'
        form = FindForm()
    params = {
            'title': '新規場所登録',
            'form': placeForm(), 
            'data': place.objects.all()           
            }
    
    return render(request, 'hello/create.html', params)

#edit
def edit(request, num):
    obj = place.objects.get(id=num)
    if(request.method == 'POST'):
        placeedit = placeForm(request.POST, instance=obj)
        placeedit.save()
        return redirect(to='/dev/create')
    params = {
            'title': '場所情報更新',
            'id':num,
            'form':placeForm(instance=obj),
            }
    return render(request, 'hello/edit.html', params)

#delete
def delete(request, num):
    placeedit = place.objects.get(id=num)
    if(request.method == 'POST'):
        placeedit.delete()
        return redirect(to='/dev/create')
    params = {
            'title': '場所情報削除',
            'id': num,
            'obj': placeedit,            
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
        return redirect(to='/dev/message')
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
        return redirect(to='/dev/message')
    params = {
            'title': '削除画面',
            'id': num,
            'obj': message,            
            }
    return render(request, 'hello/msgdelete.html', params)





def top(request):
    pulllist = {
        'place': place.objects.all(),
        'purpose': purpose.objects.all(),
    }
    return render(request, 'hello/top.html', pulllist)




def top2(request): 
    params = {
            'title': 'メンバー検索画面',
            'data1': place.objects.all(),
            'data2': purpose.objects.all(),
    }
    return render(request, 'hello/top2.html', params)



def devtest(request):
    return render(request, 'hello/devtest.html')
    