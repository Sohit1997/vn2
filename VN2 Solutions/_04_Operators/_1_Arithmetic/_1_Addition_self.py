#Addition
'''
# Requirement*/Task*/Ticket*/Story/Incident/Service Request
        Requirement : Adding Numbers

1.Count    : Only 2 numbers or more
2.Type     : Only Positive or only Negative or both Pos,Neg
3.Datatype : Only Int. Int/Float
4.Zero     : 0 is allowed or not

Scenarios:      I. Based on count
                            1. 2 numbers  (Robot)  4 + 5 = __9___
                            2. 3/4/5 numbers
                        II. Based on type
                            1. Both positive
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number(pos/neg), 0
                        III. Based on datatype
                            1. Both int
                            2. Both float
                            3. int + float
                            4. float + int
'''

print("================I. ADDITION OF NUMBERS================")
print("----------------SCENARIOS-----------------")

# Different use cases/scenarios
print("================I. Based on Count================")
print("------1. 2 Numbers------")
   # 1.STATE
x=50
y=70
   # 2.BEHAVIOR
result = x+y
  # 3. Display Result To end User
print("Addito: ",result)

print("------2. 3 or more  Numbers------")
x=50
y=70
z=90
result= x+y+z
print("Addition: ", result)
'''
                        II. Based on type
                            1. Both positive 
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number, 0 (pos/neg)
                            '''
print("================II. Based on Type================")
print("------1 Both positive------")
x=50
y=70
result=x+y
print("Both positive :" , result)

print("------2 Both negative------")
x=-15
y=-20
result=x+y
print("Both Negative :", result)

print("------3. First positive, Second negative ------")
x =  24
y = -30
res = x+y
print("3. First positive, Second negative: ", res)

print("------4. First negative, Second positive ------")
x = -24
y = 30
res = x+y
print("4. First negative, Second positive", res)

print("------5. Zero,Pos Number------")
x = 0
y = 50
res = x+y
print("Addition is : ", res)

print("------5. Zero,Neg Number------")
x = 0
y = -90
res = x+y
print("Addition is : ", res)

print("------6. Pos Number, Zero------")
x = 80
y = 0
res = x+y
print("Addition is : ", x+y)

print("------6. Neg Number, Zero------")
x = -70
y = 0
res = x+y
print("Addition is : ", res)

'''
                        III. Based on datatype
                            1. Both int
                            2. Both float 
                            3. int + float 
                            4. float +   int      
'''
print("================III. Based on DataType================")
print("--------1. Both Integers--------")
x = 80
y = 100
res = x+y
print("Addition is : ", res)

print("--------2. Both Float--------")
x = 80.5
y = 20.7
res = x+y
print("Addition is : ", res)

print("--------3. Int , Float--------")
x = 80
y = 20.7
res = x+y
print("Addition is : ", res)

print("--------4. Float, Int--------")
x = 30.5
y = 20
res = x+y
print("Addition is : ", res)
#---------------------------------------------------------------------

print("---------Realtime Scenarios-----------------")
'''I. Based on count
                            1. 2 numbers  (Robot)  4 + 5 = __9___
                            2. 3/4/5 numbers'''
print("------I. Based on Count---------------")
print("----1. 2 Numbers" )
 #1.State
physics_marks = 75
chemistry_marks=85
#2.Behavior
total_marks=physics_marks+chemistry_marks
#3. Display result to end user
print("Total Marks :", total_marks)

print("-----2. 3 or more marks")
physics_marks=85
chemistry_marks=75
hindi_marks=90
maths_marks=100

total_marks= physics_marks+chemistry_marks+maths_marks+hindi_marks
print("Total marks "  ,total_marks)

'''
 II. Based on type
                            1. Both positive 
                            2. Both negative
                            3. First positive, Second negative
                            4. First negative, Second positive
                            5. 0,  number(pos/neg)
                            6. number(pos/neg), 0 
                            '''

print(" ---------1.both positive---------")
physics_marks=75
chemistry_marks=85
total_marks=physics_marks+chemistry_marks
print("The total marks of two subject is ",total_marks)

print("--------2.Both Float---------")
physics_marks=60.50
chemistry_marks=70.50
total_marks=physics_marks+chemistry_marks
print("The addition of two  subject marks is ",total_marks)

print("===========3.Int,Float===========")
physics_marks=75
chemistry_marks=70.50
total_marks=physics_marks+chemistry_marks
print("The addition of two subject marks is  : ",total_marks)

print("=========4. Float,Int===========")

physics_marks=75.50
chemistry_marks=50
total_marks=physics_marks+chemistry_marks
print("The addition of two subject marks is : ",total_marks)

print("===============================================")

print("-----------------------I.Based on Count--------------")
'''no_shirts=int(input("enter quantity of shirts  :"))
   no_paints=int(input("enter quantity of paints :"))
result =no_shirts+no_paints
print("addition: " ,result)'''

print("------more items-------")
books=50
pencils=5
pens=4
copies=6
total=books+pencils+pens+copies
print("total number of items is ",total)


