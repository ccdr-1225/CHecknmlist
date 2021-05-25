import os
#原始表：所有的学号姓名等基本信息
#完成表、操作表：
#打开操作表-操作输出名单-重置
print(os.getcwd())
porgnamelist = open ('python\listmagnger\orglist.txt','r')
porgname_list=porgnamelist.readlines()
porgnamelist.close()

opnlist = open ('python\listmagnger\oprlist.txt','r')
pname_list=opnlist.readlines()
opnlist.close()

#delete \n
name_list=[]
orgname_list=[]
print(type(name_list))
for temp_list in pname_list:
    temp_list=temp_list.strip("\n")
    name_list.append(temp_list)
for temp_list in porgname_list:
    orgname_list.append(temp_list.strip("\n"))


while True:
    print("1：添加已观看")
    print("2：导出已观看")
    print("3：删除已观看")
    print("4：导出未观看")
    print("5：添加原名单")
    print("6：删除原名单")
    print("break：退出")

    a=input("操作模式")
    print(type(name_list))
    sum_num = 0
    if a=="1":#add name
        while True:
            append_nm=input("input name:(back)")
            if append_nm=="back":
                break
            elif append_nm in name_list:
                print("{} is in the name_list".format(append_nm))
            elif append_nm not in orgname_list:
                print("{} is not in the orgname_list".format(append_nm))
            else:
                name_list.append(append_nm)
    elif a=="2":#output namelist
        print(name_list)
        print("the sum is {}".format(len(name_list)))
    elif a=="3":#delet name
        while True:
            print(name_list)
            delet_name=input("input name:want to delet(back)")
            if delet_name=="back":
                break
            elif delet_name not in name_list:
                print("{} is not in name_list".format(delet_name))
            else:
                name_list.remove(delet_name)
    elif a=="4":#output no list name
        for temp_name in orgname_list:
            if temp_name not in name_list:
                print(temp_name,end=" ")
                sum_num+=1
        print("the sum is {} ".format(sum_num))
    elif a=="5":#add orgnamelist
        while True:
            append_nm=input("input name:(back)")
            if append_nm=="back":
                break
            elif append_nm in orgname_list:
                print("{} is in the orgname_list".format(append_nm))
            else:
                orgname_list.append(append_nm)
    elif a=="6":#delet orgnamelist
        while True:
            print(orgname_list)#
            delet_name=input("input name:want to delet(back)")
            if delet_name=="back":
                break
            elif delet_name not in orgname_list:
                print("{} is not in orgname_list".format(delet_name))
            else:
                orgname_list.remove(delet_name)
    elif a=="break":#break
        break
    elif a=="101":#debug 
        print("name_list == {}".format(name_list))
        print(len(name_list))
        print("orgname_list =={}".format(orgname_list))
        print(len(orgname_list))

    name_list=list(set(name_list))
    name_list.sort()
#add \n
fname_list=[]
for temp_list in name_list:
    fname_list.append(temp_list+'\n')
forgname_list=[]
for temp_list in orgname_list:
    forgname_list.append(temp_list+'\n')

opnlist = open ('python\listmagnger\oprlist.txt','w')
opnlist.writelines(fname_list)
opnlist.close()
opnlist = open ('python\listmagnger\orglist.txt','w')
opnlist.writelines(forgname_list)
opnlist.close()

