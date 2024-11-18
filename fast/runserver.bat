rem Activa el entorno virtual
call entornoVirtual\Scripts\activate

rem Cambio al directorio del proyecto
cd agencia_viajes

rem Ejecuta el servidor DJango
start py manage.py runserver

rem Espera unos segundos para que el servidor inicie
timeout /t 5 >nul

rem Entrar en el servidor DJango
start "" http://127.0.0.1:8000/

rem Regresa al directorio anterior
cd ..