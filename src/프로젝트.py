import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# 글로벌 변수 선언
budget_ratios = {}  # 각 카테고리별 예산 비율을 저장하는 딕셔너리
budget_amounts = {}  # 총 수입과 비율을 기반으로 계산된 각 카테고리별 예산 금액을 저장하는 딕셔너리
actual_spending = {}  # 각 카테고리별 실제 지출을 추적하는 딕셔너리
daily_spending = {}  # 날짜와 카테고리별 지출을 추적하는 딕셔너리
total_income = 0  # 이번 달의 총 수입
current_year = datetime.today().year  # 현재 연도
current_month = datetime.today().month  # 현재 월

def set_income_and_ratios(): #수입과 예산 카테고리 비율 정하는 함수
    global total_income, budget_ratios
    try:
        total_income = float(entry_income.get().strip())  #tkinter로 입력된 수입을 변수로 저장
        budget_ratios.clear()
        for entry in budget_entries:
            category = entry['category'].get().strip()  # 카테고리 입력값을 가져와서 공백 제거
            ratio = entry['ratio'].get().strip()  # 비율 입력값을 가져와서 공백 제거
            if not category or not ratio:
                raise ValueError("항목과 비율을 모두 입력하세요.")  # 입력값이 없으면 오류 발생
            ratio = float(ratio)  # 비율을 float 를 통해 실수로 변환
            budget_ratios[category] = ratio

        if sum(budget_ratios.values()) != 100:
            raise ValueError("비율의 합이 100%가 아닙니다.")
        
        calculate_budget_amounts()
        messagebox.showinfo("성공", "수입 및 예산 비율이 설정되었습니다.")
        budget_window.destroy()
    except ValueError as e:  # try 문으로 위 코드에서 예외 발생 시 messagebox 출력
        messagebox.showerror("입력 오류", f"유효한 값을 입력하세요: {e}")

def calculate_budget_amounts(): # 총 수입을 카테고리별로 분류해서 변수에 저장하는 함수
    global budget_amounts, actual_spending, daily_spending
    budget_amounts = {category: (total_income * ratio) / 100 for category, ratio in budget_ratios.items()} 
    actual_spending = {category: 0 for category in budget_ratios}  
    daily_spending = {} 

def record_spending(): # 지출 기록 함수
    global actual_spending, daily_spending
    try:
        spending = entry_spending.get().strip()  # 지출 입력값을 가져와서 공백 제거
        category, amount = spending.split() 
        amount = float(amount) 
        date = selected_date.get()  # 달력에서 선택된 날짜 가져오기

        if category not in budget_amounts:
            messagebox.showerror("입력 오류", "유효하지 않은 항목입니다.")  # 저장된 카테고리에 입력값이 없으면 오류 발생하는 messagebox 출력
            return

        actual_spending[category] += amount 
        if date not in daily_spending:
            daily_spending[date] = {}
        if category not in daily_spending[date]:
            daily_spending[date][category] = 0
        daily_spending[date][category] += amount 

        show_remaining_budget()
        messagebox.showinfo("성공", "지출이 기록되었습니다.")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 금액을 입력하세요.")  # try 문으로 위 코드에서 예외 발생 시 messagebox 출력

def show_remaining_budget(): # 지출을 계산해서 카테고리별로 남은 예산 계산하는 함수
    spending_text.delete(1.0, tk.END)
    spending_text.insert(tk.END, "남은 예산:\n")
    for category in budget_amounts:
        remaining = budget_amounts[category] - actual_spending[category]  # 남은 예산 계산
        spending_text.insert(tk.END, f"{category}: {remaining:.2f}원\n")  # 남은 예산 출력

def analyze_spending():  # 예상 소비 계획과 실소비량을 비교하여 분석
    spending_text.delete(1.0, tk.END)
    spending_text.insert(tk.END, "월말 분석:\n")
    for category in budget_amounts:
        budgeted = budget_amounts[category]
        spent = actual_spending[category]
        difference = spent - budgeted  # 예산과 실제 지출 차이 계산
        if difference > 0: #만약 소비가 수입보다 많다면 예산초과, 아니면 남은 돈 출력
            spending_text.insert(tk.END, f"{category}: 예산 초과 {difference:.2f}원\n")
        else:
            spending_text.insert(tk.END, f"{category}: 예산 내 {abs(difference):.2f}원 남음\n")

    spending_text.insert(tk.END, "\n개선 방향 제시:\n") #만약 소비가 수입보다 많다면 예산초과, 아니면 남은 돈 출력
    any_exceed = False
    for category in budget_amounts:
        if actual_spending[category] > budget_amounts[category]:
            spending_text.insert(tk.END, f"{category} 항목에서의 지출이 많습니다. 예산 비율을 조정하거나 절약할 방법을 찾아보세요.\n")
            any_exceed = True
    if not any_exceed:
        spending_text.insert(tk.END, "알맞은 비율로 돈을 사용하고 있습니다\n")

