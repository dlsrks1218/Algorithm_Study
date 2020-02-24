# 고객 센터에서 상담예약제를 실시합니다. 상담예약제란 예약 고객의 업무를 일반 고객의 업무보다 먼저 처리하는 방식을 말합니다. 상담예약제는 다음과 같은 로직으로 동작합니다.

# 1. 예약 고객 중 먼저 도착한 고객의 업무를 먼저 처리
# 2. 예약 고객이 없으면 먼저 도착한 일반 고객의 업무를 처리
# 3. 단, 시작한 업무는 중간에 중단하지 않음
#     - 즉, 일반 고객의 업무를 처리하는 도중 예약 고객이 온 경우, 일반 고객 업무를 끝낸 후 예약 고객의 업무를 처리함
# 창구는 하나뿐이며 창구에서 업무를 처리하는 데에는 10분이 걸립니다. 이때 창구에서 어떤 손님의 업무를 먼저 처리했는지 알아보려 합니다. 예를 들어 다음과 같이 손님이 들어온 경우

# 도착 시각	손님 이름	예약 여부
# 09:00	kim	예약 안 함
# 09:05	bae	예약 안 함
# 09:10	lee	예약함
# 창구는 다음과 같이 [kim, lee, bae] 순으로 업무를 처리합니다.

# 09:00 ~ 09:10 → kim의 업무를 처리
# 09:10 ~ 09:20 → lee의 업무를 처리
# 09:20 ~ 09:30 → bae의 업무를 처리

# 예약 고객의 도착 시각과 이름을 담은 배열 booked, 일반 고객의 도착 시각과 이름을 담은 배열 unbooked가 매개변수로 주어집니다. 이때 고객의 이름을 업무가 처리된 순으로 담은 배열을 return 하도록 함수를 완성해주세요.

# 제한사항
# booked의 길이는 1 이상 50 이하입니다.
# unbooked의 길이는 1 이상 50 이하입니다.
# booked 배열의 길이와 unbooked 배열의 원소는 [hh:mm 형식의 도착 시각, 이름] 형식입니다.
# hh:mm은 00:01 ~ 23:50 범위 안에서 주어집니다.
# 이름은 길이가 1 이상 5 이하인 문자열입니다.
# 이름은 알파벳 소문자로만 이루어져 있습니다.
# 각 배열은 도착 시각 순으로 정렬되어 있습니다.
# 도착 시각이 같은 고객은 없습니다.
# booked, unbooked 배열에는 오늘 하루 동안 온 고객의 정보만 주어집니다.
# 입출력 예
# booked	unbooked	result
# [["09:10", "lee"]]	[["09:00", "kim"], ["09:05", "bae"]]	["kim", "lee", "bae"]
# [["09:55", "hae"], ["10:05", "jee"]]	[["10:04", "hee"], ["14:07", "eom"]]	["hae", "jee", "hee", "eom"]
# 입출력 예 설명
# 입출력 예 #1

# 앞서 설명한 예와 같습니다.

# 입출력 예 #2

# 09:55 ~ 10:05 → hae의 업무를 처리
# 10:05 ~ 10:15 → jee의 업무를 처리
# 10:15 ~ 10:25 → hee의 업무를 처리
# 14:07 ~ 14:17 → eom의 업무를 처리

def convert_time(t):
    data = t.split(":")
    data[0] = data[0].lstrip("0")
    data[1] = data[1].lstrip("0")
    print(data)
    
    for i in range(len(data)):
        if data[i] == '':
            data[i] = 0

    tominute = int(data[0]) * 60 + int(data[1])

    return tominute

def solution(booked, unbooked):
    timecount = 0
    guestsorder = []
    first_dic = {}
    second_dic = {}
    total_dic = {}

    for i in range(len(booked)):
        temp_key = convert_time(booked[i][0])
        first_dic[temp_key] = booked[i][1]
        total_dic[temp_key] = booked[i][1]

    for j in range(len(unbooked)):
        temp_key = convert_time(unbooked[j][0])
        second_dic[temp_key] = unbooked[j][1]
        total_dic[temp_key] = unbooked[j][1]

    end_count = len(total_dic)
    print(total_dic)

    firstguest = min(total_dic.keys())
    guestsorder.append(firstguest)
    timecount = firstguest + 10

    if firstguest in first_dic:
        del first_dic[firstguest]

    if firstguest in second_dic:
        del second_dic[firstguest]

    while len(guestsorder) <= end_count:
        if len(first_dic) > 0:
            print(first_dic)
            if min(first_dic.keys()) <= timecount:
                nextguest = min(first_dic.keys())
                guestsorder.append(nextguest)
                timecount = timecount + 10
                del first_dic[nextguest]
            else:
                timecount = timecount + 10
                
        elif len(second_dic) > 0:
            if min(second_dic.keys()) <= timecount:
                nextguest = min(second_dic.keys())
                guestsorder.append(nextguest)
                timecount = timecount + 10
                del second_dic[nextguest]
                print(guestsorder)
            else:
                timecount = timecount + 10
                print(second_dic)
                
        else:
            timecount = timecount + 10

        if len(first_dic) == 0 and len(second_dic) == 0:
            break


    output = []

    for i in guestsorder:
        output.append(total_dic[i])

    
    return output

solution([["09:55", "hae"], ["10:05", "jee"]],   [["10:04", "hee"], ["14:07", "eom"]])
