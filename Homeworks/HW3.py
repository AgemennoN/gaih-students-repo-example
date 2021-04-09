# Explain your work
"""
Passing Grade isimli fonksiyon tanımladım girdileri Midterm notu, Proje notu ve Final notu
Çıktısı ise Passing Grade
takeSecond fonksiyonu iki boyutlu arrayin 2. ikdeksine göre sıralamak için oluşturduğum bi fonksiyon

5 tane Dictionary tanımladım Students1:5, Bunları bir Listeye attım Student_Dict_List
döngü ile bu listenin içindeki dictionary leri her bir öğrenci için kullanıcıdan istedim
Student1(İsim: İsim,Midterm: Midterm,Final: Final, Passinggrade: Passing_Grade()) Şeklinde

Yeni bir liste oluşturup(Student_List) bu listenin içine öğrencilerin isimlerini ve Passing Gradelerini attım
.sort methodu ile yüksek nottan düşük nota göre sıraladım.

        İlk başta Class ile yapmaya başlamıştım ama çok tecrubeli olmadığım için yarım bırakmıştım
        Geri dönüp o şekilde de yapmak istedim ve İlk yaptığım kısmı yorum satırı olarak bıraktım
        Açıklamanın kalan kısmını aşağıya yazıyorum

Student isimli class tanımladım oluştururken isim ve notlarını girmemiz gerekiyor ve
Passing grade isimli bir method tanımladım girilen notlardan Geçme notunu hesaplıyor.

For döngüsü ile bir listeye öğrencileri koyuyorum. En son başka bir listeye isimleri ile
geçme notlarını atıyorum. ve o listede notlara göre sıralama yaptırıyorum.

"""

# Question
"""
def Passing_Grade(Midterm,Project,Final):
    return (Midterm * 0.3) + (Project * 0.3) + (Final * 0.4)

def takeSecond(A):
    return A[1]

Students1 = {}
Students2 = {}
Students3 = {}
Students4 = {}
Students5 = {}

Student_Dict_List = [Students1, Students2, Students3, Students4, Students5]
Student_List = []

for i in range(5):
    print(f"\nStudent #{i+1}")
    Student_Dict_List[i].update({"Name": input('Enter Name of the Student: ')})
    Student_Dict_List[i].update({"Midterm": input('Enter Midterm Grade of The Student: ')})
    Student_Dict_List[i].update({"Project": input('Enter Project Grade of The Student: ')})
    Student_Dict_List[i].update({"Final": input('Enter Final Grade of The Student: ')})
    Student_Dict_List[i].update({"PassingGrade": Passing_Grade(float(Student_Dict_List[i].get("Midterm")),
                                                               float(Student_Dict_List[i].get("Project")),
                                                               float(Student_Dict_List[i].get("Final")))})
    Student_List.append([Student_Dict_List[i].get("Name"),Student_Dict_List[i].get("PassingGrade")])

Student_List.sort(key=takeSecond, reverse=True)

print(Student_List)
#print(Student_Dict_List)
"""



# Extra Part
class Student:
    def __init__(self, Name, Midterm, Project, Final):
        self.Name = Name
        self.Midterm = Midterm
        self.Project = Project
        self.Final = Final

    def passing_grade(self):
        Passing_Grade = (self.Midterm * 0.3) + (self.Project * 0.3) + (self.Final * 0.4)
        return Passing_Grade


def takeSecond(A):
    return A[1]


Student_Class_list = []
Student_List = []

for i in range(2):
    Student_Class_list.append(Student("", "", "", ""))
    print(f"\nStudent #{i + 1}")
    Student_Class_list[i].__init__(input("Enter Name of the Student: "),
                                   float(input("Enter Midterm Grade of The Student: ")),
                                   float(input("Enter Project Grade of The Student: ")),
                                   float(input("Enter Final Grade of The Student: ")))
    Student_List.append([Student_Class_list[i].Name, Student_Class_list[i].passing_grade()])

Student_List.sort(key=takeSecond, reverse=True)

print(Student_List)
# print(Student_Dict_List)
