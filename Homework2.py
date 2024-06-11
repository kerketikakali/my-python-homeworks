# **********************************************************************************
# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი
# იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება:
# „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება:
# „სწორია!“
# **********************************************************************************

# print("\nრომელი იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს დღესაც?\n")
#
# print("სავარაუდო პასუხები: \n"
#       "1. შუმერთა\n"
#       "2. სელჩუკთა\n"
#       "3. რომის\n"
#       "4. მონღოლთა\n")
# print(" გაითვალისწინეთ: შეიყვანეთ მხოლოდ სწორი პასუხის რიგითი ნომერი ან თავად სწორი პასუხი: \n")
# answer = input()
#
# if answer == "3" or answer == "რომის":
#     print("სწორია")
# elif answer == "1" or answer == "შუმერთა":
#     print("არა! სწორი პასუხია რომის!")
# elif answer == "2" or answer == "სელჩუკთა":
#     print("არა! სწორი პასუხია რომის!")
# elif answer == "4" or answer == "მონღოლთა":
#     print("არა! სწორი პასუხია რომის!")
# else:
#     print("შეყვანილი პასუხი არასწორა")


#____________________________________

#**************************************************************************************************
# 2. ონლაინ მაღაზია
# პროგრამა გთავაზობს პროდუქტის სამ კატეგორიას.
# მაგ.
# 1. ლეპტოპები
# 2. პერსონალური კომპიუტერები
# 3. მობილურები
# მომხმარებელი ირჩევს ერთ-ერთს.
# პროგრამა ითხოვს მაქსიმალურ ბიუჯეტს და ბიუჯეტის მიხედვით სთავაზობს
# მომხმარებელს კონკრეტულ მოდელს არჩეულ კატეგორიაში.
# (თითო კატეგორიაში მინიმუმ 3 პროდუქტი მაინც უნდა იყოს)
#
# თუ ბიუჯეტი ძალიან მცირეა, პროგრამა ბეჭდავს, რომ ამ თანხაში არ გააჩნია
# შემოთავაზება.
#**************************************************************************************************

# print("\nwelcome to our online shop! \n"
#       "please select the category you want to choose the product from: \n"
#       "1) Laptops\n"
#       "2) PC\n"
#       "3) Cell phones\n ")
# category = input().lower()
#
# print("please, enter your maximum budget")
# MaxBudget = int(input())
#
# if category == "laptops":
#     if MaxBudget >= 450:
#         print("Dell Inspiron 15: 500 $\nHP Pavilion x360: 600$\nLenovo Ideapad 3: 450\n")
#     elif MaxBudget >= 500:
#         print("Dell Inspiron 15: 500 $\nHP Pavilion x360: 600$\n")
#     elif MaxBudget >= 600:
#         print("HP Pavilion x360: 600$\n")
#     else:
#         print("product not found")
# elif category == "pc":
#     if MaxBudget >= 480:
#         print("Apple Mac Mini: 700\nAcer Aspire TC: 550\nAsus VivoMini: 480\n")
#     elif MaxBudget >= 550:
#         print("Apple Mac Mini: 700\nAcer Aspire TC: 550\n")
#     elif MaxBudget >= 700:
#         print("Apple Mac Mini: 700\n")
#     else:
#         print("product not found")
# elif category == "cell phones":
#     if MaxBudget >= 700:
#         print("iPhone 12': 800\nSamsung Galaxy S21: 750\nGoogle Pixel 5: 700\n")
#     elif MaxBudget >= 750:
#         print("iPhone 12': 800\nSamsung Galaxy S21: 750\n")
#     elif MaxBudget >= 800:
#         print("iPhone 12': 800\n")
#     else:
#         print("product not found")
# else:
#     print(" write the category correctly! ")


