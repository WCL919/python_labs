all_name =input()
name_parts =all_name.split()
new_name =''.join(name_parts)
initials =''.join([part[0].upper()for part in name_parts])+'.'
lenghth =len(new_name)
print(f"Инициалы:{initials}")
print(f"Длина (символов):{lenghth}")