class AddressBookItems:
    
    def __init__(self, row=None):
        self.Index = 0
        self.Name = 'd'
        self.fName = 'd'
        self.Phone ='d'
        self.Description = 'd'
        if (row!=None):
            
            ListParam = row.split(",")
            if(len(ListParam)==5):
                self.Index = ListParam[0]
                self.Name = ListParam[1].replace(' ','')
                self.fName = ListParam[2].replace(' ','')
                self.Phone = ListParam[3].replace(' ','')
                self.Description = ListParam[4]
    
    def __str__(self) -> str:
        return (f'{self.fName} {self.Name} ({self.Phone}) [Index = {self.Index}]')
    
    def getText(self):
        return (f'{self.Index}, {self.Name}, {self.fName}, {self.Phone}, {self.Description} \n')

_collectionItem = []

def FillCollection (collection):
    with open('repo.txt','r',encoding='utf-8') as collect:
        for line in collect:
            tmp = line.replace('\n','')
            if(len(tmp)!=0):
                _collectionItem.append(AddressBookItems(tmp))
            
def SaveItem():
    with open('repo.txt','w',encoding='utf-8') as outfile:
        for i in range(len(_collectionItem)):
            outfile.write(_collectionItem[i].getText())

def DeleteItem (index):
    IsDelete = False
    for i in range(len(_collectionItem)):
        if (_collectionItem[i].Index ==index):
            print(f'Запись {_collectionItem[i].Index} удалена')
            _collectionItem.remove(_collectionItem[i])
            IsDelete = True
    return IsDelete
        

def FoundItem(ParamName,ParamValue):
    for i in range(len(_collectionItem)):
        if(ParamName=='Index'):
            if(_collectionItem[i].Index ==ParamValue):
                print(_collectionItem[i])
        if(ParamName=='Name'):
            if(_collectionItem[i].Name ==ParamValue):
                print(_collectionItem[i])
        if(ParamName=='fName'):
            if(_collectionItem[i].fName ==ParamValue):
                print(_collectionItem[i])
        if(ParamName=='Phone'):
            if(_collectionItem[i].Phone ==ParamValue):
                print(_collectionItem[i])
                
def AddNewItem (row):
    lst = row.split(',')
    if(len(lst)==4):
        item = AddressBookItems()
        item.Index = str(GetMaxIndex()+1)
        item.Name = lst[0]
        item.fName=lst[1]
        item.Phone = lst[2]
        item.Description=lst[3]
        _collectionItem.append(item)
        
def FindToFam ():
    print('Введите фамилию и нажмите Enter:')
    fam = input()
    FoundItem('fName',fam)
    MainMethod()

def FindToNum ():
    print('Введите номер и нажмите Enter:')
    num = input()
    FoundItem('Phone',num)
    MainMethod()

    
def GetMaxIndex():
    max = 0
    for i in range(len(_collectionItem)):
        if(int(_collectionItem[i].Index)>max):
            max = int(_collectionItem[i].Index)
    return max

def ShowMenu ():
    print('1. Распечать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить новую запись\n'
          '7. Закончить работу', sep = '\n'
          )
    return int(input())

def print_AddressBook():
    for i in range(len(_collectionItem)):
        print(_collectionItem[i])
    MainMethod()
    
def DeletRow ():
    print ('Укажите индекс записи для удаления:')
    index = input()
    
    if (not DeleteItem(index)):
        print('запись не найдена')
    MainMethod()
    
def EditRow ():
    print ('Укажите индекс записи для изменения номера:')
    index = input()
    row = None
    for i in range(len(_collectionItem)):
        if(_collectionItem[i].Index==index):
            row =_collectionItem[i] 
    
    if (row!=None):
        print('Запись найдена, укажите новый номер телефона:')
        num = input()
        row.Phone = num
        print('Изменение выполнено.')
    else:
        print('Запись не найдена, изменение недоступно.')
        
def AddNewRow():
    print ('Укажите параметры новой записи в формате - [Имя],[Фамилия],[Телефон],[Описание]:')
    row = input()
    AddNewItem(row)
    print ('Запись сохранена.')
    
        
        
    

def MainMethod ():
    i = ShowMenu()
    
    if i ==1:
        print_AddressBook()
    elif i ==2:
        FindToFam()
    elif i==5:
        FindToNum()
    elif i==4:
        DeletRow ()
    elif i==3:
        EditRow()
        MainMethod()
    elif i ==6:
        AddNewRow()
        MainMethod()
    elif i ==7:
        SaveItem()
        exit()
        



    
    
    
    
            
FillCollection(_collectionItem)

##FoundItem('Name','Константин')
##DeleteItem('4')
#ShowMenu()
MainMethod()

##SaveItem(_collectionItem)



##print()
        
        

