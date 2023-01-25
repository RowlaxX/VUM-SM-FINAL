@echo off
# Windows script for testing

coverage run --branch SpaceTest.py
coverage report
coverage run --branch DegreeCoverage.py
coverage report