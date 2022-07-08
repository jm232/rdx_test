Feature: Simple Application API Movie functionality

  @api
  Scenario: Get movie not present in list
    When I call GET request on movie service "62c774c356998bdf1fb4c2b6"
    Then I get a "404" response
    And I log response from the server

  @api
  Scenario: Post new movie without body
    When I call POST request on movie service without body
    Then I get a "400" response
    And I log response from the server

  @api
  Scenario: Post new Movie
    When I call POST request on movie service
    """
    {"name":"Last Scout","rating":"7","time":["134"]}
    """
    Then I get a "208" response
    And I log response from the server

  @api
  Scenario: Get All Movies
    When I call GET request on movies service
    Then I get a "200" response
    And I log response from the server

  @api
  Scenario: Update new Movie
    When I call POST request on movie service
    """
    {"name":"Old Shatterhand","rating":"7","time":["134"]}
    """
    Then I get a "208" response
    And I log response from the server
    When I call GET request on movies service
    Then I get a "200" response
    When I call PUT request on movie service "Old Shatterhand"
    """
    {"name":"Vinnetou","rating":"8","time":["134"]}
    """
    Then I get a "200" response
    And I log response from the server