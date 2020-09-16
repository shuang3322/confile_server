from django.shortcuts import render, HttpResponse
from db import models
from django import forms
import re
import csv
from bs4 import BeautifulSoup


# Create your views hered
class EmpForm(forms.Form):
    name = forms.CharField(label="文件名", error_messages={"min_length": "你太短了", "required": "该字段不能为空!"})
class textFrom(forms.Form):
    textabout = forms.CharField(label="测试",error_messages={"min_length": "你太短了", "required": "该字段不能为空!"})

def test_veda(request):
    # book = models.CONF_PATH(name="shuang")
    # book.save()
    # with open('D:\python测试\\3.csv','r')as f1:
    #     f_csv = csv.reader(f1)
    #     for item in f_csv:
    #         book = models.CONF_PATH(path=item[0])
    #         book.save()
    # books = models.CONF_PATH.objects.all()
    # print(books, type(books))
    # print(request)
    # return HttpResponse("<p>数据添加成功！</p>")
    # return render(request, 'index.html', {'items': books})
    if request.method == 'GET':
        with open('D:\\1', 'r', encoding='utf-8')as f:
            file_test = f.readlines()
        # print(file_test)
        return render(request,'test2.html',{'text': file_test})
    # elif request.method == 'POST':
    #     form_test = textFrom(request.POST)
    #     if form_test.is_valid():
    #         data = form_test.cleaned_data
    #         print(data.get('textabout'))
def return_save_and_log_file(request):
    if request .method == "GET":
        with open('D:\\2', 'r', encoding='utf-8')as f:
            file_test = f.readlines()
            # print(file_test)
        return render(request, 'test3.html', {'text': file_test})
    # elif request.method == "POST":
    #     form_test = textFrom(request.POST)
    #     data = form_test.cleaned_data
    #     print(data.get('text'))

def add_ajax(request):
    print(request)
    # print('hello wirld')
    # print(request.POST.get('aaa1'))
    list_request = request.POST.get('aaa1')
    # print(list_request)
    soup = BeautifulSoup(list_request,"html.parser")
    with open('D:\\2', 'w', encoding='utf-8')as f1:
        for item in soup.find_all("p"):
            if item.get_text().find('\n') > 0:
                f1.write(item.get_text())
                print(item.get_text(), type(item.get_text()))
                print(item.get_text().find('\n'))
            else:
                item1 = item.get_text()+'\n'
                f1.write(item1)
                print(item1,type(item1))

    # re_list = re.match("(?P<value>\d+)",list_request)
    # print(re_list.group())
    # for item in list_request:
    #     #     print(item)
    # with open('D:\\2','w',encoding='utf-8')as f1:
    #      for item in request.POST.get('aaa1'):
    #          f1.write(item)
    #          f1.write('\n'
    return HttpResponse('hello world')

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            # data.pop('r_salary')
            print(data.get('name'))
            if data.get('name') =='all':
                form1 = models.CONF_PATH.objects.all()
            else:
                form1 = models.CONF_PATH.objects.filter(file=data.get('name'))
            # return HttpResponse(
            #     'ok'Admin
            # )
            return render(request, 'add_emp.html', {'items': form1})
        else:
            print(form.errors)  # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})
