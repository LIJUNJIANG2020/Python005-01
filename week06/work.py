from abc import ABCMeta, abstractclassmethod


class Zoo(object):
    def __init__(self, name):
        self.zoo_name = name

    def add_animal(self, animal):
        # 同一只动物不能被重复添加
        type_ = animal.animal_type
        name = animal.name
        if type_ in self.__dict__.keys():
            self.__dict__[type_].append(name)
        else:
            self.__dict__[type_] = [name,]
            

class Animal(metaclass=ABCMeta):
    def __init__(self, feeding_habits, body_type, disposition):
        self.animal_type = self.__class__.__name__
        self.feeding_habits = feeding_habits
        self.body_type = body_type
        self.disposition = disposition

    def get_body_type(self):
        return {
            "小": 1,
            "中等": 2,
            "大": 3,
        }[self.body_type]
    
    def get_disposition(self):
        return {
            '温顺': 1,
            '凶猛': 2,
        }[self.disposition]

    def get_feeding_habits(self):
        return {
            '食肉': 0,
            '食草': 1,
        }[self.feeding_habits]

    @property
    def is_beast(self):
        body_type = self.get_body_type()
        disposition = self.get_disposition()
        feeding_habits = self.get_feeding_habits()
        if body_type >= 2 and disposition == 2 and feeding_habits == 0:
            return True
        else:
            return False

class Cat(Animal):
    def __init__(self, name, feeding_habits, body_type, disposition):
        super().__init__(feeding_habits, body_type, disposition)
        self.name = name
        self.call = 'miao..'
        
    @property
    def is_pet(self):
        return not self.is_beast

    def __str__(self):
        return self.name

class Dog(Animal):
    def __init__(self, name, feeding_habits, body_type, disposition):
        super().__init__(feeding_habits, body_type, disposition)
        self.name = name
        self.call = 'wwwwwwang...'

    @property
    def is_pet(self):
        return not self.is_beast

    def __str__(self):
        return self.name


if __name__ == "__main__":
    z = Zoo("时间动物园")
    cat1 = Cat("大花猫2", '食肉', '小', '温顺')
    print(f'cat1 is_pet: {cat1.is_pet}')
    print(f'cat1 is_beast:  {cat1.is_beast}')
    dog1 = Dog('藏獒', '食肉', '大', '凶猛')
    print(f'dog1 is_pet: {dog1.is_pet}')
    print(f'dog1 is_beast:  {dog1.is_beast}')
    
    z.add_animal(cat1)
    z.add_animal(dog1)

    print(z.__dict__)
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

