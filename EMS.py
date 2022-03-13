import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("employee_dbms.db")

List_of_Tables = connection.execute("Select name from sqlite_master Where type='table' And name='Employee_management'").fetchall()

if List_of_Tables != []:

    print("Table not found!  ")

else:

    connection.execute('''Create Table Employee_management(
                          Employee_ID Integer Primary Key Autoincrement,
                          Employee_Code,
                          Employee_Name,
                          Employee_Phone,
                          Employee_Email,
                          Employee_Designation,
                          Employee_Salary,
                          Employee_Company_Name
    );     ''')

    print("Table Created Successfully")

while True:
    print("Select an OPTION from the MENU: ? ")

    print("1. ADD an Employee ")
    print("2. VIEW all the Employee ")
    print("3. SEARCH an Employee using an Employee Name ")
    print("4. UPDATE an Employee using an Employee Code ")
    print("5. DELETE an Employee using an Employee Code ")
    print("6. DISPLAY all the Employees with their GREATER than 50000 ")
    print("7. COUNT of all Employees ")
    print("8. DISPLAY all the Employee Details of RANGE and ALPHABETICAL ORDER ")
    print("9. DISPLAY all the Employee Details with SALARY with Less than AVG SALARY ")
    print("10. Exit ")

    choice = int(input("Enter any Choice to Selected ? "))

    if choice == 1:

        get_emp_code = input("Enter an Employee Code: ? ")
        get_emp_name = input("Enter an Employee Name: ? ")
        get_emp_phone = input("Enter an Employee Phone Number: ? ")
        get_emp_mail_ID = input("Enter an Employee Email ID: ? ")
        get_emp_desig = input("Enter an Employee Designation: ? ")
        get_emp_salary = input("Enter an Employee Salary: ? ")
        get_emp_company_name = input("Enter an Employee Company Name: ? ")

        connection.execute("Insert into Employee_management(Employee_Code, Employee_Name, \
        Employee_Phone, Employee_Email, Employee_Designation, Employee_Salary, Employee_Company_Name) \
        Values ("+get_emp_code+", '"+get_emp_name+"', "+get_emp_phone+", '"+get_emp_mail_ID+"', '"+get_emp_desig+"',\
         "+get_emp_salary+", '"+get_emp_company_name+"')")

        connection.commit()

        print("Data Inserted Successfully !!! ")

    elif choice == 2:

        result = connection.execute("Select * from Employee_management")

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Phone", "Employee Mail", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 3:

        get_name = input("Enter an Employee Name to be SEARCHED: ? ")

        result = connection.execute("Select * from Employee_management Where Employee_Name= '"+get_name+"'")

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Phone", "Employee Mail", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 4:

        get_employee_code = input("Enter an Employee Code to be UPDATED: ? ")

        get_emp_name = input("Enter an Employee Name: ? ")
        get_emp_phone = input("Enter an Employee Phone Number: ? ")
        get_emp_mail_ID = input("Enter an Employee Email ID: ? ")
        get_emp_desig = input("Enter an Employee Designation: ? ")
        get_emp_salary = input("Enter an Employee Salary: ? ")
        get_emp_company_name = input("Enter an Employee Company Name: ? ")

        connection.execute("Update Employee_management Set Employee_Name= '"+get_emp_name+"', Employee_Phone= "+get_emp_phone+",\
                            Employee_Email= '"+get_emp_mail_ID+"', Employee_Designation= '"+get_emp_desig+"',\
                            Employee_Salary= "+get_emp_salary+", Employee_Company_Name= '"+get_emp_company_name+"' Where \
                            Employee_Code= "+get_employee_code)

        connection.commit()

        print("Data Updated Successfully  !!!  ")

    elif choice == 5:

        get_employee_code = input("Enter an Employee Code to be DELETED: ? ")

        connection.execute("Delete from Employee_management Where Employee_Code=" +get_employee_code)

        connection.commit()

        print("Data Deleted Successfully  !!! ")

    elif choice == 6:

        result = connection.execute("Select * from Employee_management Where Employee_Salary > 50000")

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Phone", "Employee Mail", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 7:

        result = connection.execute("Select Count(*) as employees from Employee_management")

        for i in result:

            print("Count of all Employees: ", i[0])

    elif choice == 8:

        lowest_Salary = input("Enter a lowest value to print ? ")
        Highest_Salary = input("Enter a highest value to print ? ")

        result = connection.execute("Select * from Employee_management Where Employee_Salary Between "+lowest_Salary+" And  "+Highest_Salary+" Order by Employee_Salary")  # no use of asc

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Phone", "Employee Mail", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 9:

        result = connection.execute("Select * from Employee_management Where Employee_Salary < (Select Avg(Employee_Salary) from Employee_management) Order by Employee_Salary")  # no use of asc

        table = PrettyTable(["Employee ID", "Employee Code", "Employee Name", "Employee Phone", "Employee Mail", "Employee Designation", "Employee Salary", "Employee Company Name"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])

        print(table)

    elif choice == 10:

        connection.close()

        break

    else:

        print("INVALID Choice ! Please Re-Enter the CHOICE === !!!")