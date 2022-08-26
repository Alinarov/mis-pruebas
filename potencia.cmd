@echo off
set /a "base = 2"
set /a  "potencia = 6"
set /a resultado=0

:funcion
set /a "resultado=%base%"
for /l %%i in (2 1 %potencia%) do (
set /a resultado = resultado * %base%
)
echo.Resultado = %resultado% 

pause