#tamrin 2 module tafkik poroje!
import file_ops
while True:
    print("="*30)
    print("="*15 ,"menu", "="*15)
    print("gozine 1 == neveshtan file \ngozine 2 == ezafe kardan be file \ngozine 3 == namayesh file \ngozine 4 == copy va backup file \ngozine 5 == edgham file \ngozine 6 == shoamresh horof dar file \ngozine 7 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro enetkhab kardid!")
        file_name = input("lotfan esm file ie ke mikhahid dar on chizi benevisisd ro vared konid ba passvand (.txt):")
        if file_name == "":
            print("shoma esm file ro vared nakarddi!")
            continue
        if not file_name.endswith(".txt"):
            print(f"passavand file : {file_name} ro fara,osh kardid!")
            continue
        matn = input(f"lotfan on chii ke mikhahid dar file: {file_name} benevisid ro vared konid: ")
        if matn == "":
            print("shoam matni ro vared nakardid!")
            continue
        file_ops.write_file(file_name,matn)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        file = input("lotfan esm file ke mikhahid be on ezafe konid ro varded konid ba passavnd (.txt): ")
        if file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file.endswith(".txt"):
            print(f"passavnd file : {file} ro faramosh kardid!")
            continue
        add_matn = input(f"lotfan matni ke mikhahid be file : {file} ezafe konid ro vared konid: ")
        if add_matn == "":
            print(f"shoma matni ro vared nakardid baraye ezafe kardan be file: {file}")
            continue
        file_ops.add_file(file,add_matn)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        show_file = input("lotfan esm file ke mikhahid namayesh dade shavad ro vared konid ba passvand (.txt):  ")
        if show_file == "":
            print("shoam esm file ro vared nakardid ke namayesh dade shavad!")
            continue
        if not show_file.endswith(".txt"):
            print(f"passavnd file: {show_file} ro faramosh kardid!")
            continue
        file_ops.show_file(show_file)
    elif choice == "4":
        print("shoma gozine 4 ro enetkhab kardid!")
        file1 = input("lotfan esm file ke mikahhid az on backup begirid ro vared konid ba passvand (.txt):")
        if file1 == "":
            print("shoma esm file ri vared nakardid!")
            continue
        if not file1.endswith(".txt"):
            print(f"passvand file {file1} ro faramosh kardid!")
            continue
        file2 = input(f"lotfan esm file 2 ke mikhahid mohtaviyat file {file1} dar on rikhte shavad ro vared konid ba passavnd (.txt): ")
        if file2 == "":
            print("shoma esm file dovom ro vared nakardid!")
            continue
        if not file2.endswith("txt"):
            print(f"passvanf file dovom : {file2} ro faramosh kardid!")
            continue
        new_matn = input(f"lotfan matni ke mikhahid dar file 1 : {file1} ro vared konid:  ")
        if new_matn == "":
            print("shoma chizi vared nakardid!")
            continue
        file_ops.copy_backup(file1,file2,new_matn)
    elif choice == "5":
        print("shoma gozine 5 ro enetkhab karddi!")
        file_name1 = input("lotfan esm file aval ro vared konid ba passavnd (.txt) :")
        if file_name1 == "":
            print("shoma esm file aval ro vared nakardid!")
            continue
        if not file_name1.endswith(".txt"):
            print(f"passvand file aval :{file_name1} ro faramosh kardid!")
            continue
        file_name2 = input("lotfan esm file dovom ro vared konid ba passavnd (.txt): ")
        if file_name2 == "":
            print("shoam esm file dovom ro vared nakardid!")
            continue
        if not file_name2.endswith(".txt"):
            print(f"passavnd file dovom : {file_name2} ro faramosh kardid!")
            continue
        final_file = input("lotfan esm file ke mikhahid edgham shode file aval va file dovom dar on rikhte shavad ro vared konid ba passvand (.txt): ")
        if final_file == "":
            print("shoma esm file nahayi ro vared nakardid! ")
            continue
        if not final_file.endswith(".txt"):
            print(f"passvand file nahayi :{final_file} ro faramosh kardid!") 
            continue
        file_ops.edgham_file(file_name1,file_name2,final_file)
    elif choice == "6":
        print("shoma gozine 6 ro entkhab kardid!")
        count_word_file  = input("lotfan esm file ke mikhahid horof on shomorde shavad or vared konid ba passvand (.txt):  ")
        if count_word_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not count_word_file.endswith(".txt"):
            print(f"passavnd file: {count_word_file} ro faramosh kardid!")
            continue
        file_ops.count_word(count_word_file)
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid va az barname kharej shodid!!!")
        break
    else:
        print("lotfan az gozine 1 ta 7 entekhab konid!")
        continue