import json
import requests
def courses():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    print(a)
    a1 = a.text
    # print(type(a1))
    # print(a1)
    # b1=a.json()
    # print(b1)
    print("------------------------")
    with open("courses.json","w") as f:
         python_dict=json.loads(a1)# string convert into python 
        #  print(type(python_dict))
         json.dump(python_dict,f,indent=4)# python object have to store in a file
    with open("courses.json","r") as f:
         data = json.load(f)#read to python object from a file object
        #  print(data)
    id_of_courses = [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i,".",data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id_of_courses.append(data['availableCourses'][i]['id'])
        i+=1 
    # print(id_of_courses)

    select_course = int(input("select the course u want by selecting cooresponding number:"))
    excercises = requests.get("http://saral.navgurukul.org/api/courses/"+str(id_of_courses[select_course])+"/exercises")
    a=excercises.json()
    # print(a)
    print(a["data"])
    j=0
    l=0
    list_of_slug=[]
    while j<len(a["data"]):
        print(l,":",a["data"][j]["name"])
        list_of_slug.append(a['data'][j]["slug"])
        l+=1
        j=j+1

    slug_num=int(input("choose the correspionding slug number"))
    slug_list=requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num])
    b=slug_list.json()
    print("content:",b["content"]) 
    # next_step = input("coose your next step:")
    i=0
    while i<len(list_of_slug):
        next_step = input("choose your next step:")
        if next_step == "up":
            slug_list=requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num])
            l=slug_list.json()
            print(slug_num,l["content"])
            
            
        elif next_step == "prev":
            # slug_num-=1
            slug_list = requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num-1])
            b=slug_list.json()
            print(slug_num-1,"content:",b["content"]) 
        elif next_step == "next":
            # slug_num+=1
            slug_list = requests.get("http://saral.navgurukul.org/api/courses/"+ str(select_course )+"/exercise/getBySlug?slug=" + list_of_slug[slug_num+1])
            k=slug_list.json()
            print(slug_num+1,"content:",k["content"]) 
        elif next_step == "exit":
            courses()
courses()
    
