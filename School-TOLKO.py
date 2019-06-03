# # Задание-1:
# # Реализуйте описаную ниже задачу, используя парадигмы ООП:
# # В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# # У каждого ученика есть два Родителя(мама и папа).
# # Также в школе преподают Учителя. Один учитель может преподавать
# # в неограниченном кол-ве классов свой определенный предмет.
# # Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# # но больше математику не может преподавать никто другой.
#
# # Выбранная и заполненная данными структура должна решать следующие задачи:
# # 1. Получить полный список всех классов школы
# # 2. Получить список всех учеников в указанном классе
# #  (каждый ученик отображается в формате "Фамилия И.О.")
# # 3. Получить список всех предметов указанного ученика
# #  (Ученик --> Класс --> Учителя --> Предметы)
# # 4. Узнать ФИО родителей указанного ученика
# # 5. Получить список всех Учителей, преподающих в указанном классе
import weakref
import random
# FAMILY = ('Иванов', 'Петров', 'Сидоров', 'Осин')
# NAME = ('A', 'Б', 'Г', 'Д')
# SUBJECT = ('биология', 'математика', 'химия', 'английский язык')
# class School():
#     def __init__(self, name):
##        self.name = name
#         self.Classes = []
#     def addClass(self, Clas):
#         '''dobavlyaet class v scholy'''
#         self.Classes.append(Clas)
            '''!!! вот я здесь не понял, то есть получается метод так сделан чтобы каждый раз новый класс в список добав
            лялся руками? Ведь нужен ( и я у Вас спрашивал) метод, чтобы автоматически все что заполнялось в def __init__
            сразу по смыслу добавлялось в словарь автоматом, я вроде нашел как это сделать но не знаю как из функции вытащить
            '''
#     def showClasses(self):
#         '''метод возвращает все классы в школы'''
#         print('Школа{} содержит:'.format(self.name))
#         for itm in self.Classes:
#             print('класс{}'.format(itm.name))
'''' !!!! тут тоже не понял, если в список классов функция классы добавлялись 
# через метод def addClass(self, Clas) то откуда берется itm.name (вопрос откуда берется name)?'''
#     def showClass(self, name):
#         '''метод возвращения списка всех учеников в классе'''
#         for itm in self.Classes:
#             if itm.name == name: itm.showClass()
'''!!!! вот тут вообще не понял как это работает? - то есть если в списке классов есть заданный в функции класс,
# то что это за код вообще - itm.showClass()?? Так разве можно и что он делает? это же сама функция'''
#     def showPupilInfo(self, name):
#         '''метод возвращения ученик - класс - учителя - предметы'''
#         for cl in self.Classes:
#             for pup in cl.Pupils:
#                 if pup.name == name:
#                     for teach in cl.Teachers:
#                         print('Ученик {} класс {} преподаватель {} предмет {}'.format(pup.name, cl.name, teach.name, teach.subject))
   ''' !!! тут тоже не понял - здесь получается name - это имя ученика, и соответствено часть где имя ученика ищетс в cl.Pupils: мне 
   еще понятна, но как потом формируется список на принт, там что так заашито что если по списку cl.Pupils: выбрано определнное имя,
   то и из всех остальных списков также будут находиться значения с этим же именем? Но ведь в списке cl.Teachers только фио учителя и 
   название предмета (subject)? '''
#
#     def showPupilParents(self, name):
#         '''метод возвращающий родителя ученика'''
#         for cl in self.Classes:
#             for pup in cl.Pupils:
#                 if pup.name == name: pup.showParents()
#
#
#     def gensSchool(self, classes, pupils, subjects):
#         '''метод генерации школы с количеством классов учеников в классе и количеством предметов в классе'''
#         for idx in range(int(classes)):
#             xclass = Class(str(random.randint(1,11)) + random.choice(('A', 'B', 'C', 'D')))
#             self.addClass(xclass)
#             for i in range(int(pupils)):
''' тут тоже не понял как так - во первых xclass - он же 1  состоит условно из 11А, как в него как в списов получается доба
вляются ученики через функцию addPupil? зачем тогда сразу за скобкамиснова пишется Pupil - addPupil(Pupil? и зачем в три
строки заполняются данные фио если они все равно рендамом заполняются исходя из количства учеников в классе?'''
#                 xclass.addPupil(Pupil(random.choice(FAMILY) + '' + random.choice(NAME) + random.choice(NAME),
#                                       random.choice(FAMILY) + '' + random.choice(NAME) + random.choice(NAME),
#                                       random.choice(FAMILY) + 'a ' + random.choice(NAME) + random.choice(NAME)))
#                 for i in range (int(subjects)):
#                     xclass.addTeacher(random.choice(FAMILY) + random.choice(NAME) + random.choice(NAME), random.choice(SUBJECT))
#
# class Class():
#     def __init__(self, name):
#         self.name = name
#         self.Pupils = []
#         self.Teachers = []
#
#     def addPupil(self, pupil):
#         '''метод добавляет ученика в класс'''
#         self.Pupils.append(pupil)
            ''' !!!!!! Не понимаю принцип работы данных функций - правильно ли я понял что нужно каждый рах в ручную вызывать функцию
            и как аргумент (self, pupil) передавать значение pupil? но в чем тогда смысл автозаполнение которое написано выше? и аналогично вопрос 
            к функциям ниже'''
#
#     def addTeacher(self, name, subject):
#         '''метод добавления учителя с предметом в класс'''
#         self.Teachers.append(Teacher(name, subject))
            ''' то есть вот так можно из другого класса добавить его атрибуты просто через ссылку на класс и в скобаках на 
            атрибуты?'''
#
#     def showClass(self):
#         '''метод возвращает список учеников в классе'''
#         print('Класс {} содержит:'.format(self.name))
#         for itm in self.Pupils:
#             print('ученик {}'.format(itm.name))
#
# class Pupil():
#     def __init__(self, name, father, mother):
#         self.name = name
#         self.father = father
#         self.mother = mother
#
#     def showParents(self):
#         '''метод возвращает родителей ученика'''
#         print('Отец - {}, mAT - {}'.format(self.father, self.mother))
#
# class Teacher():
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

