import os
import json
#原始表：所有的学号姓名等基本信息
#完成表、操作表：
#打开操作表-操作输出名单-重置
print(os.getcwd())



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

try:
    file_oname=open("namelist\dit_onamelist.txt","r+")
    js_oname=file_oname.read()
    #print(js_oname)
    #print(type(js_oname))
    dict_oname=json.loads(js_oname)
except:
    print("dit_onamelist.txt open failed")
# print(type(dict_oname))
# print(dict_oname)

# print(dict_oname["andy"]["age"])
try:
    file_pname=open("namelist\dit_pnamelist.txt","r+")
    js_pname=file_pname.read()
    dict_pname=json.loads(js_pname)
except:
    print("dit_pnamelist.txt open failed")
# porgnamelist = open ('python\\listmagnger\\namelist\\orglist.txt','r')
# porgname_list=porgnamelist.readlines()
# porgnamelist.close()

# opnlist = open ('python\\listmagnger\\namelist\\oprlist.txt','r')
# pname_list=opnlist.readlines()
# opnlist.close()
#delete \n
# name_list=[]
# orgname_list=[]
# print(type(name_list))
# for temp_list in pname_list:
#     temp_list=temp_list.strip("\n")
#     name_list.append(temp_list)
# for temp_list in porgname_list:
#     orgname_list.append(temp_list.strip("\n"))

try:
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
            print("output\n\toutput no finish name list")
            print("init_\n\tinit onamelist")
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
                print(dict_oname)
                print(len(dict_oname),end="\n====**===")
                name_input=input("input name:(you want to delet)")
                if name_input=="back":
                    break
                elif name_input not in dict_oname:
                    print("{} is not in dict_oname".format(name_input))
                else:
                    besure=input("are you sure to delet {}:(y/...)".format(name_input))
                    if besure=="y" or besure=="Y":
                        dict_oname.pop(name_input)
                        print("{} delete finish".format(name_input))
                    else:
                        print("{} delete fail".format(dict_oname))
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
                    print("{} is in the dict_pname".format(add_name_input))
                elif add_name_input not in dict_oname:
                    print("{} is not in the dict_oname ,name error".format(add_name_input))
                else:
                    temp_dict=dict_oname[add_name_input]
                    dict_pname[add_name_input]=temp_dict
                    print("{} add_pname finish".format(add_name_input))
                    # print(dict_pname[add_name_input])
        elif tempinput=="p-output-all":
            print(dict_pname)
        elif tempinput=="p-output-name":
            print(dict_pname.keys())
            print(len(dict_pname.keys()))
        elif tempinput=="p-delet-all":
            dict_pname.clear()
            print("dict_pname clear finish")
        elif tempinput=="p-delet-name":
            while True:
                print(dict_pname)
                print(len(dict_pname),end="\n")
                name_input=input("input name(you want to delet):")
                if name_input=="back":
                    break
                elif name_input not in dict_pname:
                    print("{} is not in dict_pname".format(name_input))
                else:
                    besure=input("are you sure to delet {}:(y/...)".format(name_input))
                    if besure=="y" or besure=="Y":
                        dict_pname.pop(name_input)
                        print("{} delete finish".format(name_input))
                    else:
                        print("{} delete fail".format(dict_pname))
        elif tempinput=="output-all":
            print("onamelist:")
            print(dict_oname)
            print(len(dict_oname))
            print("pnamelist:")
            print(dict_pname)
            print(len(dict_pname))
        elif tempinput=="output":
            for name in dict_oname:
                if name not in dict_pname:
                    print(name,end=" ")
            print()
        elif tempinput=="init_":
            dict_oname={"\u5468\u6590\u7136": {}, "\u7530\u96e8\u6674": {}, "\u9b4f\u8513\u6e1d": {}, "\u738b\u82cf\u7136": {}, "\u5f20\u6676\u6676": {}, "\u4f5f\u8d5b\u6960": {}, "\u8c37\u6587\u6587": {}, "\u539f\u5b5d\u6dfb": {}, "\u5b59\u6587\u793c": {}, "\u59dc\u6d77\u946b": {}, "\u8521\u666f\u8d35": {}, "\u59da\u5929\u5b87": {}, "\u5f20\u660e\u8fea": {}, "\u5218\u53cc\u777f": {}, "\u4e8e\u4eac\u6dde": {}, "\u6bb5\u9701\u822a": {}, "\u9648\u4f73\u8302": {}, "\u8d56\u6b63\u8f89": {}, "\u674e\u52c3\u7136": {}, "\u738b\u70ab\u6d66": {}, "\u5f20\u8d75\u667a\u5eb7": {}, "\u738b\u6668": {}, "\u9ea6\u9f99\u6cc9": {}, "\u8bb8\u4f73\u5ef7": {}, "\u90d1\u94b0\u5c71": {}, "\u674e\u9e4f": {}, "\u4e25\u5cf0": {}, "\u66f9\u6c38\u6770": {}, "\u674e\u6069\u6cfd": {}, "\u5173\u6dde\u6dcb": {}, "\u5510\u7389\u5c27": {}, "\u738b\u701a\u5174": {}, "\u6155\u5347\u5347": {}, "\u5c39\u5723\u6dfc": {}, "\u738b\u6a31\u6d01": {}, "\u674e\u5fe0\u667a": {}, "\u9648\u76c8\u8bfa": {}, "\u5f90\u4e1c": {}, "\u5415\u601d\u8fbe": {}, "\u738b\u51a0\u8212": {}}
        else :
            print("fun error:101")
except:
    print("main run failed")

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

try:
    js = json.dumps(dict_oname)
    file = open('namelist\dit_onamelist.txt', 'w+')  
    file.write(js)
    file.close()
except:
    print("write onamelist.txt failed")
try:
    js = json.dumps(dict_pname)
    file = open('namelist\dit_pnamelist.txt', 'w+')  
    file.write(js)
    file.close()
except:
    print("write pnamelist.txt failed")
