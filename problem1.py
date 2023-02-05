def show_emplpyee(e_name, salary):
    # emplyee_state
    if salary == 0:
        emplyee_state= f'my name is {e_name} and my salary is 9000'
    elif salary == 0 and e_name=='':
        emplyee_state= 'my name is anonymous and my salary is 90000'
    elif e_name == '':
        emplyee_state= f'my name is anonymous and my salary is{salary}'
    else:
        emplyee_state= f'my name is {e_name} and my salary is{salary}'
    
    return emplyee_state

# input(print(f'enter your name and salary: '))
print(show_emplpyee('anisur', 8000))


# def show_employee(name="anonymous", salary=9000):
#     print(f"Employee Name: {name}")
#     print(f"Employee Salary: {salary}")
