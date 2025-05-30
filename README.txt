$ python -m venv .venv

$ source ./.venv/Scripts/activate

$ pip install pytest pytest-html playwright pytest-playwright pytest_tagging

pytest tests/. -v --browser=chromium --slowmo 500 --headed --html=report.html 

pytest tests/. -v --tags JIRA-1 --browser=chromium --slowmo 500 --headed --html=report.html

$ playwright install

[-v]                                - Verbose
[--tags name]                       - Run specific tags
[--browser chromium|firefox|webkit] - Specific browser
[--slowmo 500]                      - Waits for each command
[--headed]                          - Hide browser
[--html=report.html]                - Generates report.html

$ playwright show-trace ./traces/XXX/trace-XXX.zip

$ PWDEBUG=1 pytest tests/test_product_list.py -v --tags JIRA-4 --browser=chromium --slowmo 500 --headed --html=report.html