# -*- coding: UTF-8 -*-

#绘图区设置
def ViewSize():
  session.viewports['Viewport: 1'].restore()
  session.viewports['Viewport: 1'].setValues(origin=(0.0, -5.56111145019531), 
      width=150, height=120)
  session.viewports['Viewport: 1'].view.fitView()
  session.viewports['Viewport: 1'].view.setValues(nearPlane=700, 
      farPlane=1700, width=334.106, height=253.205, viewOffsetX=-19.8844, 
      viewOffsetY=0)
#EndDef

#仅显示坐标系
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=ON, 
    legend=OFF, title=OFF, state=OFF, annotations=OFF, compass=OFF)
#修改渲染模式：填充，隐藏边
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED, visibleEdges=NONE)
#云图设置为连续模式
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    contourStyle=CONTINUOUS)

##读取odb文件
#odb = session.openOdb(name = FileOdb)
#session.viewports['Viewport: 1'].setValues(displayedObject=odb)

session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=1)
#显示变形后云图
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.basicOptions.setValues(
    sweepSectors=ON, sectorSelectionType=SELECT_ALL)

ViewSize()

frame = odb.steps['Step-2'].frames
#输出频率的文本文件
if ii==0:
  f = open(FileOutFreq, 'w') # 打开文件， 用'w'重新写文件
  f.write('#共有%d阶固有频率(Hz)。后三列分别是密度(kg/m3)，弹性模量(GPa)和转速(r/min) \n' %(len(frame)-1))
else:
  f = open(FileOutFreq, 'a') # 打开文件， 用'a'追加写文件

for i in range(1,len(frame)):
  Freq=frame[i].frequency#频率值
  f.write('%10.2f  ' %(Freq)) # 将各阶固有频率写文本文件
  session.viewports['Viewport: 1'].odbDisplay.setFrame(step=1, frame=i)
  StrPng='Fig-Sample'+str_ii+'-Mode'+ '%02d' %i +'-Freq'+ '%.2f' %Freq +'.png'
  session.printOptions.setValues(vpDecorations=OFF)
  session.printToFile(fileName=StrPng, format=PNG, 
    canvasObjects=(session.viewports['Viewport: 1'], ))
    
f.write('%20.18e %20.18e %20.18e \n' %(rho, E, rpm))
f.close() 

session.odbs[FileOdb].close()

#判断目录是否存在
DirFig='Figs'
if not os.path.exists(DirFig):
  os.makedirs(DirFig) 
#将图片移动到目录
#StrCmd='@ move /y Fig*.png '+DirFig
#os.system(StrCmd)

for file in glob.glob("Fig*.png"):
  shutil.copy(file,DirFig)
  os.remove(file)
#EndFor