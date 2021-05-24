import os
from robot import run

suites = [
    'robot-suites/powerapp-demo-test-suite.robot'
]

root_path = os.path.dirname(__file__)
results = os.path.join(root_path, 'results')

for suite in suites:
    run(os.path.join(root_path, suite),
        report=suite.replace('.robot', '.html'),
        output=suite.replace('.robot', '.xml'),
        log=suite.replace('.robot', '_log.html'),
        loglevel='DEBUG',
        outputdir=results)
