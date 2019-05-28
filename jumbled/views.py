from django.shortcuts import render
from django.http import HttpResponse
import random 


word1 = [
    "pyhton",
    "java",
    "pearl",
    "programming"
    
    ]

def rword():  
    global jword,msg,word

    word=random.choice(word1)
    jumb=random.sample(word,len(word))
    jword="".join(jumb)
msg =" "
# Create your views here.
def homepag(request):
    rword()
    global jword,msg
    return render( request,'inde.html',{'jum_word':jword,'msg':msg})    
def checkans(request):
    global word,msg,jword
    user_answ = request.GET['answer']
    if user_answ==word:
        msg="That's right"
        homepag(request)
    else:
        msg="It's a wrong answer"

    
    return render( request,'inde.html',{'jum_word':jword,'msg':msg})  
