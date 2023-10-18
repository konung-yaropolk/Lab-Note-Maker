#!/usr/bin/powershell -Command

Start-Process -FilePath "python" -ArgumentList "lab-note-maker.py" -NoNewWindow -Wait
Write-Host "Press any key to exit..."
Read-Host