import os
import json
#原始表：所有的学号姓名等基本信息
#完成表、操作表：
#打开操作表-操作输出名单-重置
print(os.getcwd())

# porgnamelist = open ('python\\listmagnger\\namelist\\orglist.txt','r')
# porgname_list=porgnamelist.readlines()
# porgnamelist.close()

# opnlist = open ('python\\listmagnger\\namelist\\oprlist.txt','r')
# pname_list=opnlist.readlines()
# opnlist.close()

# dic = {  
#     'andy':{  
#         'age': 23,  
#         'city': 'beijing',  
#         'skill': 'python'  
#     },  
#     'william': {  
#         'age': 25,  
#         'city': 'shanghai',  
#         'skill': 'js'  
#     }  
# }  

# nm=input("nm")
# print(dic.get(nm))
# print(dic.get(nm).clear())


file_oname=open("python\listmagnger\\namelist\dit_onamelist.txt","r")
js_oname=file_oname.read()
#print(js_oname)
#print(type(js_oname))
dict_oname=json.loads(js_oname)
# print(type(dict_oname))
# print(dict_oname)

# print(dict_oname["andy"]["age"])

file_pname=open("python\listmagnger\\namelist\dit_pnamelist.txt","r")
js_pname=file_pname.read()
dict_pname=json.loads(js_pname)

#delete \n
# name_list=[]
# orgname_list=[]
# print(type(name_list))
# for temp_list in pname_list:
#     temp_list=temp_list.strip("\n")
#     name_list.append(temp_list)
# for temp_list in porgname_list:
#     orgname_list.append(temp_list.strip("\n"))


while True:
    tempinput=input("input:")
    print(type(dict_oname),type(dict_pname))
    if tempinput=="help":
        print("o-add-name o-add-id o-add-tips")
        print("o-output-all ")
        print("o-delet-all o-delet-name")
        print("o-modify")
        print("p-add-name")
        print("p-output-all p-output-name")
        print("p-delet-all p-delet-name")
        print("output-all")
        print("exit")
    elif tempinput=="exit":
        break
    elif tempinput=="o-add-name":
        while True:
            name_input=input("input name:")
            if name_input =="back":
                break
            elif name_input in dict_oname:
                print("{} is in the dict_oname")
            else:
                dict_oname.setdefault(name_input,{})
    elif tempinput=="o-add-id":
        while True:
            name_input=input("name first:")
            if name_input=="back":
                break
            elif name_input in dict_oname:
                print("This name is in the orgname")
                print(dict_oname.get(name_input))
                id_input=input("input id:")
                if id_input=='back':
                    break
                else:
                    dict_oname.get(name_input)['id']=id_input
            else:
                print("This name is not in the orgname")
    elif tempinput=="o-add-tips":
        print("tips is not developed")
    elif tempinput=="o-output-all":
        print(dict_oname)
        print(len(dict_oname))
    elif tempinput=='o-delet-all':
        dict_oname.clear()
        print(dict_oname)
        print("dict_oname is clear")
    elif tempinput=="o-delet-name":
        while True:
            name_input=input("name first:")
            if name_input=="back":
                break
            elif name_input not in dict_oname:
                print("{} is not in dict_oname".format(name_input))
            else:
                dict_oname.get(name_input).clear()
    elif tempinput=="o-modify":
        while True:
            print(dict_oname)
            name_input=input('name first')
            if name_input=='back':
                break
            elif name_input not in dict_oname:
                print("{} is not in dict_oname".format(name_input))
            else :
                while True:
                    print(dict_oname.get(name_input))
                    # modify_dict=dict_oname.get(name_input)
                    tempinput=input("What you want to modify:")
                    if tempinput == "back":
                        break
                    elif tempinput == "name":
                        new_name_input=input("new name:")
                        if new_name_input in dict_oname:
                            print("the new name '{}' is in the dict_oname".format(new_name_input))
                        else:
                            dict_oname[new_name_input]=dict_oname.pop(name_input)
                            print("name modify finish")
                    elif tempinput=="id":
                        new_id_input=input("new id:")
                        dict_oname[name_input]["id"]=new_id_input
                        print("id modify finish")
                    elif tempinput=="tips":
                        new_tips_input=input("new tips:")
                        dict_oname[name_input]["tips"]=new_tips_input
                        print("tips modify finish")
                    else :
                        print("input error")
    elif tempinput=="p-add-name":
        while True:
            add_name_input=input("finish name:")
            if add_name_input=="back":
                break
            elif add_name_input in dict_pname:
                print("{} is in the dict_pname")
            elif add_name_input not in dict_oname:
                print("{} is not in the dict_oname ,name error")
            else:
                temp_dict=dict_oname[add_name_input]
                dict_pname[add_name_input]=temp_dict
                print("add_pname finish")
                print(dict_pname[add_name_input])
    elif tempinput=="p-output-all":
        print(dict_pname)
    elif tempinput=="p-output-name":
        print(dict_pname.keys())
    elif tempinput=="p-delet-all":
        dict_pname.clear()
        print("dict_pname clear finish")
    elif tempinput=="p-delet-name":
        while True:
            delet_name=input('the name what you want to delet:')
            if delet_name=="back":
                break
            elif delet_name not in dict_pname:
                print("{} is not in the dict_pname".format(delet_name))
            else:
                dict_pname.pop(delet_name)
    elif tempinput=="output-all":
        print(dict_oname)
        print(dict_pname)
    else :
        print("fun error:101")


