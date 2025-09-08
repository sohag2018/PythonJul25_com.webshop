#pytest.main([])

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
pytest.main([f'--html={report_name}','--browser=chrome',
             '--self-contained-html'])

