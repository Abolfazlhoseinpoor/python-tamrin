# tamrin 2 module tafkik poroje!
def write_file (file_name,matn):
    try:
        with open(file_name , "w") as f:
            f.write(matn + "\n")
        print(f"matn shoma dar file {file_name} zakhire shod!")
    except PermissionError:
        print(f"shoma dastarsi be neveshtan dar file : {file_name} ro nadarid!")
        return
def add_file (file_name,matn):
    try:    
        with open(file_name , "a") as f:
            f.write(matn + "\n")
        print(f"matn mored nazar dar file : {file_name} ezafe shod!") 
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
        return
    except PermissionError:
        print(f"shoma dastarsi be neveshtan file : {file_name} ro nadarid!")
        return
def show_file (file_name):
    try:
        with open(file_name , "r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file {file_name} khali ast!")
            return
        print("="*30)
        for i,line in enumerate(khat,start= 1):
            print(f"{i} === {line}")
        print("="*30)
    except FileNotFoundError:
        print(f"file : {file_name} peyda nashod!")
        return
def copy_backup (file_name1,file_name2,matn):
    try:
        with open(file_name1 , "r") as f:
            khat = f.readlines()
        if not khat:
            print(F"file : {file_name1} khali ast!")
            return
        with open(file_name2 , "w") as g:
            g.writelines(khat)
        print(f"matn shoma az file {file_name1} be file : {file_name2} copy shod!")
        with open(file_name1,"w") as t:
            t.write(matn + "\n")
        print(f"matn shoma dar file {file_name1} zakhire shod!")
    except FileNotFoundError:
        print(f"file : {file_name1} peyda nashod!")
        return
    except PermissionError as e:
        print(f"shoma dastarasi be neveshtan matn khod dar file {e} ro nadarid!")
        return
def edgham_file (file_name1 , file_name2,final_file):
    try:
        with open(file_name1 , "r") as f:
            khat1 = f.readlines()
        if not khat1:
            print(f"file {file_name1} khali ast!")
            return
        with open(file_name2 , "r") as g:
            khat2 = g.readlines()
        if not khat2:
            print(f"file : {file_name2} khali ast!")
            return
    except FileNotFoundError as e:
        print(f"file : {e} peyda nashod!")
        return
    kol_khat1 = [line.strip() for line in khat1 if line.strip() != ""]
    kol_khat2 = [line.strip() for line in khat2 if line.strip() != ""]
    edgham = kol_khat1 + kol_khat2
    khatha = []
    for line in edgham:
        if line not in khatha:
            khatha.append(line)
    try:
        with open(final_file , "w") as t:
            t.write("\n".join(khatha) + "\n")
    except PermissionError:
        print(f"shoma dastrasi be neveshtan matni dar file : {final_file} ro nadarid!")
        return
def count_word (file_name):
    try:
        with open(file_name, "r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file : {file_name} khali ast!")
            return
    except FileNotFoundError:
        print(f"file : {file_name} peyda nashod!")
        return
    count_line = len(khat)
    count_word = 0
    for i in khat:
        words = i.split()
        count_word += len(words)
    print(f"tedad khat haye file : {file_name} === {count_line}")
    print(f"tedad kalame haye file : {file_name} === {count_word}")
