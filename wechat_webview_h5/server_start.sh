#!/usr/bin/env bash
time=$(date "+%Y%m%d_%H%M%S")
appium --log ./logs/appium_log-${time}.log --chromedriver-executable ./chrome_drivers/chromedriver2.40_66-68