# variables
age = 22
name = "Ali Raza Khan"
CGPA = 2.9
is_Student = True
print("My name is",name,"and my age is",age,"and my CGPA is",CGPA,"and it is",is_Student,"that I am a student.")


#Dictionaries (The Heart of APIs & JSON)

#key-valued pairs 
student = {"name":"Ali Raza Khan",
           "age":22,
           "CGPA":2.9,
           "skills":["python","java","c++"],
           "is_Student":True    }
print(student["name"])
print(student["age"])
print(student["CGPA"])
print(student["skills"])
print(student["is_Student"])

# Functions (indentation is king)
def calculate_square(base_pay, bonus):
    total = base_pay + bonus
    return total
salary = calculate_square(5000, 1000)
print(salary)


# classes & Objects (OOP - MLOps is important)
class MLModel:
    # constructor
    def __init__(self, model_name):
        self.name = model_name # Object Variable

    # method
    def predict(self,data):
        return f"{self.name} predicted {data * 2}"  
# create a object of MLModel class
my_model = MLModel("XGBoost")

# call the predict method
result = my_model.predict(5)
print(result) # Output: XGBoost predicted 10O

# IF/Else statements and Loops

#if/else statement
score = 85
if score >= 90:
    print("Excellent!")
elif score >= 80:
    print("Good!")
else:
    print("Keep practicing!")

# For loops
tools = ["Python", "FastAPI", "Docker", "kubernetes"]
for tool in tools:
    print(tool)
