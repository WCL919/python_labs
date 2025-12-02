def foemat_record(rec: tuple[str, str, float]) ->str:
    fio, group, gpa =rec
    fio_parts =[part.strip()for part in fio.strip().split() if part. strip()]
    if not fio_parts:
        raise ValueError("ФИО не может быть пустым")
    last_name =fio_parts[0]
    initials =[]
    for name_part in fio_parts[1:3]:
        initials.append(name_part[0].upper()+".")
    initials_str =".".join(initials) +"." if initials else""
    formatted_gpa ="{0:.2f}".format(gpa)
    return f"{last_name}{initials_str},гр. {group}, GPA{formatted_gpa}"