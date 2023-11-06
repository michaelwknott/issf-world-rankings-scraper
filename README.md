# python-project-template
A starter repo for a Python app.

## Demo
Include a demo gif or screenshot in this section to highlight your project in action.

## About the Project
Include a description of your project here.

## Built With
List the frameworks/libraries your project uses here.

## Getting Started

### Prerequisites
List the things a developer must install before running your project here.

### Installation

1. Clone the repo
    ```
    git clone git@github.com:michaelwknott/python-project-template.git
    ```

2. Create a virtual environment
   ```
   python -m venv .venv --prompt .
   ```

3. Activate your virtual environment
   ```
   .venv/bin/activate
   ```

4. Install requirements
   ```
   python -m pip install requirements.txt
   ```

## Usage
Include any relevant instructions on using your project here.

## Contributing

1. Fork the Project. See the following [instructions](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) for more information

1. Create a local clone of your fork. Ensure you change the repo address between the angle brackets to your fork's address
```
git clone <git@github.com:michaelwknott/python-project-template.git>
```

1. Create a virtual environment
   ```
   python -m venv .venv --prompt .
   ```

1. Activate your virtual environment
   ```
    .venv/bin/activate
    ```

1. Install project requirements and development requirements
```
python -m pip install -r requirements.txt -r requirements-dev.txt
```

1. Install pre-commit hooks
```
pre-commit install
```

1. Create `.git_commit_msg.txt` to use as your commit message template. A template can be found [here](https://gist.github.com/michaelwknott/67ca1a2bbd815749f5fba7a983cd2b9c) or see the following [instructions](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration) for m
ore information 

1. Add `.git_commit_msg.txt` to use as your commit message template
```
git config commit.template .git_commit_msg.txt
```

1. Create a feature branch
```
git checkout -b <feature-branch>
```

1. Make your changes and commit them
```
git add .
git commit
```

1. Push your changes to your fork
```
git push origin <feature-branch>
```

1. Create a pull request. See the following [instructions](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) for more information
