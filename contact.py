# contact.py

# exit() 함수 사용을 위한 sys 모듈 import
import sys
# 파일을 JSON 포맷으로 저장하는 json 모듈 import
import json
# JSON 모듈이 빈 파일을 불러올 때 발생하는 오류 처리 import
from json.decoder import JSONDecodeError

# 전체 연락처를 저장할 딕셔너리 선언
contacts = {}


# 특정 연락처를 알아보기 쉬운 형태로 출력하는 함수
def view_person(key):
    person = contacts.get(key)
    name = person.get("이름")
    number = person.get("전화번호")
    group = person.get("구분")
    view = f'''
이름: {name}
전화번호: {number}
구분: {group}'''
    print(view)


# 연락처 추가
def add_contact():
    name = input("이름을 입력하세요: ")
    while True:
        # 전화번호 입력
        number = input("전화번호를 입력하세요('-' 기호 제외): ")
        # 이미 등록된 전화번호를 입력한 경우
        if number in contacts:
            print("이미 등록된 전화번호입니다.")
            continue
        # 전화번호를 너무 짧거나 너무 길게 입력한 경우
        if len(number) < 9 or len(number) > 12:
            print("전화번호를 잘못 입력하였습니다.")
            continue
        else:
            break
    while True:
        # 구분 입력
        group = input("'가족', '친구', '회사', '기타' 중 하나의 구분을 입력하세요.: ")
        # 구분을 
        if group not in ['가족', '친구', '회사', '기타']:
            print("잘못 입력하셨습니다.")
            continue
        else:
            break
    person = {"이름": name, "전화번호": number, "구분": group}
    contacts[number] = person
    print("아래와 같이 연락처를 추가하였습니다.")
    view_person(number)
    while True:
        print("다른 연락처를 추가하시겠습니까?")
        print("1. 예")
        print("2. 아니오")
        try:
            select = int(input())
        except ValueError as ve:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        if select == 1:
            add_contact()
        elif select == 2:
            main()
        else:
            print("잘못 입력하셨습니다.")
            continue


# 전체 연락처 조회
def list_contact():
    contact_size = len(contacts.keys())
    print(f"총 {contact_size}개의 연락처가 있습니다.\n")
    j = 1
    key_list = list(contacts.keys())
    for k in key_list:
        print(j, end='.')
        view_person(k)
        print()
        j += 1
    main()


def modify_contact():
    keyword = input("검색할 이름을 입력하세요: ")
    result = search_contact(keyword)
    if result:
        while True:
            try:
                select = int(input("어떤 연락처를 수정하시겠습니까? "))
            except ValueError as ve:
                print("잘못 입력하였습니다. 다시 입력하세요.")
                continue
            break
    else:
        print('메인 메뉴로 복귀합니다.')
        main()
    selected_key = result[select - 1]
    view_person(selected_key)
    while True:
        print("이 연락처를 수정하시겠습니까?")
        print("1. 예")
        print("2. 아니오")
        try:
            select = int(input())
        except ValueError as ve:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        if select == 1:
            person = contacts.get(selected_key)
            while True:
                print("어떤 정보를 수정하시겠습니까?")
                print("1. 이름")
                print("2. 전화번호")
                print("3. 구분")
                try:
                    select = int(input())
                except ValueError as ve:
                    print("잘못 입력하였습니다. 다시 입력하세요.")
                    continue
                if select == 1:
                    name = input("이름을 입력하세요: ")
                    person["이름"] = name
                    contacts[selected_key] = person
                    print("수정되었습니다.")
                    print(contacts[selected_key])
                    main()
                elif select == 2:
                    while True:
                        number = input("전화번호를 입력하세요('-' 기호 제외): ")
                        if number in contacts:
                            print("이미 존재하는 전화번호를 다시 입력할 수 없습니다.")
                            continue
                        if len(number) < 9 or len(number) > 12:
                            print("전화번호를 잘못 입력하였습니다. 다시 입력하세요.")
                            continue
                        else:
                            person["전화번호"] = number
                            contacts[number] = person
                            del contacts[selected_key]
                            print("수정되었습니다.")
                            main()
                            break
                elif select == 3:
                    while True:
                        group = input("'가족', '친구', '회사', '기타' 중 하나의 구분을 입력하세요.: ")
                        if group not in ['가족', '친구', '회사', '기타']:
                            print("잘못 입력하셨습니다.")
                            continue
                        else:
                            person["구분"] = group
                            contacts[selected_key] = person
                            print("수정되었습니다.")
                            main()
                            break
                else:
                    print("잘못 선택하였습니다.")
                    continue
        elif select == 2:
            print("메인 메뉴로 복귀합니다.")
            main()
        else:
            print("잘못 입력하셨습니다.")
            continue


