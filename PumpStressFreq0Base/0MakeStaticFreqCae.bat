@echo off      
@set PATH=C:\SIMULIA\Commands\;%PATH%
@cd %cd%   
rem abaqus.bat cae noGUI=test.py 
rem abaqus.bat cae script=0MakeStaticFreqCae.py
abaqus.bat cae noGUI=0MakeStaticFreqCae.py

pause