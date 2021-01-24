from django.db import models

class NoReportTax(models.Model):
    """무신고 가산세 관련 모델
    """

    updated_at = models.DateTimeField(auto_now=True) #데이터 업데이트 시각. key로 사용
    final_norepo_tax =  models.IntegerField() #무신고 예상 가산세액
    final_delayrepo_tax =  models.IntegerField() #지연신고 예상 가산세액


    # def __str__(self):
    #     return f'[{self.pk}]{self.title}'


# class PenaltyTaxRate(models.Model):
#     """가산세 기준(부정행위/일반)
#     """

#     title = models.CharField(max_length=30)  #가산세 항목 description 
#     rate = models.FloatField() #가산세 항목별 세율 ex) 40%
#     created_at =  models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True) #데이터 업데이트 시각

#     def __str__(self):
#         return f'[{self.pk}]{self.title}'


# class PenaltyDiscountRate(models.Model):
#     """감면 기준(1개월이내/1개월초과... 등등)
#     """

#     title = models.CharField(max_length=30)  #가산세 감면 기간 description ex) 가. 1개월 이내
#     period = models.IntegerField() #감면 기한 적용 기간 day 기준이므로 int 활용. ex) 30 DAYs
#     rate = models.FloatField() #감면율 ex) 90%
#     created_at =  models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True) #데이터 업데이트 시각

#     def __str__(self):
#         return f'[{self.pk}]{self.title}'