def delete_contact():
    keyword = input("검색할 이름을 입력하세요: ")
    result = search_contact(keyword)
    if result:
        while True:
            try:
                select = int(input("어떤 연락처를 삭제하시겠습니까? "))
            except ValueError as ve:
                print("잘못 입력하였습니다. 다시 입력하세요.")
                continue
            break
    else:
        print('메인 메뉴로 복귀합니다.')
        main()
    selected_key = result[select - 1]
    view_person(selected_key)
    while True:
        print("이 연락처를 삭제하시겠습니까?")
        print("1. 예")
        print("2. 아니오")
        try:
            select = int(input())
        except ValueError as ve:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        if select == 1:
            del contacts[selected_key]
            print("삭제하였습니다. 메인 메뉴로 복귀합니다.")
            main()
        elif select == 2:
            print("삭제하지 않았습니다. 메인 메뉴로 복귀합니다.")
            main()
        else:
            print("잘못 입력하였습니다.")
            continue


def search_contact(keyword):
    result = []
    for k in list(contacts.values()):
        if keyword == k.get("이름"):
            result_key = k.get("전화번호")
            result.append(result_key)
    result_size = len(result)
    if result_size:
        print(f'총 {result_size}개의 연락처를 발견하였습니다.\n')
        j = 0
        while j < result_size:
            print(j + 1, end='.')
            view_person(result[j])
            j += 1
        return result
    else:
        print("해당 검색어로 연락처를 찾지 못하였습니다.")


def main():
    menu_text = '''
===============================
      연락처 관리 프로그램
===============================
1. 회원 추가
2. 회원 목록 보기
3. 회원 정보 수정하기
4. 회원 삭제
5. 종료
'''
    print(menu_text)
    while True:
        try:
            selection = int(input("위 메뉴 중 하나를 선택하세요: "))
        except ValueError as ve:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue
        if selection == 1:
            add_contact()
        elif selection == 2:
            list_contact()
        elif selection == 3:
            modify_contact()
        elif selection == 4:
            delete_contact()
        elif selection == 5:
            print("프로그램을 종료합니다.")
            json_data = open('contacts.json', 'w', encoding='utf-8')
            json_dump = json.dumps(contacts, ensure_ascii=False, indent=4, separators=(',', ':'))
            json_data.write(json_dump)
            json_data.close()
            sys.exit()
        else:
            print("잘못 입력하였습니다. 다시 입력하세요.")
            continue


# 프로그램 실행시 JSON 파일 불러오기
try:
    json_data = open('contacts.json', 'r', encoding='utf-8')
# 기존 JSON 파일이 존재하지 않는 경우 JSON 파일 생성 후 다시 불러오기
except FileNotFoundError:
    json_data = open('contacts.json', 'w', encoding='utf-8')
    json_data = open('contacts.json', 'r', encoding='utf-8')

# 내용이 없는 JSON 파일을 불러오는 경우의 예외 처리
try:
    contacts = json.load(json_data)
except JSONDecodeError:
    pass

main()
