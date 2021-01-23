from django.shortcuts import render
from django.shortcuts import redirect
from .models import PenaltyTaxRate

# class PenaltyTaxRateList(ListView):
#     model = PenaltyTaxRate
#     ordering = '-pk'
#     # template_name = 'no_reporting_penalty/index.html'


# class PenaltyTaxRateDetail(DetailView):
#     model = PenaltyTaxRate

def index(request):
    return render(request,'no_reporting_penalty/index.html', { })

def no_reporting(request):
    return render(request,'no_reporting_penalty/no_reporting.html', { })



# def login_home(request):
#     return render(request,'no_reporting_penalty/login.html', { })


# def usd(request):
#     amount1 = request.POST['amount']
#     amount2 = int(amount1)
#     usd = amount2/1217.50
#     return render(request,'no_reporting_penalty/index.html', {'amount':amount2,'usd':usd})


# from django import forms
# class NameForm(forms.Form):
# 	your_name = forms.CharField(label = 'Your Name', max_length=100,widget=forms.Textarea)



# from django.http import HttpResponseRedirect
# def get_name(request):

# 	#POST방식이면 제출된 폼을 처리
# 	if request.method=='POST':
# 		form = NameForm(request.POST)
# 		if form.is_valid():
# 			#폼 데이터가 유효하면 cleaned_data로 복사된다
# 			new_name = form.cleaned_data['your_name']
			
# 			#추가적 처리들...(생략)
# 			#새로운 URL로 리다이렉션
            
# 			return HttpResponseRedirect('/thanks/')
# 	        #return render(request,'index.html',{'form':form})

# 	#POST가 아닌 GET이면 빈폼을 보여준다
# 	else:
# 		form = NameForm() #아까 정의해둔 폼클래스

# 	return render(request,'index.html',{'form':form})



# from .forms import LoginForm

# def login(request):
#     if request.method == 'GET':
#         form = LoginForm
#     elif request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             request.session['user'] = form.user_id
#             return redirect('/')
 
 
#     return render(request, 'login.html', {'form': form})




