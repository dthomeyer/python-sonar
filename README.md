Shortcut to Become a 10x Developer

Sonar is an industry standard platform that enables you and your team to produce better, more elegant, more serviceable, and more secure code. It helps you be more aware and think deeper about the problems you are solving. It also helps to take the mundane and guess work out of your way so you can focus on the fun stuff. The best of all, it is a mature tool that has been around for over a decade and is integrated with all major code-flow platforms, so the integration should be simple and familiar to many developers.
The tool enables the shift-left approach via linting so code quality is known to the developer before their code is committed and any problems can be addressed as they are identified, while the solution is still fresh in the author’s mind. Once committed, integrated scanners apply the same scrutiny to the solution in neutral, prescribed environment and report on the wider quality of the project.
Sonar supports integrated quality gates, which act as the approver of the code integration request. In case a questionable PR is submitted, a quality gate is executed by the central CI/CD platform and if it is not satisfied, the PR is rejected for the author to correct before it can become integrated into the main codebase.
The author is not left to fend on their own. Sonar provides detailed description of the problems found and how to address them. This serves as a didactic mean for developers to improve their approach, problem-solving, and awareness.


Sonar scanner is integrated in most major code flow platforms. It is executed in final stages of the build process when the build environment is in its final state. This is necessary so that the scan results pertain to the actual components that will be deployed. The build environment contains all the built binaries and necessary dependencies to compile and apply any post-build processing.
Even if the code changes and dependencies are technically sound and they compile to produce an output, they might affect code outside immediate attention. This is especially important for junior developers or new teammates on complex code bases. Solution to ensure that a change has not adversely affected unintended area is unit testing. Unit testing essentially calls the methods for which it is intended, passing certain values and asserting their returns. If the condition is not met, the test fails and stops the process. This helps maintain the integrity of the code and avoid the embarrassment of finding bugs in QA.
Sonar scanner executes after the unit tests and consumes the report produced by them to incorporate the coverage (percentage of methods for which unit test exist that exercise all intended and erroneous code paths). Sonar scanner executes on the build environment, because the environment contains everything for the build to happen and its state affects the outcome. It would be rather complex and expensive to duplicate that environment on the Sonar side and consistency with build environments would be hard to maintain. It would also violate the “build once, deploy multiple times” principle that what is scanned ends up deployed. Otherwise, the same code built in two distinct build environments might not produce the same output and the scan results might vary.
While Sonar offers server-side scan on upload of the repository, the results produced during regular CI/CD process are the most relevant to the state of production.


Set-up process:
1. Go to the SonarCloud website and click Sign up or Login. Choose to authenticate with your GitHub account.
2. Authorize SonarCloud to access your GitHub account. The process will guide you to install the SonarCloud application on GitHub, which allows it to access your repositories.
3. Once logged in, click the + Analyze new project button on your SonarCloud dashboard.
4. SonarCloud will display a list of your GitHub repositories. Select the existing project you want to analyze and click Set Up.
5. Choose one of two analysis methods:
- Automatic, where SonarCloud attempts to analyze your code from GitHub "server-side".
- CI-based, which entails setting up a workflow in GitHub Actions to perform the analysis during a build.
 - In SonarCloud, go to My Account > Security and generate a new token for your project. Copy it immediately as you won't be able to retrieve it again.
 - In your GitHub repository, go to Settings > Secrets and variables > Actions. Click New repository secret and create a secret named SONAR_TOKEN. Paste the token value you copied from SonarCloud.
 - In your GitHub project, edit the workflow YML file. Add a step to run the official SonarScanner GitHub Action. This step uses the SONAR_TOKEN secret we just created.
 - Commit the updated workflow file and push it to your GitHub repository.
 - This will trigger the job with scan and send the results to SonarCloud.
 - See the analysis report on your SonarCloud project dashboard.

Example for a GitHub Actions workflow:

name: SonarCloud Analysis
on:
  push:
    branches:
      - main
  pull_request:
    types: [opened, synchronize, reopened]
jobs:
  sonarcloud:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@<action version>
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
