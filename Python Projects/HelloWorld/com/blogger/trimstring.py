string = '    Python Trim String   '
print('Original String is - \'' + string + '\'')
print('Removing Trailing Space - \'' + string.rstrip()+ '\'')
print('Removing Leading Space - \'' + string.lstrip()+ '\'')
print('Trimmed String is - \'' + string.strip()+ '\'')

from datetime import datetime
startDate = datetime.fromisoformat("2022-12-05")
print(startDate)