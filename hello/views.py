from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend, Message, place, purpose, urldata, suggest
from .forms import FriendForm, MessageForm, placeForm, purposeForm, urlForm, suggestForm
from .forms import FindForm
from .forms import CheckForm
from django.core.paginator import Paginator


#初期表示
def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 5)
    params = {
            'title': 'データ登録画面',
            'message':'',
            'data': page.get_page(num),
            }
        
    return render(request, 'hello/index.html', params)


##############################場所情報管理
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

##################################目的情報登録

# createpurpose
def createpurpose(request):
    if(request.method == 'POST'):
        main_purpose = request.POST['main_purpose']
        purpose1 = request.POST['purpose1']
        purpose2 = request.POST['purpose2']
        purpose3 = request.POST['purpose3']
        purpose4 = request.POST['purpose4']
        purpose5 = request.POST['purpose5']
        purpose6 = request.POST['purpose6']
        purpose7 = request.POST['purpose7']
        purpose8 = request.POST['purpose8']
        purpose9 = request.POST['purpose9']
        purpose10 = request.POST['purpose10']
        purposewrap = purpose(main_purpose=main_purpose, purpose1=purpose1, purpose2=purpose2, purpose3=purpose3, purpose4=purpose4,\
             purpose5=purpose5, purpose6=purpose6, purpose7=purpose7, purpose8=purpose8, purpose9=purpose9, purpose10=purpose10)
        purposewrap.save()
    params = {
            'title': '目的情報登録',
            'form': purposeForm(), 
            'data': purpose.objects.all()           
            }
    return render(request, 'hello/createpurpose.html', params)


#edit
def editpurpose(request, num):
    obj = purpose.objects.get(id=num)
    if(request.method == 'POST'):
        purposeedit = purposeForm(request.POST, instance=obj)
        purposeedit.save()
        return redirect(to='/dev/createpurpose')
    params = {
            'title': '目的情報更新',
            'id':num,
            'form':purposeForm(instance=obj),
            }
    return render(request, 'hello/editpurpose.html', params)
    

#delete
def deletepurpose(request, num):
    deletepurpose = purpose.objects.get(id=num)
    if(request.method == 'POST'):
        deletepurpose.delete()
        return redirect(to='/dev/createpurpose')
    params = {
            'title': '場所情報削除',
            'id': num,
            'obj': deletepurpose,            
            }
    return render(request, 'hello/deletepurpose.html', params)

##################################URL情報登録


def createurl(request):
    if(request.method == 'POST'):
        url = request.POST['url']
        shopname = request.POST['shopname']
        shopplace1 = request.POST['shopplace1']
        shopplace2 = request.POST['shopplace2']
##        shopplace3 = request.POST['shopplace3']
##        shopplace4 = request.POST['shopplace4']
##        shopplace5 = request.POST['shopplace5']
        tag1 = request.POST['tag1']
        tag2 = request.POST['tag2']
        tag3 = request.POST['tag3']
##        tag4 = request.POST['tag4']
##        tag5 = request.POST['tag5']
##        tag6 = request.POST['tag6']
##        tag7 = request.POST['tag7']
##        tag8 = request.POST['tag8']
##        tag9 = request.POST['tag9']
##        tag10 = request.POST['tag10']

        urlwrap  = urldata(url=url,shopname=shopname,shopplace1=shopplace1,shopplace2=shopplace2,\
             tag1=tag1, tag2=tag2, tag3=tag3 )
        urlwrap.save()
    params = {
            'title': 'URL情報登録',
            'form': urlForm(), 
            'data': urldata.objects.all()           
            }
    return render(request, 'hello/createurl.html', params)


#edit
def editurl(request, num):
    obj = urldata.objects.get(id=num)
    if(request.method == 'POST'):
        editurl = urlForm(request.POST, instance=obj)
        editurl.save()
        return redirect(to='/dev/createurl')
    params = {
            'title': 'URL情報更新',
            'id':num,
            'form':urlForm(instance=obj),
            }
    return render(request, 'hello/editurl.html', params)


#delete
def deleteurl(request, num):
    deleteurl = urldata.objects.get(id=num)
    if(request.method == 'POST'):
        deleteurl.delete()
        return redirect(to='/dev/createurl')
    params = {
            'title': 'URL情報削除',
            'id': num,
            'obj': deleteurl,            
            }
    return render(request, 'hello/deleteurl.html', params)

##################################サジェスト情報登録

# create
def createsuggest(request):
    if(request.method == 'POST'):
        suggestkannzi = request.POST['suggest']
        suggestkana = request.POST['suggestkana']
        suggestwrap = suggest(suggestkana=suggestkana, suggest=suggestkannzi)
        suggestwrap.save()
    data = suggest.objects.all().order_by('suggestkana')
    params = {
            'title': 'サジェスト情報登録',
            'form': suggestForm(), 
            'data': data           
            }
    return render(request, 'hello/createsuggest.html', params)

#edit
def editsuggest(request, num):
    obj = suggest.objects.get(id=num)
    if(request.method == 'POST'):
        editsuggest = suggestForm(request.POST, instance=obj)
        editsuggest.save()
        return redirect(to='/dev/createsuggest')
    params = {
            'title': 'サジェスト情報更新',
            'id':num,
            'form':suggestForm(instance=obj),
            }
    return render(request, 'hello/editsuggest.html', params)
    
#delete
def deletesuggest(request, num):
    deletesuggest = suggest.objects.get(id=num)
    if(request.method == 'POST'):
        deletesuggest.delete()
        return redirect(to='/dev/createsuggest')
    params = {
            'title': 'サジェスト情報削除',
            'id': num,
            'obj': deletesuggest,            
            }
    return render(request, 'hello/deletesuggest.html', params)



#############################バリデーションチェック
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

##############################Message
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



def djangoportfolio(request):
    return render(request, 'hello/djangoportfolio.html')

def top(request):
    pulllist = {
        'data': suggest.objects.all(),
    }
    return render(request, 'hello/top.html', pulllist)

def top2(request): 
    params = {
            'title': 'メンバー検索画面',
            'data1': place.objects.all(),
            'data2': purpose.objects.all(),
    }
    return render(request, 'hello/top2.html', params)



def findurl(request): 
    place = request.POST['place']
    purpose = request.POST['purpose']
    data = urldata.objects.filter(shopplace1__contains=place, tag1__contains=purpose)
    params = {
            'data': data
        }
    return render(request, 'hello/top2.html', params)


def devtest(request):
    return render(request, 'hello/devtest.html')
    

#######################################################################################################
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

