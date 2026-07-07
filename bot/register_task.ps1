$action = New-ScheduledTaskAction -Execute (Join-Path $PSScriptRoot 'start_bot.bat') -WorkingDirectory $PSScriptRoot
# AtLogOn (2026-07-07): the old AtStartup trigger never fired on this machine
# (sleep/fast-startup usage means almost no clean boots; the bot had been down
# since 2026-05-04 without anyone noticing). Mirrors the proven hisho-bot
# logon-trigger pattern. -Force allows re-running this script to update.
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 365)
Register-ScheduledTask -TaskName 'kotohira-quiz-bot' -Description 'Kotohira Daily Quiz Discord Bot' -Action $action -Trigger $trigger -Settings $settings -Force
Write-Host "Registered kotohira-quiz-bot (at logon). Start now: Start-ScheduledTask -TaskName 'kotohira-quiz-bot'"