def create_calendar(parent): #tkinter를 통해 달력 만들기
    global current_year, current_month

    today = datetime.today()
    calendar_frame = tk.Frame(parent)
    calendar_frame.pack()

    global selected_date
    selected_date = tk.StringVar()
    selected_date.set(today.strftime("%Y-%m-%d"))

    month_year_frame = tk.Frame(calendar_frame)
    month_year_frame.grid(row=0, column=0, columnspan=7)

    def show_spending_for_day(): #tkinter로 클릭한 날짜의 지출을 보여주는 함수
        date = selected_date.get()
        spending_info = daily_spending.get(date, "지출 내역이 없습니다.")
        spending_text.delete(1.0, tk.END)
        spending_text.insert(tk.END, f"{date} 지출 내역:\n")
        if spending_info != "지출 내역이 없습니다.":
            for category, amount in spending_info.items():
                spending_text.insert(tk.END, f"{category}: {amount:.2f}원\n")
        else:
            spending_text.insert(tk.END, spending_info)

    def generate_calendar(year, month): #달력 생성 함수, datetime 라이브러리를 통해서 실제 년도의 월일 계산
        for widget in calendar_frame.winfo_children():
            if isinstance(widget, tk.Button) or (isinstance(widget, tk.Label) and widget.cget("text") not in ["날짜를 선택하세요:", "이전", "다음", f"{current_year}년 {current_month}월"]):
                widget.destroy()

        header = ["일", "월", "화", "수", "목", "금", "토"]
        for col, day in enumerate(header):
            tk.Label(calendar_frame, text=day).grid(row=2, column=col)

        first_day = datetime(year, month, 1)
        start_day = (first_day.weekday() + 1) % 7
        day_row = 3
        day_col = start_day

        for day in range(1, 32):
            try:
                current_day = datetime(year, month, day)
                day_button = tk.Button(calendar_frame, text=str(day), command=lambda d=current_day: [selected_date.set(d.strftime("%Y-%m-%d")), show_spending_for_day()])
                day_button.grid(row=day_row, column=day_col)
                day_col += 1
                if day_col > 6:  # 토요일 다음은 새로운 줄로 바꿈
                    day_col = 0
                    day_row += 1
            except ValueError:
                break

    def prev_month(): # 전 달 이동
        global current_year, current_month
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
        generate_calendar(current_year, current_month)
        update_month_label()

    def next_month(): #다음 달 이동
        global current_year, current_month
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1
        generate_calendar(current_year, current_month)
        update_month_label()

    def update_month_label():
        month_label.config(text=f"{current_year}년 {current_month}월")

    prev_button = tk.Button(month_year_frame, text="이전", command=prev_month)
    prev_button.grid(row=0, column=0)

    month_label = tk.Label(month_year_frame, text=f"{current_year}년 {current_month}월")
    month_label.grid(row=0, column=1)

    next_button = tk.Button(month_year_frame, text="다음", command=next_month)
    next_button.grid(row=0, column=2)

    generate_calendar(current_year, current_month)

def add_budget_entry(): #예산 입력 ui
    entry_frame = tk.Frame(budget_window)
    entry_frame.pack()

    category_label = tk.Label(entry_frame, text="항목")
    category_label.pack(side=tk.LEFT)

    ratio_label = tk.Label(entry_frame, text="예산(%)")
    ratio_label.pack(side=tk.RIGHT)

    category_entry = tk.Entry(entry_frame)
    category_entry.pack(side=tk.LEFT)

    ratio_entry = tk.Entry(entry_frame)
    ratio_entry.pack(side=tk.LEFT)

    budget_entries.append({'category': category_entry, 'ratio': ratio_entry})

def open_budget_window(): #예산 설정 ui, 예산 설정 화면
    global budget_window, entry_income, budget_entries
    budget_entries = []

    budget_window = tk.Toplevel(root)
    budget_window.title("예산 설정")

    label_ratios = tk.Label(budget_window, text="예산 비율 설정:")
    label_ratios.pack()

    add_entry_button = tk.Button(budget_window, text="항목 추가", command=add_budget_entry)
    add_entry_button.pack()

    label_income = tk.Label(budget_window, text="이번 달 수입을 입력하세요:")
    label_income.pack()
    entry_income = tk.Entry(budget_window)
    entry_income.pack()
    button_set_income = tk.Button(budget_window, text="설정", command=set_income_and_ratios)
    button_set_income.pack()

    # 기본 항목 및 라벨 추가
    add_budget_entry()

def switch_to_spending_screen(): #지출 화면 ui, 달력이 포함된 메인화면
    initial_frame.pack_forget()
    spending_frame.pack()

    create_calendar(spending_frame)

    label_spending = tk.Label(spending_frame, text="지출 항목과 금액을 입력하세요 (예: 식비 5000):")
    label_spending.pack()
    global entry_spending
    entry_spending = tk.Entry(spending_frame)
    entry_spending.pack()
    button_record_spending = tk.Button(spending_frame, text="기록", command=record_spending)
    button_record_spending.pack()

    # 지출 분석 버튼
    button_analyze = tk.Button(spending_frame, text="분석", command=analyze_spending)
    button_analyze.pack()

    # 예산 설정 창 열기 버튼
    button_open_budget = tk.Button(spending_frame, text="예산 조정", command=open_budget_window)
    button_open_budget.pack()

    global spending_text
    spending_text = tk.Text(spending_frame, height=10, width=50)
    spending_text.pack()

def setup_ui(root): #ui 설정, 시작화면
    global initial_frame, spending_frame

    initial_frame = tk.Frame(root)
    initial_frame.pack()

    title_label = tk.Label(initial_frame, text="스마트 가계부", font=("Helvetica", 24))
    title_label.pack(pady=20)

    button_open_budget = tk.Button(initial_frame, text="예산 설정", command=open_budget_window)
    button_open_budget.pack(pady=10)

    button_proceed = tk.Button(initial_frame, text="지출 화면으로 이동", command=switch_to_spending_screen)
    button_proceed.pack(pady=10)

    spending_frame = tk.Frame(root)

def main(): #main 함수
    global root
    root = tk.Tk()
    root.title("Budget Manager")
    setup_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
