from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"input.html")
def output(request):
    num=request.GET.get("number","defult")
    even=request.GET.get("even_odd","off")
    sm_dgt=request.GET.get("sum","off")
    ck_prime=request.GET.get("prime","off")
    product=request.GET.get("prdt","off")

    if even=="on":
        prnt=""
        if int(num)%2==0:
            prnt+=f"{num}-Its a even number"
      
        else:
            prnt+=(f"{num}-its a odd number")
    
        parameter={"function":"Check Even or odd","result":prnt}
        return render(request,"output.html",parameter)

    elif sm_dgt=="on":
        sm=0
        for i in range(0,len(num)):
            sm+=int(num[i])
        parameter={"function":"Find SUM of digit","result":sm}
        return render(request,"output.html",parameter)

    elif ck_prime=="on":
        pm=""
        n=int(num)
        for i in range (2,n):
            if n%i==0:
                pm+=f"{num} is not prime"
                break
        else:
            pm+=f"{num} is prime"

        parameter={"function":"Check Prime or not","result":pm}
        return render(request,"output.html",parameter)
    elif product=="on":
        mul=1
        for i in range(0,len(num)):
            mul*=int(num[i])
        parameter={"function":"Find product of digit","result":mul}
        return render(request,"output.html",parameter)

        

   
    else:
        return HttpResponse('''<h3>Wrong input<h3><a href="http://127.0.0.1:8000/">Enter Again </a>''')
