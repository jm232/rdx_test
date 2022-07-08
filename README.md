#Introduction
rdx exercise for hiring purposes
##Manual testing part
Please see file `manual_testing/notes.md`
##Automation part
Python based framework for UI and API tests.
- UI part used `selenium` library and chrome browser. Failed step is screenshoted, saved and published to report.
- API part used `requests` as HTTP library

Project saved in `automation` directory
###Prerequisites
1. Running simple app
2. Cloned repo https://github.com/jm232/rdx_test
3. Installed:
   - Python [v3.8]
   - Java [v1.8]
   - PyCharm
   - Allure [v2.17.2]
   - pip [v22.0.4]
4.  Install packages
```
pip install -r .\automation\requirements.txt
```
###Structure
.
├── automation                  # root folder for automated tests
│   ├── features                # feature test file with test scenarios
│   ├── page_objects            # Definition of UI elements and functions related to them
│   ├── steps                   # Action steps
│   ├── utilities               # folder for various configuration files (file operation, screenshots, logging, selenium functions) 
│   ├── environment.py          # Hook structure 
│   ├── fixtures.py             # Browser setting
│   ├── requirements.txt        # List of packages
│   └── properties.ini          # Property files
├── manual_testing

###Test Execution:
[Executed on Windows env]

UI
```
behave .\automation\features\ui\BasicUITest.feature -f allure_behave.formatter:AllureFormatter -o ./automation/reports/
```
Api
```
behave .\automation\features\api\BasicAPITest.feature -f allure_behave.formatter:AllureFormatter -o ./automation/reports/
```
Test Report:
```
allure serve {ROOT_DIR}\automation\reports
```