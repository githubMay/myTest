'''class person():#使用属性property对变量进行保护
    def __init__(self,name):
        self.hidden_name=name
    def get(self):
        print('usingGet')
        return self.hidden_name
    def set(self,name):
        print('usingSet')
        self.hidden_name=name
    name=property(get,set)'''
    

        
'''class person():#属性保护的另外一种形式，使用修饰符来保护，会使用新的方法@property,name.setter
    def __init__(self,name):
        self.hidden_name=name
    @propertys
    def name(self):
        print('usingGet')
        return self.hidden_name
    @name.setter
    def name(self,name):
        print('usingSet')
        self.hidden_name=name'''
   

class person():#属性保护的另外一种形式，使用修饰符来保护，会使用新的方法@property,name.setter
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        print('usingGet')
        return self.__name
    @name.setter
    def name(self,name):
        print('usingSet')
        self.__name=name
   


        


