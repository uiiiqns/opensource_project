import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser
from datetime import datetime
import os

root = tk.Tk()
root.title("고민사거리 한눈에 보기")
root.geometry("1200x600")

#왼쪽 프레임 설정
left_frame = tk.Frame(root, width=400, height=600, padx=10, pady=10, bg="white")
left_frame.pack(side=tk.LEFT, fill=tk.Y)
left_frame.pack_propagate(False)

#오른쪽 프레임 설정
right_frame_outer = tk.Frame(root, padx=10, pady=10)
right_frame_outer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_frame_outer.pack_propagate(False)

canvas = tk.Canvas(right_frame_outer)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(right_frame_outer, orient="horizontal", command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas.configure(xscrollcommand=scrollbar.set)

right_frame1 = tk.Frame(canvas)
right_frame2 = tk.Frame(canvas)
right_frame3 = tk.Frame(canvas)
right_frame4 = tk.Frame(canvas)
right_frame5 = tk.Frame(canvas)
canvas.create_window((0, 0), window=right_frame1, anchor='nw')
canvas.create_window((0, 150), window=right_frame2, anchor='nw')
canvas.create_window((0, 200), window=right_frame3, anchor='nw')
canvas.create_window((0, 250), window=right_frame4, anchor='nw')
canvas.create_window((0, 400), window=right_frame5, anchor='nw')

def update_scrollregion():
    canvas.configure(scrollregion=canvas.bbox("all"))

right_frame1.bind("<Configure>", lambda e: update_scrollregion())
right_frame2.bind("<Configure>", lambda e: update_scrollregion())
right_frame3.bind("<Configure>", lambda e: update_scrollregion())
right_frame4.bind("<Configure>", lambda e: update_scrollregion())
right_frame5.bind("<Configure>", lambda e: update_scrollregion())

left_label = tk.Label(left_frame, text="고민사거리\n한눈에 보기", font=("Arial", 16, "bold"), bg="white")
left_label.pack(pady=20)

food_type_label = tk.Label(left_frame, text="원하는 음식 종류 고르기 !!", font=("Arial", 12), bg="white")
food_type_label.pack(anchor='w')

food_type_note = tk.Label(left_frame, text="- 선택하신 종류를 판매하는 식당을 보여줍니다.", font=("Arial", 10), bg="white")
food_type_note.pack(anchor='w', padx=20)

buttons_frame_line1 = tk.Frame(left_frame, bg="white")
buttons_frame_line1.pack(pady=10)

buttons_frame_line2 = tk.Frame(left_frame, bg="white")
buttons_frame_line2.pack(pady=10)

food_types_line1 = ["한식", "중식", "양식"]
food_types_line2 = ["일식", "그 외"]

restaurant_buttons = {}  # 버튼을 저장할 딕셔너리

# 각 음식 종류 버튼의 상태를 추적하는 변수
food_type_states = {
    "한식": False,
    "중식": False,
    "양식": False,
    "일식": False,
    "그 외": False
}

# 버튼 색상을 변경하는 함수
def toggle_button_colors(food_type, food_names, color):
    food_type_states[food_type] = not food_type_states[food_type]
    for name in food_names:
        if name in restaurant_buttons:
            restaurant_buttons[name].configure(bg=color if food_type_states[food_type] else "SystemButtonFace")

# 음식 종류 버튼 클릭 이벤트 처리 함수
def highlight_korean_food():
    korean_foods = ["김가네", "한솥", "1F 밀알식당", "2F 내가찜한닭", "손칼국수", "1F 청운", "먹돼지", "고기스토리", "일품양평해장국",
                    "백채김치찌개", "신의주찹쌀순대", "코웍비스트로", "파라다이스", "889상도", "고기마을찌개나라", "2F 찌개대학부대과",
                    "명품고향삼계탕", "더진국수육국밥", "2F 설쌈냉면", "1F 현선이네"]
    toggle_button_colors("한식", korean_foods, "#A9E2F3")

def highlight_chinese_food():
    chinese_foods = ["2F 취향", "2F 샹츠마라", "2F 황궁쟁반짜장", "2F 연래춘"]
    toggle_button_colors("중식", chinese_foods, "#F79F81")

def highlight_western_food():
    western_foods = ["샤로스톤", "스톤504", "프랭크버거", "크라이치즈버거", "맥도날드", "프레드피자", "뚝배기스파게티"]
    toggle_button_colors("양식", western_foods, "#F2F5A9")

def highlight_japanese_food():
    japanese_foods = ["2F 초밥이야기", "긴자료코", "면식당", "은화수식당", "쑝쑝돈까스", "도쿄라멘3900", "1F 핵밥", "스몰하우스", "1F 멘동", "왕돈까스왕냉면"]
    toggle_button_colors("일식", japanese_foods, "#BCF5A9")

def highlight_other_food():
    all_restaurants = list(restaurant_buttons.keys())
    other_foods = [name for name in all_restaurants if name not in
                   ["김가네", "한솥", "1F 밀알식당", "2F 내가찜한닭", "손칼국수", "1F 청운", "먹돼지", "고기스토리", "일품양평해장국",
                    "백채김치찌개", "신의주찹쌀순대", "코웍비스트로", "파라다이스", "889상도", "고기마을찌개나라", "2F 찌개대학부대과",
                    "명품고향삼계탕", "더진국수육국밥", "2F 취향", "2F 샹츠마라", "2F 황궁쟁반짜장", "2F 연래춘", "샤로스톤", "스톤504",
                    "2F 초밥이야기", "긴자료코", "면식당", "은화수식당", "쑝쑝돈까스", "도쿄라멘3900", "1F 핵밥", "스몰하우스", "1F 멘동", "왕돈까스왕냉면",
                    "2F 설쌈냉면", "1F 현선이네", "크라이치즈버거", "맥도날드", "프레드피자", "뚝배기스파게티"]]
    toggle_button_colors("그 외", other_foods, "#F6CEEC")

# 음식 종류 버튼 UI(첫 번째 줄)
for food in food_types_line1:
    if food == "한식":
        button = tk.Button(buttons_frame_line1, text=food, width=10, command=highlight_korean_food)
    elif food == "중식":
        button = tk.Button(buttons_frame_line1, text=food, width=10, command=highlight_chinese_food)
    elif food == "양식":
        button = tk.Button(buttons_frame_line1, text=food, width=10, command=highlight_western_food)
    else:
        button = tk.Button(buttons_frame_line1, text=food, width=10)
    button.pack(side=tk.LEFT, padx=(10, 10))

# 음식 종류 버튼 UI(두 번째 줄)
for food in food_types_line2:
    if food == "일식":
        button = tk.Button(buttons_frame_line2, text=food, width=10, command=highlight_japanese_food)
    elif food == "그 외":
        button = tk.Button(buttons_frame_line2, text=food, width=10, command=highlight_other_food)
    else:
        button = tk.Button(buttons_frame_line2, text=food, width=10)
    button.pack(side=tk.LEFT, padx=(10, 10))

price_label = tk.Label(left_frame, text="가격을 입력하세요 !!", font=("Arial", 12), bg="white")
price_label.pack(anchor='w', pady=10)

price_note = tk.Label(left_frame, text="- 대표메뉴가 입력하신 가격 이하인 식당을 보여줍니다.", font=("Arial", 10), bg="white")
price_note.pack(anchor='w', padx=20)

price_entry = tk.Entry(left_frame, width=20)
price_entry.pack(pady=10)

# 가격 필터링 기능
def apply_price_filter():
    try:
        max_price = int(price_entry.get())
    except ValueError:
        return

    for name, button in restaurant_buttons.items():
        if name in restaurant_prices and restaurant_prices[name] <= max_price: #입력한 메뉴의 가격과 대표 메뉴 가격 비교
            button.configure(bg="#3CB371")
        else:
            button.configure(bg="SystemButtonFace")

def reset_button_colors():
    for button in restaurant_buttons.values():
        button.configure(bg="SystemButtonFace")

price_buttons_frame = tk.Frame(left_frame, bg="white")
price_buttons_frame.pack(pady=10)

price_button = tk.Button(price_buttons_frame, text="가격 필터 적용", command=apply_price_filter)
price_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(price_buttons_frame, text="초기화", command=reset_button_colors)
reset_button.pack(side=tk.LEFT, padx=5)


# 식당 정보 화면
def open_restaurant_info(name):
    info_window = tk.Toplevel()
    info_window.title(f"{name} 정보")
    info_window.geometry("400x300")

    info_label = tk.Label(info_window, text=f"{name} 정보", font=("Arial", 16))
    info_label.pack(pady=10)

    # 네이버 지도 식당 검색 
    def search_on_naver_maps():
        query = name.replace("1F ", "").replace("2F ", "")
        url = f"https://map.naver.com/v5/search/{query}"
        webbrowser.open(url)

    search_button = tk.Button(info_window, text="식당 정보 확인하기", command=search_on_naver_maps)
    search_button.pack(pady=10)

    review_label = tk.Label(info_window, text="리뷰 작성", font=("Arial", 14))
    review_label.pack(pady=5)

    review_text = scrolledtext.ScrolledText(info_window, width=40, height=5)
    review_text.pack(pady=5)

    # 리뷰 제출 함수
    def submit_review():
        review = review_text.get("1.0", "end").strip()
        if review:
            filename = f"{name}_리뷰.txt"
            with open(filename, "a", encoding="utf-8") as file:  # 파일을 열고 리뷰 내용 추가
                file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n{review}\n\n")
            review_text.delete("1.0", "end")

    submit_button = tk.Button(info_window, text="제출", command=submit_review)
    submit_button.pack(pady=10)

    # 리뷰 확인 함수
    def view_reviews():
        filename = f"{name}_리뷰.txt"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:  # 파일을 열어 리뷰 목록 확인
                reviews = file.read()
            review_window = tk.Toplevel()
            review_window.title(f"{name} 리뷰")
            review_window.geometry("400x300")
            review_content = scrolledtext.ScrolledText(review_window, width=40, height=15)
            review_content.pack(pady=10)
            review_content.insert(tk.END, reviews)
            review_content.configure(state='disabled')
        else:
            messagebox.showinfo("리뷰 없음", "이 식당에 대한 리뷰가 없습니다.", parent=info_window) # 리뷰가 없을 시 뜨는 화면 설정        

    view_button = tk.Button(info_window, text="리뷰 확인하기", command=view_reviews)
    view_button.pack(pady=10)

# 레스토랑 목록(지도 시각화 과정에서 각 줄마다 공백 설정을 따로 하기 위해 식당들을 5개 목록으로 분리)
restaurant_names1 = [
    "프랭크버거", "리얼후라이", "이삭토스트", "1F 샐러디, 2F 취향", "1F 써브웨이, 2F 초밥이야기", "김가네", "긴자료코",
    "1F 슬로우캘리, 2F 순수치킨", "한솥", "청년다방", "1F 밀알식당, 2F 내가찜한닭", 
    "1F 현선이네, 2F 샹츠마라, 2F 설쌈냉면", "맥도날드", "면식당", "은화수식당", "손칼국수", "포케올데이", "쑝쑝돈까스","1F 퍼민, 2F 황궁쟁반짜장"
]
restaurant_names2 = ["도쿄라멘3900", "지지고"]
restaurant_names3 = ["1F 청운", "2F 연래춘"]
restaurant_names4 = ["고기스토리", "1F 부리또집, 2F 더코네", "먹돼지", "일품양평해장국", "백채김치찌개", 
                     "신의주찹쌀순대", "코웍비스트로", "파라다이스", "뚝배기스파게티"]
restaurant_names5 = ["889상도", "샤로스톤", "프레드피자", "고기마을찌개나라", "크라이치즈버거", "1F 핵밥, 2F 밀플랜비", 
                     "스몰하우스", "1F 멘동, 2F 찌개대학부대과", "명품고향삼계탕", "더진국수육국밥", "숯가마바베큐치킨", 
                     "왕돈까스왕냉면", "철탄함바그텐동", "스톤504", "고렝"]

# 레스토랑 가격 정보
restaurant_prices = {
    "프랭크버거": 4600, "리얼후라이": 19000, "이삭토스트": 3100, "1F 샐러디" : 7200, "2F 취향" : 6500, 
    "1F 써브웨이" : 9300, "2F 초밥이야기" : 16000, "김가네" : 4500,
    "긴자료코" : 10500, "1F 슬로우캘리" : 11500, "2F 순수치킨" : 19000, "한솥" : 6200,
    "청년다방" : 17500, "1F 밀알식당" : 5000, "2F 내가찜한닭" : 24000, "1F 현선이네" : 21000,
    "2F 샹츠마라" : 9000, "2F 설쌈냉면" : 9000, "맥도날드" : 6300, "면식당" : 7900, 
    "은화수식당" : 9000, "손칼국수" : 6500, "포케올데이" : 9900, "쑝쑝돈까스" : 8900, "1F 퍼민" : 9400, 
    "2F 황궁쟁반짜장" : 5000, "도쿄라멘3900" : 3900, "지지고" : 4500, "1F 청운" : 18000,
    "2F 연래춘" : 5000, "고기스토리" : 13000, "1F 부리또집" : 3500, "2F 더코네" : 8500, 
    "먹돼지" : 9500, "일품양평해장국" : 9000, "백채김치찌개" : 8500, "신의주찹쌀순대" : 9000,
    "코웍비스트로" : 11000, "파라다이스" : 7500, "뚝배기스파게티" : 7000, "889상도" : 18000, "샤로스톤" : 15000, 
    "프레드피자" : 15900, "고기마을찌개나라" : 15000, "크라이치즈버거" : 7900, "1F 핵밥" : 12900,
    "2F 밀플랜비" : 6000, "스몰하우스" : 8000, "1F 멘동" : 7500, "2F 찌개대학부대과" : 7000,
    "명품고향삼계탕" : 14000, "더진국수육국밥" : 8000, "숯가마바베큐치킨" : 17000,
    "왕돈까스왕냉면" : 9500, "철탄함바그텐동" : 10900, "스톤504" : 34900, "고렝" : 9500
}

# names1을 처리하는 반복문
for name in restaurant_names1:
    if ',' in name:
        names = name.split(',')
        if "1F 현선이네" in names[0]:
            frame = tk.Frame(right_frame1)
            frame.pack(side=tk.LEFT, padx=(70, 0), pady=10)
        else:
            frame = tk.Frame(right_frame1)
            frame.pack(side=tk.LEFT, padx=10, pady=10)
        for single_name in names:
            single_name = single_name.strip()
            button = tk.Button(frame, text=single_name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=single_name: open_restaurant_info(name))
            button.pack(padx=10, pady=6)
            restaurant_buttons[single_name] = button
    else:
        button = tk.Button(right_frame1, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                           command=lambda name=name: open_restaurant_info(name))
        button.pack(side=tk.LEFT, padx=10, pady=10)
        restaurant_buttons[name] = button

# names2를 처리하는 반복문
for name in restaurant_names2:
    button = tk.Button(right_frame2, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                       command=lambda name=name: open_restaurant_info(name))
    if name == '지지고':
        button.pack(side=tk.LEFT, padx=(110,0), pady=10)
    else:
        button.pack(side=tk.LEFT, padx=(1090, 10), pady=10)
    restaurant_buttons[name] = button

# names3를 처리하는 반복문
for name in restaurant_names3:
    button = tk.Button(right_frame3, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                       command=lambda name=name: open_restaurant_info(name))
    if name == "1F 청운":
        button.pack(side=tk.LEFT, padx=(1300,10), pady=10)
    if name == "2F 연래춘":
        button.pack(side=tk.LEFT, padx=10, pady=10)
    restaurant_buttons[name] = button

# names4를 처리하는 반복문
for name in restaurant_names4:
    if ',' in name:
        names = name.split(',')
        frame = tk.Frame(right_frame4)
        if "1F 부리또집" in names[0]:
            frame.pack(side=tk.LEFT, padx=10, pady=10)
        elif "먹돼지" in names[0]:
            frame.pack(side=tk.LEFT, padx=(400,10), pady=10)
        else:
            frame.pack(side=tk.LEFT, padx=10, pady=10)
        for single_name in names:
            single_name = single_name.strip()
            button = tk.Button(frame, text=single_name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=single_name: open_restaurant_info(name))
            button.pack(pady=6)
            restaurant_buttons[single_name] = button
    else:
        if name == "고기스토리":
            button = tk.Button(right_frame4, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=name: open_restaurant_info(name))
            button.pack(side=tk.LEFT, padx=(800,10), pady=10)
        elif name == "먹돼지":
            button = tk.Button(right_frame4, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=name: open_restaurant_info(name))
            button.pack(side=tk.LEFT, padx=(300,10), pady=10)
        else:
            button = tk.Button(right_frame4, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=name: open_restaurant_info(name))
            button.pack(side=tk.LEFT, padx=10, pady=10)
        restaurant_buttons[name] = button

# names5를 처리하는 반복문
for name in restaurant_names5:
    if ',' in name:
        names = name.split(',')
        frame = tk.Frame(right_frame5)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        for single_name in names:
            single_name = single_name.strip()
            button = tk.Button(frame, text=single_name, relief="solid", borderwidth=1, padx=10, pady=5, 
                               command=lambda name=single_name: open_restaurant_info(name))
            button.pack(padx=10, pady=6)
            restaurant_buttons[single_name] = button
    else:
        button = tk.Button(right_frame5, text=name, relief="solid", borderwidth=1, padx=10, pady=5, 
                           command=lambda name=name: open_restaurant_info(name))
        if name == '889상도':
            button.pack(side=tk.LEFT, padx=(510,10), pady=10)
        elif name == '스몰하우스':
            button.pack(side=tk.LEFT, padx=(100,10), pady=10)
        else:
            button.pack(side=tk.LEFT, padx=10, pady=10)
        restaurant_buttons[name] = button

root.mainloop()
