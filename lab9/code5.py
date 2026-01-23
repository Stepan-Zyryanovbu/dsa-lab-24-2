def create_report(name, age, department, salary, bonus, performance_score):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {department}")
    print(f"Salary: {salary}")
    print(f"Bonus: {bonus}")
    print(f"Performance Score: {performance_score}")



def create_report(data):
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"Department: {data['department']}")
    print(f"Salary: {data['salary']}")
    print(f"Bonus: {data['bonus']}")
    print(f"Performance Score: {data['performance_score']}")

#с присером использования нового кода
employee = { 
    "name": "Ivan",
    "age": 23,
    "department": "IT",
    "salary": 70000,
    "bonus": 5000,
    "performance_score": 8
}

create_report(employee)