#***************************************************************************************
# 3. ქუესთის შედგენა (Text Based Adventure Game)
# დაწერე ერთმანეთში ჩასმული if-else კონსტრუქციების
# გამოყენებით მარტივი ტექსტზე დაფუძნებული სათავგადასავლო თამაში.
# მაგ. თავიდან პროგრამა ბეჭდავს მომხმარებლის ადგილსამყოფელს და სთავაზობს
# მქომედების რამდენიმე ვარიანტს. სხვადასხვა არჩევანის შემთხვევაში თამაშ
# სხვადასხვანაირად ვითარდება.

# კატა-თაგვობანა
# 1. აირჩიეთ რომელ ოთახში იმყოფება ფისო: საძინებელი,სხვენი,მარანი, სამზარეულო
# 2. აირჩიეთ თქვენი კატა მებრძოლია თუ ნებიერი
# 3. თუ კატა საძინებელშია  სძინავს
# 4. თუ კატა სხვენშია  კაკალს ათამაშებს ან ციყვს დასდევს
# 5. თუ კატა  მარანშია  ხორბალში სძინავს ან  თაგვი დაიჭირა
# 6. თუ კატა სამზარეულოშია პედიგრს ჭამს
#***************************************************************************************

# print("მიყევით ინსტრუქციებს და გაიგეთ რას საქმიანობს თქვენი კატა ")
# print("აირჩიეთ შესაბამისი რიცხვი, რომელ ოთახში იმყოფება კატა?:\n1. საძინებელი\n2.სხვენი\n3.მარანი\n4.სამზარეულო ")
# location = input()
# print("აირჩიეთ შესაბამისი რიცხვი, როგორია თქვენი კატის ხასიათი:\n1.ნებიერი \n2. მებრძოლი")
# character = input()
#
# if location == "1":
#     print("სძინავს")
# elif location == "2":
#     if character == "1":
#         print("კაკალს ათამაშებს")
#     elif character == "2":
#         print("ციყვს დასდევს")
#     else:
#         print("incorrect number")
# elif location == "3":
#     if character == "1":
#         print("ხორბალში სძინავს")
#     elif character == "2":
#         print("თაგვი დაიჭირა")
#     else:
#         print("incorrect number")
# elif location == "4":
#     print("პედიგრს ჭამს")
# else:
#     print("incorrect number ")


#_______________________________________________
#*****************************************************************************************************
#4. კარიერის შემრჩევი (არასავალდებულო დავალება)
# პროგრამა უსვამს მომხმარებელს რამდენიმე კითხვას
# (თქვენი იმპროვიზაციით) და ურჩევს მისთვის შესაფერის
# პროფესიას.

# 1. You find it easy to make new friends? agree, neutral, disagree
# 2. You could spend days learning about random things that interest you.
# 3. You stay cool, calm, and collected even when under lots of stress.
# 4. You’re a sentimental type of person.
# 5. You easily spark up a conversation with a stranger.

#*****************************************************************************************************

# print("answer the following questions and plan your career\n")
# questions = ["1. You stay cool, calm, and collected even when under lots of stress.",
# "2. You easily spark up a conversation with a stranger."]
#
# answers =" 1) agree\n 2) neutral\n 3) disagree\n"
# Ans1 = ""
# Ans2 = ""
# while True:
#    i = 1
#    while i <= len(questions):
#       print(questions[i-1],"\n")
#       print(answers)
#       if i ==1:
#          Ans1 = input()
#       else:
#          Ans2 = input()
#       i +=1
#
#    if Ans1 == "1" and Ans2 == "1":
#        print("international relations specialist")
#    elif Ans1 == "1" and Ans2 == "2":
#        print("banker")
#    elif Ans1 == "1" and Ans2 == "3":
#        print("programmer")
#    elif Ans1 == "2" or Ans2 == "1":
#        print("teacher")
#    elif Ans1 == "3" or Ans2 == "1":
#        print("youtuber")
#    elif Ans1 == "3" and Ans2 == "2":
#        print("you have to start your online business")
#    else:
#        print("we could not find  any profession suitable for you")


