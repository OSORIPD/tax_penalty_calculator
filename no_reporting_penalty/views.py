from django.shortcuts import render
from django.shortcuts import redirect

from .models import NoReportTax
from django.http import HttpResponseRedirect
from django import forms

"""2021-01-24 v1 박상현
"""


def no_reporting(request):
    """무신고 가산세 , 납부지연 가산세 처리
    """

    if request.method == 'GET':
        return render(request,'no_reporting_penalty/no_reporting.html')

    elif request.method == 'POST':

        #DB 에서 전체 무신고 가산세 평가건 로드
        # noReports = NoReportTax.objects.all()

 
        if 'norepo_submit_btn' in request.POST:

            is_error_norepo_tax_tobepaid = False

            # 1.납부해야할 세액 처리
            norepo_tax_tobepaid = request.POST.get('norepo_tax_tobepaid','')
            if norepo_tax_tobepaid is None or norepo_tax_tobepaid is '' :
                norepo_tax_tobepaid = 0
        
            #예외처리: 숫자 외의 입력이 들어올 경우 0으로 간주
            if type(norepo_tax_tobepaid) is str:
                try:
                    norepo_tax_tobepaid = int(norepo_tax_tobepaid)
                
                except:
                    norepo_tax_tobepaid = 0
                    is_error_norepo_tax_tobepaid = True


            # 2. 가산세율 수신 처리
            norepo_taxrate_tobepaid = request.POST.get('norepo_taxrate_tobepaid','')

            if( norepo_taxrate_tobepaid == "40%"):
                tax_rate_basic = 0.4

            else:
                tax_rate_basic = 0.2 


            # 3. 감면 계산
            datetimepicker1_input = request.POST.get('datetimepicker1_input','')
            datetimepicker2_input = request.POST.get('datetimepicker2_input','')
            select_discount_period =  request.POST.get('norepo_taxrate_todiscount','')

            if(select_discount_period == "50%"):
                tax_rate_discount = 0.5

            elif(select_discount_period == "30%"):
                tax_rate_discount = 0.3

            elif(select_discount_period == "20%"):
                tax_rate_discount = 0.2

            else:
                tax_rate_discount = 0
    

            # 4. 최종 계산
            if is_error_norepo_tax_tobepaid is True:
                return_value = "납부해야할 세액이 잘못 입력되었습니다."
            else:
                return_value = int(norepo_tax_tobepaid * tax_rate_basic *(1 - tax_rate_discount))
            
            return_dic = { 

                'datetimepicker1_input' : datetimepicker1_input,
                'datetimepicker2_input' : datetimepicker2_input,
                'datetimepicker3_input' : datetimepicker1_input,
                'datetimepicker4_input' : datetimepicker2_input,

                'norepo_finaltax': return_value,
                'final_norepo_tax' :  return_value,
            }


            return render(request,'no_reporting_penalty/no_reporting.html', return_dic)


        elif 'delayrepo_submit_btn' in request.POST:
            
            is_error_delayrepo_taxtobepaid = False

            # 1.납부해야할 세액 처리
            delayrepo_taxtobepaid = request.POST.get('delayrepo_taxtobepaid','')
            if delayrepo_taxtobepaid is None or delayrepo_taxtobepaid is '' :
                delayrepo_taxtobepaid = 0
        
            #예외처리: 숫자 외의 입력이 들어올 경우 0으로 간주
            if type(delayrepo_taxtobepaid) is str:
                try:
                    delayrepo_taxtobepaid = int(delayrepo_taxtobepaid)
                
                except:
                    delayrepo_taxtobepaid = 0
                    is_error_delayrepo_taxtobepaid = True



            # 2. 미납부일수 계산
            datetimepicker3_input = request.POST.get('datetimepicker3_input','')
            datetimepicker4_input = request.POST.get('datetimepicker4_input','')
            delayrepo_daytobepaid = request.POST.get('delayrepo_daytobepaid','')
    
            delayrepo_daytobepaid = int(delayrepo_daytobepaid)
    
            # 3. 세율 수신 처리
            delayrepo_taxrate =  request.POST.get('delayrepo_taxrate','')
            if(delayrepo_taxrate == "0.025%"):
                tax_rate_delay = 0.00025

            else:
                tax_rate_delay = 0.0003



            # 4. 최종 계산
            if is_error_delayrepo_taxtobepaid is True:
                return_value = "납부해야할 세액이 잘못 입력되었습니다."
            else:
                return_value = int(delayrepo_taxtobepaid * tax_rate_delay * delayrepo_daytobepaid )
                final_delayrepo_tax = return_value
                

                final_norepo_tax = request.POST['final_norepo_tax']

                try:
                    tax_final = int(final_norepo_tax) + return_value

                except:
                    tax_final = return_value


            return_dic = { 

         
                'datetimepicker1_input' : datetimepicker3_input,
                'datetimepicker2_input' : datetimepicker4_input,     
                'datetimepicker3_input' : datetimepicker3_input,
                'datetimepicker4_input' : datetimepicker4_input,

                'delayrepo_finaltax': return_value,   
                'final_delayrepo_tax' :  return_value,

                'norepo_finaltax' : final_norepo_tax,
                'final_norepo_tax': final_norepo_tax,


                'tax_final' : tax_final
            }




            return render(request,'no_reporting_penalty/no_reporting.html', return_dic)

        elif 'session_reset_btn' in request.POST:
            return_dic = {          
                # 'norepo_finaltax' : 0,
                # 'final_norepo_tax': 0,

                # 'tax_final' : 0
            }
            return render(request,'no_reporting_penalty/no_reporting.html',return_dic)



    else:
        raise Exception("POST도 GET도 아님")




