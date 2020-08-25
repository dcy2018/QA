import json
import argparse
#将多人标注答案所在句一致的问题及其所在句提取出来生成新的数据集
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type = str, default = "train-v1.1.json", help = 'source json to sini')
parser.add_argument('-o', '--output', type = str, default = "sini2train.json", help = 'json after sini')
parser.add_argument('-a', '--applenth', type = int, default = 0, help = '中心句的左右扩展宽度')

args = vars(parser.parse_args())
i = args['input']
o = args['output']
a = args['applenth']

#eg. lines = ['sd','fsgh','qrf'] s = [0, 3, 8]
def starts(lines): #输入split并重新添加句号后的句子列表，输出句首索引的列表
    s = [0]
    num = len(lines)
    for i in range(1, num):
        s.append(s[i-1] + len(lines[i-1]))
    return s

#eg. linestarts = [0, 5, 12, 24], answer_start = 14, loca = 2
def loca(linestarts, answer_start):
    j = 1
    num = len(linestarts)
    while ((j < num) and (answer_start >= linestarts[j])):
        j = j + 1
    j = j - 1
    return (j)

def newst(linestarts, answer_start, sloca):
    newst = answer_start - linestarts[sloca]
    return (newst)

    
def check(localist):
    lenth = len(localist)
    if (lenth == 1):
        return True
    for i in range(lenth-1):
        if (localist[i] != localist[i + 1]):
            return False
    return True
    
#检查三人标注答案是否在同一句中
def checksame(linestarts, answers):
    answer_num = len(answers)
    localist = []
    for i in range(answer_num):
        localist.append(loca(linestarts, answers[i]['answer_start']))
    if (check(localist)):
        return True
    return False

def addjuhao (list):
    l = []
    for i in list :
        j = i + '.'
        l.append(j)
    return l
    
def mkcon(location, lines, applenth):
    context = ''
    ss = 0
    ee = len(lines) - 1

    s = location - applenth
    e = location + applenth
    sloca = max(0, s)
    
    for i in range(s, e + 1):
        if (i >= ss and i <= ee) :
            context = context + lines[i] 

    return context, sloca
    
def sinitext(i, o):
    with open(i, 'r') as f:
        d = json.load(f)
    d2 = {"data":[],"version":1.1}
    data = d['data']
    
    for m in range(len(data)): #每title
        tt = {'title':'', 'paragraphs':[]}
        tt['title'] = data[m]['title']
        para = data[m]['paragraphs']
 
        for n in range(len(para)): #每context, len(para)是context数量
            context = para[n]['context']
            lines = context.split('.')
            lines.pop() #删除split导致的最后的空串
            lines = addjuhao(lines)
            linestarts = starts(lines)
            
            for k in range(len(para[n]['qas'])): #每question
                answers = para[n]['qas'][k]['answers']
                if checksame(linestarts, answers): #若多人标注答案在同一句中则接收
                    location = loca(linestarts, answers[0]['answer_start'])
                    pairs = {'context':'', 'qas':[{'question':'','answers':[],'id':''}]}
                    newtext , sloca = mkcon(location, lines, applenth = a)
                    pairs['context'] = newtext
                    #pairs['context'] = lines[location] + '.'
                    pairs['qas'][0]['question'] = para[n]['qas'][k]['question']
                    pairs['qas'][0]['id'] = para[n]['qas'][k]['id']
                    for i in range(len(answers)): #根据每份答案生成新的答案
                        text = para[n]['qas'][k]['answers'][i]['text']
                        answer_start = para[n]['qas'][k]['answers'][i]['answer_start']
                        newstart = newst(linestarts, answer_start, sloca)
                        answer = {'text':text, 'answer_start' : newstart}
                        pairs['qas'][0]['answers'].append(answer)
                    tt['paragraphs'].append(pairs)
        d2['data'].append(tt)
    
    
    with open(o, 'w') as f2:
        json.dump(d2, f2)

if (__name__ == '__main__'):
    sinitext(i, o)
