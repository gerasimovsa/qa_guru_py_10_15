# Test Automation Project of OZ.by e-commerce service

----
> [Link to the OZ.by](https://oz.by//)

![](assets\ozby.PNG)

----

## List of implemented autotests:

### UI tests:

- [x] New profile registration with phone number
  - **_NOTE:_** Currently skipped
- [x] Login into existing user profile
- [x] Logout from current profile
- [x] Product catalog navigation
- [x] Search in product catalog
- [x] Filtering search results in catalog
- [x] Adding product into cart
- [x] Removing product from cart
- [x] Adding product to favorites
- [x] Removing product from favorites


----

### The project is implemented using the following tools:

<p  align="left">
<code><img width="5%" title="python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
<code><img width="5%" title="selene" src="assets\selene.png"></code>
<code><img width="5%" title="selenium" src="assets\selenium.png"></code>
<code><img width="5%" title="pytest" src="assets\pytest.png"></code>
<code><img width="5%" title="selenoid" src="assets\selenoid.PNG"></code>
<code><img width="5%" title="jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"></code>
<code><img width="5%" title="allure" src="assets\allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="assets\allure_testops.png"></code>
<code><img width="5%" title="github" src="assets\github.png"></code>  
<code><img width="5%" title="telegram" src="assets\tg.png"></code>   
<code><img width="5%" title="pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>  

----

## Running tests locally

Необходимо создать файл `.env` и заполнить его актуальными тестовыми параметрами.  
Пример заполнения файла указан в файле `.env.example`

1) Sync the [project](https://github.com/gerasimovsa/qa_guru_py_10_15)
2) Create `.env` file in the root directorry
3) Enter valid test data into `.env` file similarly to `.env.example` in the root directory
4) Run the following command in the CLI:
   
   ```commandline
   pytest -s -v
   ```

5) Run the following command in the CLI to generate Allure Report:

   ```commandline
   allure serve tests/allure-results
   ```

----

## Running tests remotely on Jenkins server

> [Link to the Jenkins project](https://jenkins.autotests.cloud/job/10-sergey_ra9-qa_guru_py_10_15_homework)

![](assets\ozby.PNG)
----

#### Build Parameters:

`ENVIRONMENT` - by default is set to `PROD`

`COMMENT` - commentary for Allure Notification

1. Open [Jenkins project](https://jenkins.autotests.cloud/job/10-sergey_ra9-qa_guru_py_10_15_homework)
2. Select `Build with Parameters`
3. Adjust `COMMENT` parameter or leave the default
4. Select `Build`
5. After run ends navigate to `'`Allure`'` or `Allure TestOps`

----

### Allure Report Integration

> [Link to the Allure Report](https://jenkins.autotests.cloud/job/10-sergey_ra9-qa_guru_py_10_15_homework/5/allure/)

#### Detailed test reports are generated with logs, HTML, screenshots and video recording

![](assets\allure_reports_integration.PNG)

#### Video recording of launched test in Allure 

![](assets\allure_attachment_video.GIF)

----

### Allure TestOps Integration

> [Link to the Allure Report](https://jenkins.autotests.cloud/job/10-sergey_ra9-qa_guru_py_10_15_homework/5/allure/)

#### Jenkins launches are added into test management system

![](assets\allure_testops_integration.PNG)

----

### Allure Notifications Integration

#### Test results are send into Telegram chat with preview, links and comments

![](assets\allure_notifications.PNG)





