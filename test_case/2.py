def _score():
    sum_all=0
    with open('文件路径.txt','r') as f :
        lines = f.readlines()
        file_list =list(lines)
        for index,line in enumerate(file_list):
            if index==len(file_list)-1:
                sum_all += float(file_list[index].split(",")[2])
                print("同学%s的平均成绩为:"%k,"%.2f"%(sum_all/3))
                break

            k=line.split(',')[0]
            m=float(line.split(',')[2])
            next_item =file_list[index+1]
            next_k=next_item.split(',')[0]
            if k == next_k:
                sum_all+=m
            else:
                sum_all+=m
                print("同学%s的平均成绩为:"%k,"%.2f"%(sum_all/3))
                sum_all=0

if __name__=="__main__":
    _score()