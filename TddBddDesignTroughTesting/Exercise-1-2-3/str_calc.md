# Feature: String Calculator


## Scenario_1:

**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is an empty string. <br>
**Then**: return value should be zero. <br>

## Scenario_2:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is a one number. <br>
**Then**: calculator should return a value of that number. <br>

## Scenario_3:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is multiple numbers. <br>
**Then**: calculator should return a sum of those numbers. <br>

## Scenario_4:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is multiple numbers, containing new-line (\n) delimiter. <br>
**Then**: calculator should return a sum of those numbers. <br>

## Scenario_5:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is multiple numbers, with delimiters defined by the user. <br>
**Then**: calculator should return a sum of those numbers. <br>

## Scenario_6:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is negative number. <br>
**Then**: calculator should rise an exception. <br>

## Scenario_7:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: input is negative number. <br>
**Then**: calculator should rise an exception with explanation. <br>

## Scenario_8:
**Given**: the user would like to calculate the result passed in string format. <br>
**When**: addition is performed. <br>
**Then**: expression and result should be displayed. <br>