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
    print("3：导出未观看")
    print("4：退出")

    a=int(input("操作模式"))

    sum_num = 0
    if a==1:
        append_nm=input("input name:")
        if append_nm in name_list:
            print("{} is in the name_list".format(append_nm))
        elif append_nm=="back":
            continue
        else:
            name_list.append(append_nm)
    elif a==2:
        print(name_list)
        print("the sum is {}".format(len(name_list)))
    elif a==3:
        for temp_name in orgname_list:
            if temp_name not in name_list:
                print(temp_name)
                sum_num+=1
        print("the sum is {} ".format(sum_num))
    elif a==4:
        break
    elif a==101:
        print(name_list)
        print(len(name_list))
        print(orgname_list)
        print(len(orgname_list))

    name_list=list(set(name_list))
    name_list.sort()
#add \n
fname_list=[]
for temp_list in name_list:
    fname_list.append(temp_list+'\n')

opnlist = open ('python\listmagnger\oprlist.txt','w')
opnlist.writelines(fname_list)
opnlist.close()

#更新日志 2021-5-18 Version 0.0.1.1 
#加入导出已观看时 加入人数统计
#修复已观看名单第一个为空的问题
#增加错误输入回调（开发者指令——back）
#增加数据查看入口101
