# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by CJY on Wed Jul 27 21:40:57 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.20703, 1.20139), width=177.675, 
    height=119.178)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('C:/Users/CJY/Desktop/pump/PumpStressFreq0Base/0MakeStaticFreqCae.py', 
    __main__.__dict__)
#: 
#:  计算单只叶片静强度及动频�?循环周期对称)...
#: 
#:  读取ansa生成的inp文件...
#: ģ�� "Model-1" �Ѵ���.
#: ���� "PART-1" �Ѵ������ļ��е���.
#: �໥���� "Int-CycSymm" �Ѵ���.
#: ģ�� "Model-1" �Ѵ������ļ�����. 
#: �������϶��������Բ鿴����򾯸���Ϣ.
#: 
#:  读取Fluent生成的壁面压力数据，形成analytical field...
#: 
#:  修改static分析�?..
#: 
#:  创建Job...
#: 
#:  保存cae文件...
#: ģ�����ݿ��ѱ��浽 "C:\Users\CJY\Desktop\pump\PumpStressFreq0Base\PumpStaticFreq.cae".
#: 
#:  提交Job...
#: 		 提交时间:2022-07-27 21:41:05.600000
#: ����: 
#: Following warning detected while evaluating the pressure "Load-2"
#: from analytical field "AnalyticalField-Pres".
#: The mapper has mapped the field values using distance weighting 
#: algorithm for some of the target nodes.
#: 		 完成时间:2022-07-27 21:48:21.830000
#: 		 计算耗时:436.2265042s 
#: 
#:  后处理，提取应力应变�?..
#: ģ��: C:/Users/CJY/Desktop/pump/PumpStressFreq0Base/PumpStaticFreq.odb
#: װ�������:         1
#: װ���ʵ������: 0
#: ����ʵ���ĸ���:     1
#: ������:             1
#: ��Ԫ������:       3
#: ��㼯����:          6
#: �������ĸ���:              2
#: 
#:  后处理，提取频率�?..
#: 
#:  清除不必要的文件...
#: �µ�ģ�����ݿ��Ѵ���.
#: ģ�� "Model-1" �Ѵ���.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
print 'RT script done'
#: RT script done
