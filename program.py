qA=int(input('enter the quantity of product A required : '))
qB=int(input('enter the quantity of product B required : '))
qC=int(input('enter the quantity of product C required : '))

cart={'pa':qA*20,
      'pb':qB*40,
      'pc':qC*50
      }

cart_total=cart['pa']+cart['pb']+cart['pc']
print('Product Name  Quantity  Total Amount')
print("Product A      {x}        {a}".format(x=qA,a=cart['pa']))
print("Product B      {y}        {b}".format(y=qB,b=cart['pb']))
print("Product C      {z}        {c}".format(z=qC,c=cart['pc']))
print("Subtotal = ",cart_total)
## flat10 ##

if cart_total > 200:
    flat_10=10
else:
    flat_10=0
    

## flat10 ##

## bulk5 ##
def bulk5(qA,qB,qC):
    if qA>10:
        bulk_5_a=0.05*qA*20
    else:
        bulk_5_a=0    
    if qB>10:
        bulk_5_b=0.05*qB*40
    else:
        bulk_5_b=0   
    if qC>10:
        bulk_5_c=0.05*qC*50
    else:
        bulk_5_c=0
    
    return(bulk_5_a+bulk_5_b+bulk_5_c)

bulk_5=bulk5(qA,qB,qC)    
      
## bulk5 ##

## bulk10 ##

if qA+qB+qC>20:
    bulk_10=0.1*cart_total
else:
    bulk_10=0
    


## bulk10 ##


## tiered50 ##
def tiered(qA,qB,qC):
    if qA+qB+qC>30 and qA>15 or qB>15 or qC>15:
        if qA>15:
            ta=(qA-15)*20*0.5
        else:
            ta=0
        if qB>15:
            tb=(qB-15)*40*0.5
        else:
            tb=0
        if qC>15:
            tc=(qC-15)*50*0.5
        else:
            tc=0
        tier_50=ta+tb+tc
    else:
        tier_50=0
    return(tier_50)
    
tiered_50=tiered(qA,qB,qC)

    
## tiered50 ##

## selection of discount ##

discounts={'flat_10_discount':flat_10,
         'bulk_5_discount':bulk_5,
         'bulk_10_discount':bulk_10,
         'tiered_50_discount':tiered_50
         }

discount_applied=max(discounts,key=discounts.get)
print('Discount applied : ',discount_applied)
discount_amount = discounts[discount_applied]
print('Discount Amount = ',discount_amount)

## selection of discount ##

## gift  ##

gift_wrap_fee=(qA+qB+qC)
print('Gift Wrap Fee = ',gift_wrap_fee)

##  gift  ##

## shipping  ##

shipping_package=(qA+qB+qC)//10

if (qA+qB+qC)%10 != 0:
    shipping_package=shipping_package + 1

shipping_fee=shipping_package*5
print("shipping fee = ",shipping_fee)

##  shipping  ##
    
##   total    ##

Total=cart_total-discount_amount+gift_wrap_fee+shipping_fee

print("Total = ",Total,'$')

##   total    ##



    
        
    
