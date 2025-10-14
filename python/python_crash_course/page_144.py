# 9.1 & 9.2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.curisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐厅名称：{self.restaurant_name}，菜系：{self.curisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业")

restaurant = Restaurant("大董", "烤鸭")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant("海底捞", "火锅")
restaurant2.describe_restaurant()

# 西贝 ^v^
restaurant3 = Restaurant("西贝莜面村", "西北菜")
restaurant3.describe_restaurant()

# 9.3
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        if gender in ['male', 'female']:
            self.gender = gender
        else:   
            self.gender = 'unknown'

    def describe_user(self):
        print(f"用户信息：{self.first_name} {self.last_name}, 年龄：{self.age}, 性别：{self.gender}")

    def greet_user(self):
        print(f"欢迎您，{self.first_name} {self.last_name}！")

user = User("张", "三", 20, "male")
user.describe_user()
user.greet_user()
user2 = User("李", "四", 18, "female")
user2.describe_user()   
user2.greet_user()
user3 = User("王", "五", 22, "unknown") 
user3.describe_user()
user3.greet_user()