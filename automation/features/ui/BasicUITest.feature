Feature: Simple Application Movie functionality

  @ui
  Scenario Outline: Create new movie
    Given I enter simple app
    Then I go to Create Movie page
    When I create new movie with name "<name>", rating "<rating>" and time "<time>"
    Then I go to List Movies page
    Then I verify movie is present with name "<name>", rating "<rating>" and time "<time>"
    Examples:
      | name | rating | time |
      | Jurassic Park | 4 | 85 |

  @ui
  Scenario Outline: Delete movie
    Given I enter simple app
    Then I go to Create Movie page
    When I create new movie with name "<name>", rating "<rating>" and time "<time>"
    Then I go to List Movies page
    Then I delete movie with name "<name>"
    Examples:
      | name | rating | time |
      | Brideshead Revisited | 9 | 115 |

  @ui
  Scenario Outline: Update movie
    Given I enter simple app
    Then I go to Create Movie page
    When I create new movie with name "<name>", rating "<rating>" and time "<time>"
    Then I go to List Movies page
    When I update movie with name "<name>" to name "<updated_name>", rating "<updated_rating>" and time "<updated_time>"
    Then I go to List Movies page
    Then I verify movie is present with name "<updated_name>", rating "<updated_rating>" and time "<updated_time>"
    Examples:
      | name | rating | time | updated_name | updated_rating | updated_time |
      | Mission | 10 | 75 | Yes Man        | 5              | 90          |

  @ui
  Scenario Outline: Filter movie
    Given I enter simple app
    Then I go to Create Movie page
    When I create new movie with name "<name>", rating "<rating>" and time "<time>"
    Then I go to List Movies page
    Then I filter movie name "<name>" by value "<value>"
    Examples:
      | name | rating | time | value |
      | Inception | 3 | 105 | ception   |
    And I verify movie is present with name "<name>", rating "<rating>" and time "<time>"

  @ui
  Scenario: Validation on empty input fields
    Given I enter simple app
    Then I go to Create Movie page
    When I click on Add Movie button
    Then I verify error message




