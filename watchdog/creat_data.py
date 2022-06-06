from  watchdog import watchtime

# 创建测试数据


'''#创建按小时执行的数据

生效时间只有一天的未生成告警记录，且未失效
# 1,按小时执行，5.15-5.19单位时间为1小时，每间隔2分钟执行1次，总清零次数为2，达到清零次数，不生成告警记录
# 2，按小时执行，5.15-5.19单位为2小时，间隔时间为20分钟执行一次，清零次数为2，未达到清零次数，（0点，2点，4，6，8，10，12，14，16，18，20，22，24）0分的59秒，40分的59秒，0分的59秒分别执行一次告警
3，按小时执行，5.15-5.15结束时间为当天，单位间隔时间为5小时，清零次数为2，前两次达到清零次数，（0，5，10，15，20）10，15，20生成告警记录
4，按小时执行，5.15-5.19设置休息时间5.19。5月19不生成告警记录，正常显示清零记录，时间间隔20分钟执行一次
5，按小时执行，5.15-5.20设置逾期时间为30s，单位间隔时间为每5小时，前两次达到清零次数，10，15，20点生成两条告警记录
'''
watchtime.login('zengjuan', 123456)
# watchtime.add_wathchdog('1', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',2,'',1,1,'00,02,04,06,08,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58',[])
# watchtime.wa()
# watchtime.edit_time('2022-05-14','2022-05-20')
# watchtime.add_wathchdog('2', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',2,'',2,1,'00,20,40',[])
# watchtime.add_wathchdog('3', '2022-05-14T16:00:00.000Z', '2022-05-14T16:00:00.000Z',2,'',2,1,'00,20,40',[])
# watchtime.add_wathchdog('4', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',3,'',2,1,'00,20,40',['2022-05-19'])
# watchtime.add_wathchdog('5', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',3,30,5,1,'00,20,40',[])
'''
1,生效时间，清零次数，清零时间范围，逾期，休息时间，清零时间间隔天是以小时告警
按天创建执行数据
5.15-5.19，每间隔1天，1个小时执行，清零次数为2，达到清零次数，每次时间为（0：59：59，1：59：59。。。。。）
5.15-5.19，每间隔6天，6小时执行，清零次数为2，未达到清零次数（0，6，12，18，）前两次达到
5.15-5.15，间隔时间为2天,设置时间为0，5点执行告警，未达到清零次数0：59：59 5：59：59告警一次，之后不再告警
5.15-5.19 每间隔1天，设置休息时间为5.18,清零次数为，0点执行告警，未达到清零次数告警时间为5.15 0：59.59，5.16 0：59：59，5.17 0：59：59 5.19 0：59：59
'''
# watchtime.add_wathchdog('1', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',2,'',1,2,'00,01,02,03,04,05,06,07,08',[])
# watchtime.add_wathchdog('2', '2022-05-14T16:00:00.000Z', '2022-05-18T16:00:00.000Z',2,'',6,2,'00,06,12,20',[])
# watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-30T16:00:00.000Z',2,'',2,2,'00,05',[])
watchtime.add_wathchdog('4', '2022-05-26T16:00:00.000Z', '2022-06-30T16:00:00.000Z',1,2,1,2,'00,05',['2022-05-27'])




'''按周创建执行数据
1,5.15-5.19 每间隔1周，清零次数为2，默认每周二（0点）执行，5，17执行，5.24执行，执行时间为5.17 0点，
2，5.15-5.30 每间隔2周，清零次数为2，默认为（周一，周三，周五，周日）0，16，18点执行，执行时间为（15日 0点 16点，18点）23，25，27，29日（0点，16点，18点）
3，5.16-6.6 每间隔3周，清零次数为2，默认为（周一0点执行） 执行时间为16日 0：59：59，6.5 0：59：59
'''
# watchtime.add_wathchdog('1', '2022-05-22T16:00:00.000Z', '2022-05-30T16:00:00.000Z',2,'',1,3,'周二(00时',[])
# watchtime.add_wathchdog('2', '2022-05-20T16:00:00.000Z', '2022-07-30T16:00:00.000Z',2,'',1,3,'周一(00时,周三(00时,周五(00时,周日(08时',[])
# watchtime.add_wathchdog('4', '2022-05-22T16:00:00.000Z', '2022-08-19T16:00:00.000Z',2,'',2,3,'(周一(00时,18时)，周三(00时,17时)，周五(00时,18时)，周日(00时',[])
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',3,3,'周一(00),'[])
'''按月创建执行数据
1,5，15-5.31 间隔1月，清零次数为2，每月的15日执行  5.15 23：59：59 
2，5.14-6.30 间隔1月，清零次数为2，15，25号，25号为休息日 15 23：59：59 14日有清零记录，6月15 23：59：59 
3，5.14-6.30 间隔两月，清零次数为2，15，25，25日为休息日 5.15 00：59：59 
'''
#watchtime.add_wathchdog('1', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',1,4,'15,'[])
#watchtime.add_wathchdog('2', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',1,4,'15,25',['2022-05-15'])
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',2,4,'15,25',['2022-05-25'])

'''按年创建执行数据
1，2021，2-2022，12 间隔1年，清零次数为2，2，5，10月，2021年2月28 ，21年5.3121年10月31 23：59：59  2022年1月31 23：59：59，2022年2月2.28 2022.10.31 
2，2021，1-2022，12 间隔2年 2，5，10，不会执行
3，2021，1-2024，1 间隔2年，2，5，12月，2023.2，2023，5，2023，12
4，2021-2024.1 间隔两年，休息时间为2023年2月 2023.5，2023，12 

'''
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',1,5,'2,5,10',[])
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',2,5,'2,5,10',[])
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',2,5,'2,5,12',[])
#watchtime.add_wathchdog('3', '2022-05-19T16:00:00.000Z', '2022-05-19T16:00:00.000Z',2,'',2,5,'2,5,12',['2023-02','2023-12'])





