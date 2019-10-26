# Tutorial content

### [Link to live content](https://louisdewar.github.io/tutorial_web_content/).

This repo houses the content for tutorials, see [this repo](https://github.com/louisdewar/tutorial_web) for the code that builds the websites.

## How does it work?

You write courses in `.yml` files (YAML) and then the code reads them and builds websites from them. Checkout the `courses` folder for examples of how other courses used them.

Also see [these examples](https://github.com/louisdewar/tutorial_web/tree/master/courses/example) for some other examples explaining how it works.

## Folder structure

All the content is in the `courses` folder. Within that folder there are course group folders (e.g. `courses/python`) which house a series of similar courses.
If you want to include assets with your project you must name the folder the same as the `.yml` file. See [this](https://github.com/louisdewar/tutorial_web/blob/master/courses/example/demonstrating_assets.yml)

## How do I view the result?

All the courses are automatically rendered [here](https://louisdewar.github.io/tutorial_web_content/).

If you want to view them locally run the script called `run_server.sh` (this should help you install everything you need).

## How do I build static content?
This question is best answered on the repository that handles the code.

Usage instructions are included with all releases (once you install locally see the `bin` folder). But you can find the latest instructions [here](https://github.com/louisdewar/tutorial_web/blob/master/USAGE.md)
