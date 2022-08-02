# -*- coding: UTF-8 -*-

    
#根据Analytical Filed创建压力载荷
a = mdb.models['Model-1'].rootAssembly
region = a.surfaces['PRESSURE']
mdb.models['Model-1'].Pressure(name='Load-2', createStepName='Step-1', 
    region=region, distributionType=FIELD, field='AnalyticalField-Pres', 
    magnitude=1.0, amplitude=UNSET)

#创建圆柱坐标系
a = mdb.models['Model-1'].rootAssembly
Cylindrical1=a.DatumCsysByThreePoints(name='Cylindrical', coordSysType=CYLINDRICAL, 
    origin=(0.0, 0.0, 100.0), point1=(100.0, 0.0, 100.0), point2=(100.0,100.0,100.0))
#后续调用该圆柱坐标系RTZ
Cylindrical1 = a.datums[Cylindrical1.id]

#修改边界条件的坐标系为圆柱坐标系
mdb.models['Model-1'].boundaryConditions['Disp-BC-1'].setValues(localCsys=Cylindrical1)
mdb.models['Model-1'].boundaryConditions['Disp-BC-2'].setValues(localCsys=Cylindrical1)
mdb.models['Model-1'].boundaryConditions['Disp-BC-3'].setValues(localCsys=Cylindrical1)

#设置输出变量，其中S为应力、LE为真实应变、U为位移、NT为节点温度
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S','LE','U'), frequency=LAST_INCREMENT)