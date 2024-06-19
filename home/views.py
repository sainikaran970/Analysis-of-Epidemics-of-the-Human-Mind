from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Test
from Predict import predict
from django.contrib import messages
# We use render keyword to render the templates

# Create your views here.
def index(request):
    # context = {
    #     "variable" : "this is sent"
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')
    # return HttpResponse('This is Home page')

def about(request):
    # return HttpResponse('This is About page')
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    # return HttpResponse('This is Services page')

def blogdetails(request):
    return render(request, 'blog-details.html')

def journal(request):
    return render(request, 'journal.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # password = request.POST.get('password')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name , email = email , phone = phone , desc = desc , date = datetime.today())
        contact.save()
        messages.success(request, "Our team will contact you shortly..!")

    return render(request, 'contact.html')
    # return HttpResponse('This is Contact page')

def test(request):
    if request.method == "POST":
        
        # name = request.POST.get('name')
        # test = Test(name=name)
        # # test.save()

        # test1 = request.POST.get('test1')
        # test = Test(test1=test1)
        # # test.save()

        # test2 = request.POST.get('test2')
        # test = Test(test2=test2)
        # # test.save()

        # test3 = request.POST.get('test3')
        # test = Test(test3=test3)
        # # test.save()

        # test4 = request.POST.get('test4')
        # test = Test(test4=test4)
        # # test.save()

        # test5 = request.POST.get('test5')
        # test = Test(test5=test5)
        # # test.save()

        # test6 = request.POST.get('test6')
        # test = Test(test6=test6)

        # test.save()


        name = request.POST.get('name')
        # test = Test(name=name)

        test1 = request.POST.get('test1')

        test2 = request.POST.get('test2')

        test3 = request.POST.get('test3')

        test4 = request.POST.get('test4')

        test5 = request.POST.get('test5')

        test6 = request.POST.get('test6')

        test7 = request.POST.get('test7')

        test8 = request.POST.get('test8')

        test9 = request.POST.get('test9')

        test10 = request.POST.get('test10')
        
        test11 = request.POST.get('test11')
        
        test12 = request.POST.get('test12')
        
        test13 = request.POST.get('test13')
        
        test14 = request.POST.get('test14')

        test15 = request.POST.get('test15')

        test16 = request.POST.get('test16')

        test17 = request.POST.get('test17')

        test = Test(name = name , test1=test1 , test2=test2 , test3=test3 , test4=test4 , test5=test5 , test6=test6 , test7=test7 , test8=test8 , test9=test9 , test10=test10 , test11=test11 , test12=test12, test13=test13, test14=test14, test15=test15, test16=test16, test17=test17 , date = datetime.today())

        test.save()

        messages.success(request, "Your choices has been recorded and the result is...")
        
        val = predict(int(test1),int(test2),int(test3),int(test4),int(test5),int(test6),int(test7),int(test8),int(test9),int(test10),int(test11),int(test12),int(test13),int(test14),int(test15),int(test16),int(test17))

        # print(test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13,test14,test15,test16,test17)

        # name = request.POST.get('name')
        # test1 = request.POST.get('test1')
        # test2 = request.POST.get('test2')
        # test3 = request.POST.get('test3')
        # test4 = request.POST.get('test4')
        # test5 = request.POST.get('test5')
        # test6 = request.POST.get('test6')

        # test = Test(name=name)
        # test = Test(test1=test1)
        # test = Test(test2=test2)
        # test = Test(test3=test3)
        # test = Test(test4=test4)
        # test = Test(test5=test5)
        # test = Test(test6=test6)
        # test.save()
        if (val==0):
            return render(request, 'zero.html')
        elif(val==1):
            return render(request,'one.html')
        else:
            return render(request,'two.html')

    return render(request, 'test.html') 