#     a=input("操作模式")
#     print(type(name_list))
#     sum_num = 0
#     if a=="1":#add name
#         while True:
#             append_nm=input("input name:(back)")
#             if append_nm=="back":
#                 break
#             elif append_nm in name_list:
#                 print("{} is in the name_list".format(append_nm))
#             elif append_nm not in orgname_list:
#                 print("{} is not in the orgname_list".format(append_nm))
#             else:
#                 name_list.append(append_nm)
#     elif a=="2":#output namelist
#         print(name_list)
#         print("the sum is {}".format(len(name_list)))
#     elif a=="3":#delet name
#         while True:
#             print(name_list)
#             delet_name=input("input name:want to delet(back)")
#             if delet_name=="back":
#                 break
#             elif delet_name not in name_list:
#                 print("{} is not in name_list".format(delet_name))
#             else:
#                 name_list.remove(delet_name)
#     elif a=="4":#output no list name
#         for temp_name in orgname_list:
#             if temp_name not in name_list:
#                 print(temp_name,end=" ")
#                 sum_num+=1
#         print("the sum is {} ".format(sum_num))
#     elif a=="5":#add orgnamelist
#         while True:
#             append_nm=input("input name:(back)")
#             if append_nm=="back":
#                 break
#             elif append_nm in orgname_list:
#                 print("{} is in the orgname_list".format(append_nm))
#             else:
#                 orgname_list.append(append_nm)
#     elif a=="6":#delet orgnamelist
#         while True:
#             print(orgname_list)#
#             delet_name=input("input name:want to delet(back)")
#             if delet_name=="back":
#                 break
#             elif delet_name not in orgname_list:
#                 print("{} is not in orgname_list".format(delet_name))
#             else:
#                 orgname_list.remove(delet_name)
#     elif a=="break":#break
#         break
#     elif a=="101":#debug
#         print("name_list == {}".format(name_list))
#         print(len(name_list))
#         print("orgname_list =={}".format(orgname_list))
#         print(len(orgname_list))

#     name_list=list(set(name_list))
#     name_list.sort()
# #add \n
# fname_list=[]
# for temp_list in name_list:
#     fname_list.append(temp_list+'\n')
# forgname_list=[]
# for temp_list in orgname_list:
#     forgname_list.append(temp_list+'\n')

# opnlist = open ('python\listmagnger\\namelist\oprlist.txt','w')
# opnlist.writelines(fname_list)
# opnlist.close()
# opnlist = open ('python\listmagnger\\namelist\orglist.txt','w')
# opnlist.writelines(forgname_list)
# opnlist.close()


js = json.dumps(dict_oname)
file = open('python\listmagnger\\namelist\dit_onamelist.txt', 'w')  
file.write(js)
file.close()
js = json.dumps(dict_pname)
file = open('python\listmagnger\\namelist\dit_pnamelist.txt', 'w')  
file.write(js)
file.close()

