#Explain your work
"""
										Question 1
İlk soru için swap array isimli bir fonksiyon tanımladım. Bu fonksiyon arrayin başından uzunluğunun
yarısına kadar olan değerleri bir geçici değişkene atıyor. Bu atanan kısmı Arrayin geri kalanı ile
dolduruyor. En son da yarısından sonrası için geçici değişkenden değerleri geri alıyor.
										Question 2
Kullanıcıdan değer istedim, bu değere kadar olan tüm sayıların 2 ye bölümünden kalanı 0 olanları bastırdım.
"""
#Question 1
def swap_array(Array): #Function that swaps the first half of the array with the second half
	temp = Array[0:int(len(Array)/2)] #int, rounds the float value to an even integer..9/2 = 4.5, int(4.5) = 4
	Array[0:int(len(Array)/2)] = Array[int(len(Array)/2):len(Array)]
	Array[int(len(Array) / 2):len(Array)] = temp
	return Array

print("\nQuestion 1")
Array = [2,3,4,5,"One","Two","Three","Four","Five"]
print(Array)
swap_array(Array)
print(Array)

#Question 2
print("\nQuestion 2")
n = int(input("Enter a single digit number: "))
for i in range(n+1):
	if i % 2 == 0:
		print(i)

