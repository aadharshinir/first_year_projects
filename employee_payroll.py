def calculate_weekly_salary(hours,hourly_wage):
    if hours>1 and hours<40:
        wage = hours*hourly_wage
    elif hours>=40:
        wage = hours*1.5*hourly_wage
    return wage
   
def calculate_bonus(performance_score, annual_salary):
    if performance_score>=90:
        bonus = annual_salary*10/100
    elif performance_score>=80:
        bonus = annual_salary*5/100
    elif performance_score<80:
        bonus = 0
    return bonus
   
def calculate_tax(wage, bonus):
    net_salary = wage+bonus
    print("Net_salary = Rs.", net_salary)
    tax_amount=0
    if net_salary>0 and net_salary<=3000:
        tax_amount=0
    elif net_salary>3000 and net_salary<=8000:
        tax_amount=net_salary*10/100
    elif net_salary>8000 and net_salary<=15000:
        tax_amount=net_salary*20/100
    elif net_salary>15000:
        tax_amount=net_salary*30/100
    netsalary_2 = net_salary - tax_amount
    return netsalary_2
   
name= input("Enter the employee name: ")
hourly_wage= int(input("Enter the hourly wage: "))
hours = int(input("Enter the number of working hours: "))
performance_score = int(input("Enter the performance score: "))
annual_salary = int(input("Enter the annual salary: "))


print("Employee Payroll Report")
print("Employee name: ",name)
wage = calculate_weekly_salary(hours,hourly_wage)
print("Weekly salary = Rs.",wage)
bonus = calculate_bonus(performance_score, annual_salary)
print("Bonus = Rs.", bonus)
netsalary_2 = calculate_tax(wage, bonus)
print("Net salary(after tax) = Rs.",netsalary_2)
total_compensation = wage+netsalary_2
print("Total compensation = Rs.", total_compensation)