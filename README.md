# Tutorial content

### [Link to live content](https://louisdewar.github.io/tutorial_web_content/).

This repo houses the content for tutorials, see [this repo](https://github.com/louisdewar/tutorial_web) for the code that builds the websites.

## ==Quickstart==
I want to get started straight away!

### Mac/Linux(/Windows with linux subsystem)
1. Clone this repo and open a terminal in that folder
2. (Optional - run_server.sh will run this script anyway) Run `python3 install.py`
3. Run `./run_server.sh`

### Windows
1. Clone this repo
2. Run `python3 install.py` (make sure you have python3 installed)
4. cd (change directory) using command prompt into folder where this repository was cloned
5. Run `bin/tutorial_web.exe --help` for help OR `bin/tutorial_web.exe start-test-server -s bin/static -i courses` to start the server

## How does it work?

You write courses in `.yml` files (YAML) and then the code reads them and builds websites from them. Checkout the `courses` folder for examples of how other courses used them.

Also see [these examples](https://github.com/louisdewar/tutorial_web/tree/master/courses/example) for some other examples explaining how it works.

## Folder structure

All the content is in the `courses` folder. Within that folder there are course group folders (e.g. `courses/python`) which house a series of similar courses.
If you want to include assets with your project you must name the folder the same as the `.yml` file. See [this](https://github.com/louisdewar/tutorial_web/blob/master/courses/example/demonstrating_assets.yml) for more information.

## How do I view the result?

All the courses are automatically rendered [here](https://louisdewar.github.io/tutorial_web_content/).

If you want to view them locally run the script called `run_server.sh` (this should help you install everything you need).

## How do I view the result of a pull request?

All pull requests are automatically rendered [here](http://dev.tutorial.dewardt.uk/) (once the pull request is closed the deployment disappears).

## How do I build static content?

Usage instructions are included with all releases (once you install locally see the `bin` folder). But you can find the latest instructions [here](https://github.com/louisdewar/tutorial_web/blob/master/USAGE.md).

You can also look at the [build script](./build.sh) in this repo or run `tutorial_web build --help` for some information on running the command.
