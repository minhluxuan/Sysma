import numpy as np
from sympy import symbols
from sympy.solvers import solve
from sklearn.metrics import r2_score
import datetime as dt

#Tìm phần tử lớn nhất trong list
def max(a):
    max = a[0]
    for x in a:
        if x >= max:
            max = x
    return max

#Tính tổng Reimann trái
def reaverage(ypoints,xpoints):
    reimann_sum = 0
    for i in range(len(xpoints)-1):
        reimann_sum += ypoints[i]*(xpoints[i+1]-xpoints[i])
    return reimann_sum/(len(xpoints)-1)

#Tính giá trị trung bình các phần tử trong list
def average(a):
    sum = 0
    for x in a:
        sum += x
    average = sum/len(a)
    return average

#Lấy đạo hàm bậc order của hàm 1 biến f
def get_deriv(f,order):
    if order==1:
        return f.deriv().c
    elif order==2:
        return f.deriv().deriv().c
    else:
        return "Higher order is not supported."

#Đề xuất bậc của model fit với tập data (x,y)
def rec_order(x,y):
    for i in range(11):
        model = np.poly1d(np.polyfit(x,y,i))
        if r2_score(y,model(x)) > 0.9 or r2_score(y,model(x))==0.9:
            order=i
            break
    return order

#Chuyển thời điểm ở đơn vị phút thành khung giờ
def min_to_timeslot(min):
    start = int(min/60) + 7
    end = start + 1
    timeslot = str(start) + " - " + str(end)
    return timeslot

#Chọn khung giờ phổ biến
def popular_timeslot(num_people,min,average):
    timeslot = []
    for x in num_people:
        if x>=average:
            timeslot.append(min_to_timeslot(min[num_people.index(x)]))
    return [*set(timeslot)]

#Tìm nghiệm phương trình đa thức
def find_solution(vecto_c):
    c = []
    for i in vecto_c:
        c.append(i)
    for i in range(11 - len(c)):
        c = [0] + c
    x=symbols('x')
    solutions = solve(c[0]*x**10 + c[1]*x**9 + c[2]*x**8 + c[3]*x**7 + c[4]*x**6 + c[5]*x**5 + c[6]*x**4 + c[7]*x**3 + c[8]*x**2 + c[9]*x**1 + c[10]*x**0,x)
    return solutions

#Khảo sát tính đơn điệu của hàm đa thức
def analyze_function(model):
    model_der_c = model.deriv().c
    solutions = find_solution(model_der_c)
    string = ""
    if (model.deriv()(solutions[0]-0.01)) > 0:
        string += "Tăng trong khoảng 7 - " + str(int(solutions[0]/60+7)) + '\n'
    elif (model.deriv()(solutions[0]-0.01)) < 0:
        string += "Giảm trong khoảng 7 - " + str(int(solutions[0]/60+7)) + '\n'
    for i in range(len(solutions)):
        if (model.deriv()(solutions[i]+0.01)) < 0:
            if(i+1<len(solutions)):
                string += "Giảm trong khoảng " + str(int(solutions[i]/60+7)) + " - " + str(int(solutions[i+1]/60+7)) + '\n'
            else:
                string += "Giảm trong khoảng " + str(int(solutions[i]/60+7)) + " - 22" + '\n'
        elif (model.deriv()(solutions[i]+0.01)) > 0:
            if(i+1<len(solutions)):
                string += "Tăng trong khoảng " + str(int(solutions[i]/60+7)) + " - " + str(int(solutions[i+1]/60+7)) + '\n'
            else:
                string += "Tăng trong khoảng " + str(int(solutions[i]/60+7)) + " - 22" + '\n'
    return string

#Tìm phần tử có mode lớn nhất trong list
def most_pop(ds):
    temp = set(ds)
    x = 0
    for i in temp:
        if ds.count(i)>x:
            x = ds.count(i)
            y=i
    return y

#Chuyển thời điểm dạng datetime hoặc time thành giờ (số thực)
def single_hour_convert(time):
    try:
        time = dt.datetime.strptime(time, '%d/%m/%Y %H:%M:%S')
    except:
        time = dt.datetime.strptime(time, '%H:%M:%S')
    hour = int(time.strftime('%H'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    return hour + min / 60 + sec/3600

#Chuyển danh sách thời điểm dạng datetime hoặc time thành danh sách giờ (số thực)
def hour_convert(time_list):
    converted_list = []
    for x in time_list:
        converted_list.append(single_hour_convert(x))
    return converted_list

#Chuyển thời điểm dạng datetime hoặc time thành phút (số thực)
def single_min_convert(time):
    try:
        time = dt.datetime.strptime(time, '%d/%m/%Y %H:%M:%S')
    except:
        time = dt.datetime.strptime(time, '%H:%M:%S')
    hour = int(time.strftime('%H'))
    min = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    return hour*60 + min + sec/60

#Chuyển danh sách thời điểm dạng datetime hoặc time thành danh sách phút (số thực)
def min_convert(time_list):
    converted_list = []
    for x in time_list:
        converted_list.append(single_hour_convert(x))
    return converted_list



