Set-Alias -Name my-python -Value 'C:\Users\lucas\Miniconda3\python.exe' 
Set-Alias -Name my-editor 'C:\Program Files (x86)\VSCodium\VSCodium-win32-x64-1.60.2\VSCodium.exe'

my-python math-journal.py
$time = Get-Date -Format "yyyy\\MM\\dd"
$title = $time + ".tex"
my-editor $title