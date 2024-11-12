# Created by isaac at 11/9/2024
Feature: Tests for User Guide Page


  Scenario: User can open User guide page
    Given Open main page
    When Log in to the page
    And  Click on settings option
    And Click on User Guide option
    Then Verify the right page opens
    And Verify all lesson videos contain titles