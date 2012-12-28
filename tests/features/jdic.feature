Feature: Get sentence word by word translation using JDic API

    Scenario: Try to translate japanese sentence
        Given I have the sentence "体を癒すために。"
        When I query JDic API
        Then I get 3 translated terms
        And All translated terms are found in original sentence


