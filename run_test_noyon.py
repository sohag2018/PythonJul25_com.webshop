#pytest.main([])
'''pytest.main() is a Python function provided by the pytest library that allows you to run pytest programmatically from within a Python script, rather than using the command line.

Run by right click or in terminal execute command 'python <runner.py>'

'''
from datetime import datetime
import os

import pytest

#generate data and time
timestamp=datetime.now().strftime('%y%m%d%H%M%S')
#ensure report folder exists
os.makedirs('Reports',exist_ok=True)
#reportname making
report_name=f'Reports/automation_testReport_{timestamp}.html'

#calling main()--to pass all command what we would in command line
pytest.main([f'--html={report_name}','--browser=firefox',
             '--self-contained-html',
             'testCases/test_sohag_02_HomePage_LogoValidation.py',
             'testCases/test_sohag_03_LoginTestWithValidCredentials.py'])

