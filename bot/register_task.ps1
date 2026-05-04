$action = New-ScheduledTaskAction -Execute (Join-Path $PSScriptRoot 'start_bot.bat') -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -AtStartup
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 365)
Register-ScheduledTask -TaskName 'kotohira-quiz-bot' -Description 'Kotohira Daily Quiz Discord Bot' -Action $action -Trigger $trigger -Settings $settings
