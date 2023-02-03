import numpy as np
from sympy import symbols
from sympy.solvers import solve
from sklearn.metrics import r2_score
import datetime as dt
from sympy import symbols
from sympy.solvers import solve
import numpy
import pandas

from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import datetime as dt
import pandas
import matplotlib.pyplot as plt

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
    return reimann_sum/(xpoints[len(xpoints)-1]-xpoints[0])

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
def exam_function(model):
    model_der_c = model.deriv().c
    solutions = find_solution(model_der_c)
    string = ""
    if (model.deriv()(solutions[0]-0.01)) > 0:
        string += "Tăng trong khoảng âm vô cùng - " + str(int(solutions[0]/60+7)) + '\n'
    elif (model.deriv()(solutions[0]-0.01)) < 0:
        string += "Giảm trong khoảng âm vô cùng - " + str(int(solutions[0]/60+7)) + '\n'
    for i in range(len(solutions)):
        if (model.deriv()(solutions[i]+0.01)) < 0:
            if(i+1<len(solutions)):
                string += "Giảm trong khoảng " + str(int(solutions[i]/60+7)) + " - " + str(int(solutions[i+1]/60+7)) + '\n'
            else:
                string += "Giảm trong khoảng " + str(int(solutions[i]/60+7)) + " - cộng vô cùng" + '\n'
        elif (model.deriv()(solutions[i]+0.01)) > 0:
            if(i+1<len(solutions)):
                string += "Tăng trong khoảng " + str(int(solutions[i]/60+7)) + " - " + str(int(solutions[i+1]/60+7)) + '\n'
            else:
                string += "Tăng trong khoảng " + str(int(solutions[i]/60+7)) + " - cộng vô cùng" + '\n'
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
    return hour + min / 60

#Chuyển danh sách thời điểm dạng datetime hoặc time thành danh sách giờ (số thực)
def hour_convert(time_list):
    converted_list = []
    for x in time_list:
        converted_list.append(single_hour_convert(x))
    return converted_list

#Chuyển thời điểm dạng datetime hoặc time thành phút (số thực)
def single_min_convert(time):
    try:
        time = dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
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
        converted_list.append(single_min_convert(x))
    return converted_list

# hàm bestsell_time trả về các khung giờ bán chạy nhất trong 1 ngày
def bestsell_time(sale_list, time_list): # 7-8, 8-9   
    max_product = sale_list[0]
    list_bestseller = []
    for i in range(len(sale_list)):
        if sale_list[i] > max_product:
            max_product = sale_list[i]
    for i in range (len(sale_list)):
        if sale_list[i] == max_product:
            list_bestseller.append(time_list[i])
    return list_bestseller

#Tính tổng số lượng sản phẩm bán được trong từng khung giờ,
# trả về khung giờ bán được nhiều sản phẩm nhất (bán chạy nhất)
def prod_hour(list_prod,list_time):
    temp = list_time[0]
    list_sell = []
    sum = 0
    for i in range(len(list_prod)):
        temp0 = list_time[i]
        if (temp == temp0):
            sum += list_prod[i] 
        if (temp != temp0):
            list_sell.append(sum)
            sum = list_prod[i]
            temp = temp0
    list_sell.append(sum)
    return list_sell

# hàm trả về tổng số lượng 1 sản phẩm bán được trong 1 ngày
def sale_day(sale_list):
    total = 0
    for i in range (len(sale_list)):
        total += sale_list[i]
    return total


# hàm tính giá trị  trung bình của 1 sản phẩm bán được trong 1 giờ trên ngày 
def average_day(sale_day):
    return float(sale_day)/float(15)

# hàm doanh thu của sản phẩm ứng với sản phẩm được bán ra trong 1 ngày 
def revenue(sale_day, price):
    return sale_day*price

# hàm tính lợi nhuận sản phẩm được bán ra trong 1 ngày
def profit(sale_day, price, cost):
    return sale_day*(price-cost)

# hàm tính tổng sản phẩm bán được trong 1 tuần
def sale_week(sale_days_list):
    total = 0
    for i in range(len(sale_days_list)):
        total += sale_days_list[i]
    return total

# hàm trả về danh sách các ngày bán chạy trong tuần
def bestsell_week(sale_days_list): #sale_days_list là list số lượng sản phẩm bán được trong các ngày từ thứ hai đến chủ nhật, sắp xếp theo chiều tăng của chỉ số
    res = []
    days = ['Thứ hai','Thứ ba','Thứ tư','Thứ năm','Thứ sáu','Thứ bảy','Chủ nhật']
    average = average(sale_days_list)
    for i in range(len(sale_days_list)):
        if sale_days_list[i]>=average:
            res.append(days[i])
    return res

#Đề xuất bậc tốt nhất cho hàm đa biến
def rec_deg(X,y):
    mean_squared_error_list = []
    number_degrees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for degree in number_degrees:
        #Khai báo sử dụng mô hình hồi quy đa biến bậc degree
        poly_reg = PolynomialFeatures(degree=degree)
        X_poly = poly_reg.fit_transform(X)
        #Mô hình hồi quy đa biến
        model=poly_reg.fit_transform(np.array(X))
        poly_reg.fit(X_poly,y)
        lin_reg = LinearRegression()
        lin_reg.fit(X_poly, y)
        y_pred = lin_reg.predict(model)
        mean_squared_error_list.append(mean_squared_error(y,y_pred,squared=False))
    degree = number_degrees[mean_squared_error_list.index(min(mean_squared_error_list))]-1
    return degree

#Dự đoán lợi nhuận
def predict_sale(data,price,time):
    dataset = pandas.read_csv(data)
    X = dataset.iloc[:,0:2].values
    y = dataset.iloc[:,2].values
    mean_squared_error_list = []
    number_degrees = [1,2,3,4,5,6,7,8,9,10]
    degree = rec_deg(X,y)
    poly_reg = PolynomialFeatures(degree=degree)
    X_poly = poly_reg.fit_transform(X)
    model = poly_reg.fit_transform(np.array([[price,time]]))
    poly_reg.fit(X_poly, y)
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    predicted_sale = lin_reg.predict(model)
    return predicted_sale[0]

#Đề xuất mức giá để thu được doanh thu lớn nhất
def rec_saleoff(data,cost,limit,time):
    dataset = pandas.read_csv(data)
    X = dataset.iloc[:,0:2].values
    y = dataset.iloc[:,2].values
    sales = []
    prices = []
    inc = 0
    while inc <= limit:
        price = cost + inc
        sales.append(predict_sale(data,price,time))
        prices.append(price)
        inc+=0.1
    return prices[sales.index(max(sales))]


