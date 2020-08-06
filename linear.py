'''This code if For linear Convolution     
    Developed By Vraj Parikh           '''

#defining x[n] naming it as x
x=[1,2,3,5]

#defining h[n] naming it as h

h=[1,3]

length_x=len(x)
length_h=len(h)


print(x,"----->",len(x))
print(h,"----->",len(h))



#formula for linear convolution
#y= x *  h (* is convolution operator)


print(x[0],x[1],x[2],x[3])
print(h[0],h[1])

#making lenght of both strings equal

balance_lenght=length_x-length_h
print('balance Lenght ',balance_lenght)

while(len(h)<=balance_lenght+1):
    h.append(0)
    len(h)


print(h,"----->",len(h))
print(x,"----->",len(x))


#Here , we made the length of both strings equal by appending Zeros to h[n]

#Linearly plotting the values 

lin1=[i*1 for i in x ]
lin2=[i*3 for i in x]
#Linearly plotting the values 
print(lin1)
print(lin2)

for i in lin1:
   for j in lin2:
      l0=lin1[0]
      l1=lin1[1]+lin2[0]
      l2=lin1[2]+lin2[1]
      l3=lin1[3]+lin2[2]

      

      ln=lin2[-1]

final=[l0,l1,l2,l3,ln]
print('Final List',final)


# Verfication of Answers
sum_x=sum(x)
sum_h=sum(h)
sum_final=sum(final)

print('The Sum of Impulse List is ',sum_h)
print('The Sum of Given List',sum_x)
print('The Sum of Final List',sum_final)

productFinal=sum_h*sum_x

if productFinal==sum_final:
   print('The Linear Convolution condiition is satifies with \n')
   print('y[n] = ',productFinal)

   print(f'The product of x[n] * h[n] = y[n]' , sum_final)
  
else:
   print('There is some error in the calculation SOP mightbe')



