@echo off
REM ~ url https://github.com/MichaelB7/Stockfish/releases

REM ~ set PATH=%cd%\mingw64\bin;%cd%\msys\1.0\bin;%PATH%
REM ~ cd %cd%\McBrain\src"

make profile-build ARCH=x86-64-bmi2 COMP=mingw
strip McBrain_2017.exe
REM ~ move McBrain_2017.exe ..\McBrain_2017_x64_bmi2.exe
make clean

REM ~ set PATH=%cd%\mingw32\bin;%cd%\msys\1.0\bin;%PATH%

make profile-build ARCH=x86-32-old COMP=mingw
strip McBrain_2017.exe
REM ~ move McBrain_2017.exe ..\McBrain_2017_32bit.exe
make clean
