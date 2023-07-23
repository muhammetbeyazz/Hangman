my_text = "yazılım"
my_list = ["y", "a", "z", "ı", "l", "ı", "m"]
kalan_hak = 3
bul_list = ["-", "-", "-", "-", "-", "-", "-"]

name = input("Adınız Nedir ?\n")
print("Adam Asmaca Oyununa Hoş Geldin " + name + " Başarılar Dileriz..")
print("!! Toplamda 4 Hakkınız Bulunmaktadır !!")

while kalan_hak > 0:
	
	for x in bul_list:
		print(x),
	
	if bul_list == my_list:
		print("WİCTORY ! :)")
		break
	else:
		letter = input("Lütfen Bir Harf Tahmini Giriniz : ")	
		if letter == my_text[0]:
			bul_list[0] = my_text[0]
		elif letter == my_text[1]:
			bul_list[1] = my_text[1]
		elif letter == my_text[2]:
			bul_list[2] = my_text[2]
		elif letter == my_text[3]:
			bul_list[3] = my_text[3]
			bul_list[5] = my_text[5]
		elif letter == my_text[4]:
			bul_list[4] = my_text[4]
		elif letter == my_text[6]:
			bul_list[6] = my_text[6]
		else:
			if kalan_hak == 0:
				print("HATA! \tTüm Hakkınızı Kullandınız :( \nBulunan Harfler : ")
				for y in bul_list:
					print(y)
				print("GAME OVER !!")
				break
			else: 	
				print(f"Hata!\n {kalan_hak} Hakkınız Kaldı :(")
				kalan_hak -= 1
""" 
yukarda kendim yaptığım algoritma çokta mantıklı değil çünkü her kelimeye uygun değil bunun
için aşşağıdaki algoirtma çok daha mantıklıdır.
"""

"""
name = input("Enter name: ")
print("Hello " + name + " time to play hangman!")

secret_word = "Metallica"

guess_string = ""

lives = 10

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string:

			print(character)
		else:
			print("-")
			character_left += 1

	if character_left == 0:
		print("You won!!!")	
		break

	guess = input("Guess a word: ")
	guess_string += guess

	if guess not in secret_word:
		lives -= 1
		print("Wrong!")
		print(f"You have {lives} left")

		if lives == 0:
			print("You died!")

"""