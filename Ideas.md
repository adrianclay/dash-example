# Ideas for what else to explore:

- Can we write tests for the creation of the `number_of_accidents_per_day` variable?

  - Break out the behaviour into its own testable unit.
  - Set up some testing library for Python.
  - Understand how to assert that the dataframe you are returning is correct?!
    - Indexes ordered?
    - Are they in a "yyyy-mm-dd" format?
    - Are the values correct per day?

- Could we create visual regression tests?

  - https://www.browserstack.com/guide/visual-regression-testing
  - Note that this is just a description, there are likely lots of different tools etc to help with this, not just browser stack.

- Hosting the application within a cloud environment

  - Seen people use AWS
    [x] Heroku

- Set up a pipeline to deploy the application to the cloud environment.
  [x] Set up a linter for our code?
  [x] How do we style the dashboard?
  [x] Adding interactivity to the dashboard, in some way, a dropdown perhaps?
  [x] Add documentation to the README, as to how you install/run the project.

- Remove compiled python files already in git.
