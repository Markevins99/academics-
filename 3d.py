information={2019:{'sl no':[],'names':[],'stream':[]},
             2020:{'sl no':[],'names':[],'stream':[]},2021:{'sl no':[],'names':[],'stream':[]}}



print('the input for sl no for 2019 is')
information[2019]['sl no'].clear()
for i in range(0,5):
    information[2019]['sl no'].append(int(input()))

print('the input for sl no for 2020 is')
information[2020]['sl no'].clear()
for i in range(0,5):
    information[2020]['sl no'].append(int(input()))

print('the input for sl no for 2021 is')
information[2021]['sl no'].clear()
for i in range(0,5):
    information[2021]['sl no'].append(int(input()))


print('the input for names for 2019 is')
list1=[]
information[2019]['names'].clear()
for i in range(0,5):
    
    das=str(input())
    if das not in list1:
        list1=das
    information[2019]['names'].append(list1)
    
print('the input for names for 2020 is')
list2=[]
information[2020]['names'].clear()
for i in range(0,5):
    
    das1=str(input())
    if das1 not in list2:
        list2=das1
    information[2020]['names'].append(list2)
    
print('the input for names for 2021 is')
list3=[]
information[2021]['names'].clear()
for i in range(0,5):
    
    das2=str(input())
    if das2 not in list3:
        list3=das2
    information[2021]['names'].append(list3)




print('the input for names of stream of 2019 is')
strim=[]
information[2019]['stream'].clear()
for i in range(0,5):
    item=str(input())
    if item not in strim:
        strim=item
    information[2019]['stream'].append(strim)
    
print('the input for names of stream of 2020 is')
strim1=[]
information[2020]['stream'].clear()
for i in range(0,5):
    item1=str(input())
    if item1 not in strim1:
        strim1=item1
    information[2020]['stream'].append(strim1)
    
print('the input for names of stream of 2021 is')
strim2=[]
information[2021]['stream'].clear()
for i in range(0,5):
    item2=str(input())
    if item2 not in strim2:
        strim2=item2
    information[2021]['stream'].append(strim2)





for key,value in information.items():
    print(key,value)