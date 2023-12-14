; script_instalacion.iss

[Setup]
AppName=AdmRedes
AppVersion=1.0
DefaultDirName={pf}\AdmRedes
DefaultGroupName=AdmRedes
OutputDir=.\Instalador

[Files]
Source: ".\dist\main.exe"; DestDir: "{app}"
Source: ".\dist\icono.png"; DestDir: "{app}"
Source: ".\dist\config.ini"; DestDir: "{app}"

[Icons]
Name: "{group}\AdmRedes"; Filename : "{app}\main.exe"; IconFilename: "{app}\icono.png"