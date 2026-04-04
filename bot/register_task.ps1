$action = New-ScheduledTaskAction -Execute 'C:\Users\user\kotohira-quiz\bot\start_bot.bat' -WorkingDirectory 'C:\Users\user\kotohira-quiz\bot'
$trigger = New-ScheduledTaskTrigger -AtStartup
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 365)
Register-ScheduledTask -TaskName 'kotohira-quiz-bot' -Description 'Kotohira Daily Quiz Discord Bot' -Action $action -Trigger $trigger -Settings $settings
