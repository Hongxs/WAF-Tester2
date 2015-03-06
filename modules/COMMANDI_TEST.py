#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
from lib.logging import *
import time

def check_commandi_usecase(info,domain,method,i,logging_file):
	print "----------------"
#	print i,":",info
	res = check_usecase("/default.aspx",method,{"id":info},None,domain)
	print res[0]
        logging_file.writelog("-------------\n")
        logging_file.writelog(res[0]+"\n" )
        if res[1] == 400:
                print i,":",res[1],"   usecase:",info
                logging_file.writelog("[OK] "+ str(i) +" : "+ str(res[1]) +"   usecase:"+ info +"\n" )
        else:
                print '\033[1;31;40m'
                print i,":",res[1],"   usecase:",info
                print '\033[0m'
                logging_file.writelog("[!!] "+ str(i) +" : "+ str(res[1]) +"   usecase:"+info+"\n" )

def COMMANDI_TEST(domain,method,usecase):
	commandi_file = open(usecase)
	file_content_lines = commandi_file.readlines()
	commandi_file.close()
	i = 0
	logging_file = logging("result/commandi_result.txt")
	for line in file_content_lines:
		info = line.strip()
		i+=1
		if info != "":
			check_commandi_usecase(info,domain,method,i,logging_file)
			#time.sleep(5)
	logging_file.close()
