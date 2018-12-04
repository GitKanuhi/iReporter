**iReporter**
[![Build Status](https://travis-ci.org/GitKanuhi/iReporter.svg?branch=develop)](https://travis-ci.org/GitKanuhi/iReporter)
<a href="https://codeclimate.com/github/GitKanuhi/iReporter/test_coverage"><img src="https://api.codeclimate.com/v1/badges/32b126fff4706fd89cc5/test_coverage" /></a>

[iReporter](https://gitkanuhi.github.io/iReporter/)

Project Overview
Corruption is a huge bane to Africa’s development. African countries must develop novel and
localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables
any/every citizen to bring any form of corruption to the notice of appropriate authorities and the
general public. Users can also report on things that needs government intervention

**Design**

The iReporter contains the static pages showing the look-and-feel of the App.
[View the Designs Here](https://gitkanuhi.github.io/iReporter/)

**To Run the API**

First clone this Repo to your machine --->
https://github.com/GitKanuhi/iReporter.git

Then change the directory to the project by --->

``` cd iReporter ```

change to the active branch ---> ``` git checkout develop ```


Just to make sure all the packages needed to run the project present in your machine, create a virtual enviroment and install the packages there.

        To create a virtual enviroment run --->  virtualenv -p python3 venv

        To activate the enviroment --->  source venv/bin/activate 

The virtual enviroment is now ready, you should install all packages for the project to ensure you have pip installed otherwise then on your terminal run --->  ``` pip install -r requirements.txt ```

**Run**

To test the project on your terminal run --->   ``` export FLASK_APP=run.py ```

then ---> ``` flask run ```
