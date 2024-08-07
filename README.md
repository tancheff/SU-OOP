# Theory tests

- [First Steps In OOP](https://forms.gle/jenahYVLxPK8PYhN6)

- [Classes and Objects](https://forms.gle/PeoSqmdHyCJbptxP8)

- [Inheritance](https://forms.gle/jzjTh2sLYGRNQak6A)

- [Encapsulation](https://forms.gle/rRjWfFMJgFeDLLmw6)

- [Static And Class Methods](https://forms.gle/eTrbAFr3SA2ohh3q8)

- [Polymorphism and Abstraction](https://forms.gle/9ArSM52FqWugHm7V8)

- [SOLID](https://forms.gle/AhW2e1hJnySE45KL9)

- [Iterators And Generators](https://forms.gle/c2GM6FsSRhAc3eyB8)

- [Decorators](https://forms.gle/5WEUAUmfKneqv8th7)

- [Unit Testing](https://forms.gle/EwZhDtuEaqnxyJzZA)

- [Final Test](https://forms.gle/WXhdCZnbSgyov1ZC9)

---

# Plans

### 01. First Steps In OOP

1. Какво е **namespace**?
   - Пространство, в което са дефинирани обекти
   - Видове:
     - Built-In
     - Global
     - Local

2. Какво е **scope**?
   - Поле на действие, в което един обект е достъпен
   - Видове:
     - Built-In
     - Global
     - Enclosing
     - Local

3. Обекти
   - **Всичко в Python е обект**
   - Обектите се състоят от две основни части:
     - Характеристики (State)
     - Поведение (Behavior)
  ```py
    class MyObject:
        def __init__(self, property1):
            self.property1 = property1  # State

        def doSomething():  # Behavior
            ...
  ```

---

### 02. Classes and Objects

1. Атрибути
   - Data Attributes
     - Instance Attributes -
       - Закачени на инстанцията(self)
       - Уникални за всяка инстанция
     - Class Attributes
       - Закачени на класа
       - Споделени между всички инстанции
   - Methods
     - Функции принадлежящи на класа
    
2. Магически методи
   - **__init__** - използваме за инстанциране на класа
   - **__str__** - използваме за стрингова репрезентация на класа (т.е. вместо <object in memory ...>); извиква се, когато се опитаме да кастнем инстанция към стринг
   - **__repr__** - използваме, за да представим класа като стринг дори при дебъгване (машинна репрезентация)
   - **__dict__** - репрезентира стейта на класа като dictionary
   - **__doc__** - връща документацията на обекта 

---

### 03. Inheritance

1. Какво е наследяване?
   - Наследяването е един от четирите основни стълба на обектно ориентираното програмиране
   - Използваме го, за по-добра абстракция и преизползване на код
   - DRY - **Don't Repeat Yourself**

2. super()
   - **super** представлява първия бащин клас
  
3. Видове наследяване
   - Single
     </br>
     <img src="https://simplesnippets.tech/wp-content/uploads/2018/03/single_inheritance_in_cpp.png" width=400 height=200 />
   - Multiple
     </br>
     <img src="https://media.geeksforgeeks.org/wp-content/uploads/20191222084630/multipleinh.png" width=400 height=200 >
   - Multilevel
     </br>
     <img src="https://media.geeksforgeeks.org/wp-content/uploads/multilevel-inheritance.png" width=400 height=200 >
   - Hierarchical
     </br>
     <img src="https://www.simplilearn.com/ice9/free_resources_article_thumb/Hierarchical_Inheritance_In_C_P_P_Chart.png" width=400 height=200>

4. What is MRO (Method Resolution Order)
   - Depth First Resolve
   - Подрежда наследяваните класове в определен ред.

5. Mixins
   - Миксините са класове, които използваме, за да наследим някаква функционалност в множество класове.
   - Пример:
     - Имаме клас кола и клас фурна
     - Колата и фурната имат часовник, които работи както всички други часовници по света
     - Съответно правим миксин клас часовник, който да наследим в другите 2 класа.

---

### 04. Encapsulation

1. Какво е енкапсулация
   - Пакетирането на данни и методи
   - Да скрием данни или методи от 'външния свят' или да валидираме стойностите, които се опитват да бъдат присвоени

**Енкапуслацията в Python е слаба => нищо не остава скрито**

2. Нива на достъп
   - private
     - Създаваме слагайки **__** пред името на атрибута
     - Подсказва на човека, който чете кода, че този атрибут може да бъде достъпван само в класа
     - Поради слабата енкапслация в Python, можем да го достъпим и извън класа чрез **name mangling** -> _ИметоНаКласа__ИметоНаАтрибута
   - protected
     - Създаваме слагайки **_** пред името на атрибута
     - Подсказва на човека, който чете кода, че този атрибут може да бъде достъпван само в класа и наследяващите го класове
     - Поради слабата енкапсулация, можем да го достъпим навсякъде
   - public
     - По подразбиране, всичко е достъпно навсякъде

3. Getters and Setters
   - Гетърите и сетърите ни позволяват да валидираме какви стойности се присвпяват на нашите атрибути и да конторлираме стойнностите, които се връщат.
   ```py
   @property
   def name(self):  # Getter
      return self.name


   @name.setter
   def name(self, value: str):  # Setter
      if value != "":
         print("Name cannot be empty")
         return

      self.name = value
   ```

   ---

### 05. Static and Class Methods

1. Static Methods
   - Методи, които не използват инстанцията, съответно не я получават като параметър
   - Не знаят нищо за класа и не могат да променят неговия стейт
   - Използваме ги за неща, които бихме написали като функции извън класа
   - Единствената причина да са в класа е, защото по някакъв начин са обвързани с неговата логика или се ползват там
   - Създаваме ги с декоратора **@staticmethod**

   ```py
   @staticmethod
   def is_adult(age):
      return age >= 18
   ```

2. Class Methods
   - Закачени са към самия клас, а не към инстанциите(подобно на class data attributes)
   - Вместо инстанцията, като първи параметър получават класа като обект
   - Създаваме ги с декоратора **@classmethod**

   ```py
   @classmethod
   def create_new_instance(cls, *args):
      return cls(*args)
   ```
      
   ---

### 06. Polymorphism and Abstraction

1. Полиморфизъм
   - Poly(много) - morphism(форми)
   - Пример в програмирането, когато два производни класа имат един и същи метод реализиран по различен начин
   ```py
   class Eagle(Bird):
      def fly(self):
         print("I fly only forward")

   class Hummingbird(Bird):
      def fly(self):
         print("I fly in all directions")
   ```

2. Method Overloading
   - Когато променяме поведението на методи и оператори използвайки магически методи
   - __len__
   - __add__
   - __mul__
   - __truediv__
   - __floordiv__
   - __pow__
   - __eq__
   - __ne__
   - and so on...
  
3. Duck Typing
   - Когато не се интересуваме от типа на обекта, а от това дали той има методите, които искаме

4. Abstraction
   - Да кажем какво прави нещо, без да казваме как го прави
   - В ООП това често се отнася към това да изнесем оща логика в бащини или mixin класове

5. Абстрактни класове
   - Класове, които не се инстанцират и служат като шаблон за наследяващите ги класове
   ```py
   from abc import ABC, abstractmethod

   class Shape(ABC):
   
      @abstractmethod  # задължава наследяващите класове да имплементират този метод 
      def area(self):
         pass

      @abstractmethod  # задължава наследяващите класове да имплементират този метод 
      def perimeter(self):
         pass
   ```

---

### 07. SOLID

**S** - Single Responsibility
**O** - Open/Closed
**L** - Liskov Substitution
**I** - Interface Segregation
**D** - Dependency Inversion

1. Single Responsibility
   - Всеки метод/функция трябва да прави точно едно нещо

2. Open Closed
   - Трябва така да пишем кода си, че той да бъде заторен за модифициране, но отворен за разширение
   - Тоест, когато имаме нова логика, да не трябва да променяме старата, а просто да я добавим

3. Liskov Substitution
   - "Децата трябва да бъдат подходящи за родителите"
   ```py
   from abc import ABC, abstractmethod


   class Notification(ABC):
       @abstractmethod
       def notify(self, message, email):
           pass
   
   class Email(Notification):
       def notify(self, message, email):
           print(f'Send {message} to {email}')
   
   class SMS(Notification):
       def notify(self, message, phone):  # notify метода получава параметър телефон, вместо имейл, което прави класа неподходящ наследник
           print(f'Send {message} to {phone}')
   ```

   Решението:

   ```py
   
   class Notification(ABC):
       @abstractmethod
       def notify(self, message):
           pass

   class Email(Notification):
       def __init__(self, email):
           self.email = email
   
       def notify(self, message):
           print(f'Send "{message}" to {self.email}')
   
   
   class SMS(Notification):
       def __init__(self, phone):
           self.phone = phone
   
       def notify(self, message):
           print(f'Send "{message}" to {self.phone}')
   ```

4. Interface segregation
   - Не трябва да задължаваме класовете ни да имплементират методи, които не ползваме

5. Dependency Inversion
   - Разчитаме на абстракция, а не на конкретна имплементация

   ```py
      from abc import ABC, abstractmethod
   
      class LoggerInterface(ABC):
          @abstractmethod
          def log(self, message):
              pass
      
      class Logger(LoggerInterface):  # Наследяваме Абстрактния клас, за да можем да разчитаме на абстракцията да ни задължи да имплементираме нужните методи
          def log(self, message):
              with open('log.txt', 'a') as f:
                  f.write(message + '\n')
      
      class Calculator:
          def __init__(self, logger: LoggerInterface):
              self.logger = logger
      
          def add(self, x, y):
              result = x + y
              self.logger.log(f"Added {x} and {y}, result = {result}")
              return result
   ```

6. Dependency Injection
   - Когато подадем на метод инсанция на обект от друг клас, за да може тя да свърши нужната работа
---

### 08. Iterators And Generators

1. Какво е итератор?
   - Обект през, който можем да итерираме
   - Връща един елемент на всяка итерация
   - Имплементира итератор протокола, а именно да има __iter__ и __next__ методите в себе си.
   - В __iter__ метода връщаме обекта, през който ще итерираме; Метода се извиква само веднъж при започване на цикъл.
   - В __next__ метода връщаме елемент от обекта, през който итерираме - изпълнява се на всяка итерация.
  
2. Какво е генератор?
   - Функция, която връща итератор
   - Съдържа думата **yield**, която връща стойност както **return**, но също така запазва стейта на функцията.
   - Можем да създаваме генератори чрез фунцкии и чрез компрехеншъни.
   ```py
   (x ** 2 for x in range(10)
   ```

---

### 09. Decorators

1. Какво е декоратор
   - Функция, която обгражда друга функция и я получава като параметър
   ```py
   def print_result_in_brackets(func):  # Тази функция приема функцията под нея като параметъ и я заменя с wrapper фунцкията ни
      def wrapper(*args, **kwargs):
         result = func(*args, **kwargs)
         print(f"({result})")  # връщаме резултата обграден от скоби

      return wrapper

   # Usage
   @print_result_in_brackets
   def get_hi():
      return "Hi"

   get_hi()  # (Hi)
   ```

2. Декоратор с параметър
   ```py
      def print_result_in_brackets(brackets)  # Tази фунцкия приема аргументите на декоратора
         def decorator(func):  # Тази функция приема функцията под нея като параметъ и я заменя с wrapper фунцкията ни
            def wrapper(*args, **kwargs):
               result = func(*args, **kwargs)
               print(f"{brackets[0]}{result}{brackets[1]}")  # връщаме резултата обграден от скоби
   
         return wrapper
      return decorator

      @print_result_in_brackets("[]")
      def get_hi():
         return "Hi"
   
      get_hi()  # [Hi]
   ```

3. Class decorator
   ```py
   class func_logger:
      _logfile = 'out.log'

      def __init__(self, func):
         self.func = func

      def __call__(self, *args):
         log_string = self.func.__name__ + " was called"

         with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')

         return self.func(*args)
   ```
   
---

### 10. Testing 

1. Видове тестване
   - Manual
   - Automated
     - Unit
     - Integration
     - E2E
     ...

2. Какво е unit тестване?
  - Тестване на най-малката единица код (част от функция или функция)

3. Термини
  - Test fixture - среда, в която ще тестваме
  - Test case - един тестов случай
  - Test suite - колекция от тест кейсове
  - Test runner - средството, което използваме за тестване
  - Triple A Pattern - Arrange Act Assert

4. Какво е мокване?
   - Да симулираме действие, което поради определени причини не изпълняваме
  
5. Седем принципа на Тестването
   1. Не можем да тестваме всичко, възможностите са към безкрай
   2. Ранното тестване е винаги предпочитано
   3. Defect Clustering - трябва да тестваме кода ни равномерно
   4. Pesticide paradox - да не тестваме неща, които по някакъв начин вече се тестват
   5. Тестването само намаля шанса да имаме бъгове, но не го премахва
   6. Absence-of-errors - тестването е безполезно, ако нямаме работещ по изискванията на клиента продукт
   7. Тестването е различно при различните видове софтуер



---
заслугите са на: Диян Калайджиев
---
