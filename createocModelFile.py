#!/usr/bin/python
# -*- coding: UTF-8 -*-


#这个python 脚本 用来生成 oc 的模型文件  传入 文件名  以及 对应的 包含 模型字典的文件  就会生成 oc 的 .h 和 .m文件



#首先 需要接受 命令行中传进来的 文件  （存放的是 模型对应的json数组）




import sys, getopt ,os , time





def openInputFile(fileName,ofileName) :
	
	"在这个类里面 处理 传进来的文件内容然后转化成字典并且  写入到  新的文件中去 （文件路径就是当前终端打开的路径）"
	fo = open(fileName,"rb")
	
	string =  fo.read()
	print "输入的文件中的 字符串 ：", string
	
	string = string.replace("=",":")
	print string
	dic = eval(string)
	print dic
	
	list =  dic.keys()
	print list
	fo.close()
	
	
	outfileName = ofileName + ".h"
	foc = open(outfileName,"wb+")
	
# 	foc.write("//create by wangshen\n")
# 	foc.write
# 	foc.write("shuxing")
	localTime =  time.localtime(time.time())
	print localTime.tm_mday
# 	dateString = chr(localTime.tm_mday) + "/" + chr(localTime.tm_mon) + "/" + chr(localTime.tm_year)
	dateString = "%d/%d/%d" % (localTime.tm_mday,localTime.tm_mon,localTime.tm_year)
	ocString = "//\n//  %s .h\n//\n//\n//  Created by wangshen on %s.\n//  Copyright © 2015年 wangshen. All rights reserved.\n//" % (outfileName , dateString)
	ocString = ocString + "\n\n\n#import <Foundation/Foundation.h>"
	ocString = ocString + "\n\n@interface %s : NSObject\n\n" % ofileName
	
	apString = "\n@property (nonatomic,copy) NSString *"
	for pname in list :
		ocString = ocString + apString + pname + "\n"
		
	ocString = ocString + "\n\n@end"
# 	ocString = ocString + ""
	
	foc.write(ocString)
	foc.close()
	

	
	



def main(argv):
    inputfile = ''
    outputfile = ''
    try:
       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
       print(opts)
       print(args)
    except getopt.GetoptError:
       print 'test.py -i <inputfile> -o <outputfile>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print 'test.py -i <inputfile> -o <outputfile>'
          sys.exit()
       elif opt in ("-i", "--ifile"):
          inputfile = arg
       elif opt in ("-o", "--ofile"):
          outputfile = arg
          print '输入的文件为：', inputfile
          print '输出的文件为：', outputfile
          
          
          fo = open(inputfile,"rb")
          print fo.name
          print fo.mode 
          print fo.closed   
          string = fo.read()
          print fo.tell()
          print string
          
          openInputFile(inputfile,outputfile)
               
# 		  print fo.tell()string =  fo.read()
# 		  print "输入的文件中的 字符串 ：", string
#          openInputFile(inputfile)
          
          
          
          
          

if __name__ == "__main__":
    main(sys.argv[1:])



