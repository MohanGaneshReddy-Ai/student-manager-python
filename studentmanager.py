import json 
def starting_part():

    print("                                   ")
    print("========student manager============")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.delete student")
    print("5.update student")
    print("6.exit")
students={}

def add_students(students): 
    name=input("enter student name:") 
    age=int(input("enter your age:")) 
    year=int(input("enter your year:")) 
    students[name] = {
    "age": age,
    "year": year
}
    save_students(students)
def save_students(students):
    with open('my_data.json','w') as f:
      json.dump(students,f,indent=4)

    print("student added successfully") 

def view_students(students): 
    if not students: 
        print("no students found") 
    else: 
      for name,details in students.items(): 
        print(f"""
        Name:"{name}
        Age:"{details["age"]}
        Year:"{details["year"]}
         """)

def search_students(students): 
    name=input("enter your search name:") 
    if name in students: 
        age = students[name]["age"]
        year = students[name]["year"]
        print(f"name:{name},age:{age},year:{year}")
    else: 
        print("student not found")
def delete_students(students):
    name=input("enter name to delete:")
    if name in students:
        del students[name]
        save_students(students)
        print("student deleted succesfully")

def update_students(students):
    name=input("enter user name to update:")
    if name in students:
        new_age=int(input("enter you age:"))
        students[name]["age"]=new_age
        new_year=int(input("enter you year:"))
        students[name]["year"]=new_year
        save_students(students)
    else:
        print("name not found")



def load_student():
    try:
     with open('my_data.json','r') as f:
        return json.load(f)
    except FileNotFoundError:
     return{}
students=load_student()

while True: 
    #print("-----------students list------------ ")
    #print(students)
    starting_part()
    choice=int(input("enter your choice:")) 
    if choice==1: 
        add_students(students) 
    elif choice==2: 
        view_students(students) 
    elif choice==3: 
        search_students(students) 
    elif choice==4: 
        delete_students(students)
    elif choice==5:
        update_students(students)
    elif choice==6:
        print("exiting the prgram")
        break 
    else: 
        print("invalid choice") 