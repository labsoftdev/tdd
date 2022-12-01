# Feature: xUnit

## Scenario_1: Invoke test method

**Given**: user created a test case. <br>
**When**: user launch a test case. <br>
**Then**: test method should be invoked. <br>

## Scenario_2: Invoke setUp first

**Given**: user created a setUp and a test case. <br>
**When**: user launch a test case. <br>
**Then**: setUp should be invoked before test case. <br>

## Scenario_3: Log string in WasRun

**Given**: user created a test case. <br>
**When**: user launch a test case. <br>
**Then**: Log string should be generated. <br>

## Scenario_4: Invoke tearDown afterward

**Given**: user created a test case and a tearDown. <br>
**When**: user launch a test case. <br>
**Then**: tearDown should be invoked after test case. <br>

## Scenario_5: Invoke tearDown afterward even if the test method fails

**Given**: user created a test case and a tearDown. <br>
**When**: user launch a test case and test fails. <br>
**Then**: tearDown should be invoked. <br>