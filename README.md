# Wyyder

<a href="https://twitter.com/wyyder">
      <img alt="Twitter - Follow..." title="Please Follow..." 
src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"/>
</a>

<a href="https://www.youtube.com/channel/UCklWKcVOeAAV1SC1eQwnLNQ?sub_confirmation=1">
      <img alt="Youtube - Please Subscribe..." title="Please Subscribe..." 
src="https://img.shields.io/badge/-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white"/>
</a>

## Projects
| Youtube | Project | Technology |
| --- | --- | --- |
| <a href="https://www.youtube.com/watch?v=xl77kz4eIwU"><img alt="Youtube - Please Subscribe..." title="Please Subscribe..." src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/></a> | [Python Robot Framework POC - Microsoft Power App (Help desk Ticket App)](https://github.com/wyyder/python-robot-framework-poc-microsoft-power-app/blob/master/README.md) | Python / Selenium / Robot Framework / Pycharm / VSCode / Microsoft Power App |


## Microsoft Power App (Help desk Ticket App) - Python - Robot Framework - POC

```
This is a Proof of concept Using Python, Selenium & Robot framework,
In which Automated Tests of Sample MicroSoft Power App (Help desk Ticket App)
```

**Objective**

- Check the Feasibility of Test Automation of MicroSoft Power Apps using Robot Framework
- Feasibility study in Chrome browser using a windows operating system

**Approach**

- A Sample Canvas app (Help desk Ticket App) is Used for this POC
- Expose only keywords in the PowerApp Library
- By importing PowerApp Library User has to create Robot file.
- Using the exposed keywords in library & by Sequencing them as Test steps in logical order we can achieve the Test use
  case.
- Implemented the browser actions, logs & assertions using pure python & Selenium.

**Challenges**

- Capturing XPath by finding the right IFrame
- Handing / Switching the context between the IFrames & Main browser in selenium.
- Arguments passing in robot file (Test data Management)

**Limitations**

- May face issue in Identifying elements in selenium using DOM

**Alternative**

- Microsoft released V1 of Power Apps Test studio A low-code solution to help makers build tests for their apps

Reference [https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/test-studio](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/test-studio)

__Author__ 
- Kiran Kumar
