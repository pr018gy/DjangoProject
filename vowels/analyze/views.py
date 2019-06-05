from django.shortcuts import render

# Create your views here.
def homepag(request):
    return render(request,'inde.html')
def calc(request):
    vol_count=0
    consonent_count=0
    vow=['a','e','i','o','u']
    if request.method =='POST':
        text= request.POST['text'].lower()
        for chars in text:
            if not chars.isalpha():
                continue
            elif chars in vow:
                vol_count+=1
            else:
                consonent_count+=1
        return  render(request, 'inde.html',{'vowel':vol_count,'consonants':consonent_count,'text':text}) 
        
        

    else:
        return render(request,'inde.html')