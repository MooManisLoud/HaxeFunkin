@echo off
title HFDownloader

echo Now making folders
echo.
mkdir plugins
cd plugins
mkdir thirdparty
cd thirdparty
mkdir discord_rpc
echo Installing...

pip install pypresence
pip install pyinstaller
pip install pyfiglet

cls

cd plugins
cd thirdparty
cd discord_rpc
echo > discord_rpc.py
echo import pypresence >> discord_rpc.py
echo import time >> discord_rpc.py
echo. >> discord_rpc.py
echo if __name__ == '__main__': >> discord_rpc.py
echo.    RPC = pypresence.Presence('client_id') >> discord_rpc.py
echo.    RPC.connect() >> discord_rpc.py
echo.    print('Connected to Discord rich presence RPC') >> discord_rpc.py
echo. >> discord_rpc.py
echo.    i = 0 >> discord_rpc.py
echo.    start = int(time.time()) >> discord_rpc.py
echo.    while i < 10: >> discord_rpc.py
echo.        i += 1 >> discord_rpc.py
echo. >> discord_rpc.py
echo.        RPC.update( >> discord_rpc.py
echo.            details='Iteration #{}'.format(i), >> discord_rpc.py
echo.            start=start, >> discord_rpc.py
echo.            large_image='default', >> discord_rpc.py
echo.            buttons=[{'label': 'Button 1', 'url': 'https://example.com'}, {'label': 'Button 2', 'url': 'https://example.com'}] >> discord_rpc.py
echo.        ) >> discord_rpc.py
echo. >> discord_rpc.py
echo.        time.sleep(2) >> discord_rpc.py
echo. >> discord_rpc.py
echo.    RPC.close() >> discord_rpc.py
echo.    print('Disconnected from Discord rich presence RPC') >> discord_rpc.py


echo should be fine now have fun!

pause