from numpy import*
import operator
#定义KNN算法分类器函数
#函数参数包括：（测试数据，训练数据，分类，K值）
def classify(inX,dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5 #计算欧式距离
    sortedDistIndicies=distances.argsort() #从小到大进行排序并返回index
    #选择距离最近的k个值
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        #D.get(k[,d]) -> D[k] if k in D, else d. d defaults to None.
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    #排序
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]#返回发生频率最高的元素标签
#定义生成“训练样本集”的函数，包含特征和分类信息
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.1],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

#定义一个将文本转化为numpy的函数
def file2matrix(filename):
    fr=open(filename) #读取文件
    arraylines=fr.readlines() #获取样本个数
    numberOfLines=len(arraylines) #得到行数
    returnMat=zeros((numberOfLines,3)) #构造全为0的零矩阵
    classLabelVector= [] #初始化标签数组
    index=0 #样本的索引
    #解析文件
    for line in arraylines:
        line=line.strip() #删除空白符（包括'\n', '\r',  '\t',  ' ')
        listFromLine=line.split('\t') #按照('\t')进行拆分
        returnMat[index,:]=listFromLine[0:3] #得到特征变量
        classLabelVector.append(int(listFromLine[-1])) #得到目标分类变量
        index+=1
    return returnMat,classLabelVector
