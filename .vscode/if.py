#print("python", "java", sep=" vs ")
# print("python", "java", sep=" , ", end="? ")
# print("무엇이 더 재밌을까요?")

# scores = {"math" :0, "english" :1, "coding" :100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")



# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

#     answer = input("아무 값이나 입력하세요 : ")
#     print(" 입력하신 값은 " + answer + "입니다")

# print("{0: >+10}" .format(500))
# print("{0: >+10}" .format(500))
# print("{0: >+10}" .format(-500))


# print("{0:*<+10}" .format(500))
# print("{0: ,}" .format(100000000000))
# print("{0:+,}" .format(100000000000))
# print("{0:+,}" .format(-100000000000))


# print("{0:^<+30,}" .format(10000000000))

# print("{0:f}" .format(5/3))
# print("{0:.2f}" .format(5/3))


# score_file= open("score.txt", "a", encoding="utf8")
# score_file.write("science : 80")
# score_file.write("\ncoding: 100")
# score_file.close()

#파일은 읽고 나면 항상 close

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "박명수", "나이" :30, "취미" :["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()





# for i in range(1,5):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무요약 : ")






name = "마린"
hp = 40
damage = 5

print("{}유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}\n" .format(hp, damage))



